#https://adventofcode.com/2020/day/2

file1 = open('Day 1\input.txt', 'r') 
Lines = file1.readlines() 
for line in Lines: 
    for line_ in Lines:
        for l in Lines:
            if int(line_) + int(line) + int(l) == 2020:
                print(int(line_) * int(line) * int(l))
                exit()