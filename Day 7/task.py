#https://adventofcode.com/2020/day/7

def readMapFromLine(line):
    type_of_bag = line[0:line.find("bag")]
    if type_of_bag[len(type_of_bag)-1] == " ":
            type_of_bag = type_of_bag[0:len(type_of_bag)-1]
    nums = []
    com = []
    bags = []
    map_ = {}
    map_["color"] = type_of_bag
    for i in range(len(line)): 
        if line[i].isdigit():
            nums.append(i)
        elif line[i] == "," or line[i] == ".":
            com.append(i)
    if "no other bags" in line:
        tmp_ = {}
        tmp_["color"] = type_of_bag
        tmp_["bags"] = []
        return tmp_
    for i in range(len(com)):
        tmp_ = {}
        color = line[nums[i]+2:com[i]-4]
        if color[len(color)-1] == " ":
            color = color[0:len(color)-1]
        tmp_["color"] = color
        tmp_["bags"] = []
        bags.append(tmp_)
    map_["bags"] = bags
    return map_
    
def combine(map1,color,res):
    if type(map1) == str:
        return False
    if not map1["color"]:
        return False
    if map1["color"] == color:
        map1["bags"] = (res["bags"])
        return True
    if map1["bags"]:
        for bag in map1["bags"]:
            combine(bag,color,res)
    else:
        return False
    
def contains(map1,color):
    if map1["color"] == color:
        return True
    if map1["bags"]:
        print(map1["bags"])
        for i in range(len(map1["bags"])):
            tmp = map1["bags"][i]
            return contains(tmp,color) 
        


lines = [line.strip() for line in open("Day 7/input.txt", "r")]
bags = []
for line in lines:
    bags.append(readMapFromLine(line))


for map_ in bags:
    for _map in bags:
        if _map["color"] != map_["color"]:
            combine(map_,_map["color"],_map)

            
counter = 0   
find_color = "shiny gold"
for bag in bags:
    if bag["color"] != find_color and contains(bag, find_color):
        counter+=1
        
print(counter)



            
#print(len(bags))
#print(bags[2].bags[0].bags)