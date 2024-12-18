### read files 

def read_file_splitlines(filename):
    return(open(filename,"r").read().splitlines())


rules = read_file_splitlines("Input day 5 - 1.txt")
rules = [row.split("|") for row in rules]


manuals = read_file_splitlines("Input day 5 - 2.txt")
manuals = [manual.split(",") for manual in manuals]


def is_rule_broken(manual,rule):
    try:
        pos_first = manual.index(rule[0])
        pos_second = manual.index(rule[1])
    except:
        return(False)

    if (pos_first > pos_second):
        return(True)
    else:
        return(False)


def is_manual_valid(manual,rules):
    for rule in rules:
        if is_rule_broken(manual,rule):
            return(False)
    return(True)


valid_manuals = []
invalid_manuals = []
for manual in manuals:
    if is_manual_valid(manual,rules):
        valid_manuals.append(manual)
    else:
        invalid_manuals.append(manual)

import math

def get_center_number(l):
    return(l[math.floor(len(l)/2)])

n=0
for manual in valid_manuals:
    n = n + int(get_center_number(manual))
print(n)

### 2
def fix_broken_rule(manual,rule):
    pos_first = manual.index(rule[0])
    pos_second = manual.index(rule[1])

    manual[pos_first]="Ø"
    manual.insert(pos_second,rule[0])
    manual.remove("Ø")

    return(manual)

def check_and_fix_manual(manual,rule):
    try:
        pos_first = manual.index(rule[0])
        pos_second = manual.index(rule[1])
    except:
        return(manual)

    if (pos_first > pos_second):
        return(fix_broken_rule(manual,rule))
    else:
        return(manual)

def check_and_fix_manual_complete(manual,rules):
    i=0
    while (not is_manual_valid(manual,rules) and i < 100000):
        for rule in rules:
            manual = check_and_fix_manual(manual,rule)
    if i != 100000:
        return(manual)
    else:
        print("CANT BE FIXED")
        return -1

fixed_manuals = []
for manual in invalid_manuals:
    manual_fixed = check_and_fix_manual_complete(manual,rules)
    fixed_manuals.append(manual_fixed)

n=0
for manual in fixed_manuals:
    n = n + int(get_center_number(manual))
print(n)


