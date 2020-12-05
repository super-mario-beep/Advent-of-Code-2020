#https://adventofcode.com/2020/day/3
def addRepeatableMap(map_):
    tmp = []
    for line in map_:
        ll = line + line
        tmp.append(ll)
    return tmp

def calculateTrees(x_,y_):
    map_ = [line.strip() for line in open("Day 3/input.txt", "r")] 
    x = y = count = 0
    for index in range(0,len(map_),2):
        line = map_[index]
        if len(line) <= x + x_:
            map_ = addRepeatableMap(map_)
        if(line[x] == "."):
            tmp = list(line)
            tmp[x] = "O"
            map_[index] = "".join(tmp)     
        elif line[x] == "#":
            count += 1
            tmp = list(line)
            tmp[x] = "X"
            map_[index] = "".join(tmp)  
        
        x += x_
    if y_ == 2:
        pass#print(map_)
    print(y_)
    return count

#x1 = calculateTrees(1,1)
#x2 = calculateTrees(3,1)
#x3 = calculateTrees(5,1)
#x4 = calculateTrees(7,1)
x5 = calculateTrees(1,2)
    
print(x5)
print(60*191*64*63*32)
#print(map_)
#map_ = addRepeatableMap(map_)
#print(map_)
#60
#191
#64
#63
#32
    
