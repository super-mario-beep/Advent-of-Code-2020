#https://adventofcode.com/2020/day/6
groups = [line.strip() for line in open("Day 6/input.txt", "r")] 

ans = {}
count = 0
l = 0
for line in groups:
    if len(line) < 1:
        for key in ans.keys():
            if ans[key] == l:
                count += 1
        ans = {}
        l = 0
    else:
        l += 1
        for char in line:
            if not char in ans:
                ans[char] = 1
            else:
                ans[char] = ans[char] + 1
            
for key in ans.keys():
    if ans[key] == l:
        count += 1
print(count)


