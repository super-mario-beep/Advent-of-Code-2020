#https://adventofcode.com/2020/day/5
seats = [line.strip() for line in open("Day 5/input.txt", "r")] 
def calcRow(info):
    max_ = 127
    min_ = 0
    for i in range(7):
        if info[i] == "B":
            min_ = int((max_+min_)/2)
        else:
            max_ = int((max_+min_)/2)
    return max_
def calcSeat(info):
    max_ = 7
    min_ = 0
    for i in range(7,10,1):
        if info[i] == "R":
            min_ = int((max_+min_)/2)
        else:
            max_ = int((max_+min_)/2)
    return max_
    
high = 0
l = []
for line in seats:    
    row = calcRow(line)
    seat = calcSeat(line)
    total = row * 8 + seat
    l.append(total)
    if total >= high:
        high = total
print(high)

l.sort()
for i in range(len(l)):
    if l[i] != i+32:
        print(i+32)
        break
    
