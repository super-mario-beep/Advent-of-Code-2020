#https://adventofcode.com/2020/day/4

import re
def checkIsValid(items):
    keys = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
    for key in keys:
        if key not in items:
            return False
    return True

def stringToItem(string,item_):
    item = item_
    if "byr" in string:
        i = string.find("byr")
        item["byr"] = string[i+4:i+8]
        if not (2002 >= int(item["byr"]) >= 1920):
            del item["byr"]
    if "iyr" in string:
        i = string.find("iyr")
        item["iyr"] = string[i+4:i+8]
        if not (2020 >= int(item["iyr"]) >= 2010):
            del item["iyr"]
    if "eyr" in string:
        i = string.find("eyr")
        item["eyr"] = string[i+4:i+8]    
        if not (2030 >= int(item["eyr"]) >= 2020):
            del item["eyr"]
    if "hgt" in string:
        i = string.find("hgt")
        item["hgt"] = string[i+4:i+9]
        if "cm" in item["hgt"]:
            i_ = item["hgt"].find("cm")
            s_ = item["hgt"]
            hgt = int(s_[0:i_])
            if not(193 >= hgt >= 150):
                del item["hgt"] 
        elif "in" in item["hgt"]:
            i_ = item["hgt"].find("in")
            s_ = item["hgt"]
            hgt = int(s_[0:i_])
            if not(76 >= hgt >= 59):
                del item["hgt"]
        else:
            del item["hgt"]
    if "hcl:#" in string:
        i = string.find("hcl")
        if re.match("^[A-Fa-f0-9]*$", string[i+5:i+11]):   
            item["hcl"] = string[i+5:i+11]            
    if "ecl" in string:
        i = string.find("ecl")
        item["ecl"] = string[i+4:i+7]   
        must = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        if item["ecl"] not in must:
            del item["ecl"] 
    if "pid" in string:
        i = string.find("pid")
        item["pid"] = string[i+4:i+13]  
        if (not (re.match("^[0-9]*$", item["pid"]))) and len(item["pid"]) == 9:
            del item["pid"]          
    return item_
        

items = [line.strip() for line in open("Day 4/input.txt", "r")]
count = 0
cur_item = {}
good = []
for item in items:
    if len(item) == 0:
        cur_item = {}
    else:
        cur_item = stringToItem(item,cur_item)
        if checkIsValid(cur_item):
            good.append(cur_item)
            count += 1
            cur_item = {}
    
tmp = []
for item in good:
    tmp.append({'byr': item["byr"], 'eyr': item["eyr"], 'hgt': item["hgt"], 'hcl': item["hcl"], 'iyr': item["iyr"], 'ecl': item["ecl"], 'pid': item["pid"]})

    
print(count)