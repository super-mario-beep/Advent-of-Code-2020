#https://adventofcode.com/2020/day/2

file1 = open('Day 1\input.txt', 'r') 
Lines = file1.readlines() 

count = 0
for line in Lines: 
    startPos = line[0:line.index("-")]
    endPos = line[line.index("-")+1:line.index(" ")]
    letter = line[line.index(" ")+1:line.index(":")]
    string = line[line.index(":")+2:len(line)-1] + "___"
    
    list_ = [pos for pos, char in enumerate(string) if char == letter]
    if (int(endPos)-1 in list_ or int(startPos)-1 in list_) and not (int(endPos)-1 in list_ and int(startPos)-1 in list_):
        count += 1

    #numChar = 0
    #for char in string:
        #if char == letter:
            #numChar += 1   
    #if string.find(letter) == int(startPos)
    #if string[int(startPos)-1] == letter or string[int(endPos)-1] == letter:
        #count += 1

print(count)   
file1.close()


