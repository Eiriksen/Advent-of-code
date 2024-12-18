### General functions 

def file_read_lines(filename):
    with open(filename) as fil:
        file=fil.readlines()
    return(file)

def prep_list(length):
   return([ [] for i in range(length)])

def remove_from_list(li,index):
    return(li[:index] + li[index+1 :])

import re

def str_numbers_extract(string):
    res = re.findall(r'\d+', string)
    res=list(map(int, res))
    return(res)











### Executing Part 1 ------------------------------------

file = file_read_lines("input day 3.txt")

file_singleline = "".join(file)

list_muls = re.findall("mul\([0-9]*,[0-9]*\)",file_singleline)

def mul_multiply(mul):
    # get numbers in mul
    numbers = str_numbers_extract(mul)
    return(numbers[0]*numbers[1])

sum_muls = 0 
for mul in list_muls:
    sum_muls = sum_muls + mul_multiply(mul)
print(sum_muls)










### Part 2 ------------------------------------------

list_megamuls = re.findall("mul\([0-9]*,[0-9]*\)|do\(\)|don't\(\)",file_singleline)

sum_megamuls = 0
cur_state = 1
for i in range(0,len(list_megamuls)):
    operation = list_megamuls[i]
    if operation == "do()":
        cur_state = 1
    elif operation == "don't()":
        cur_state = 0
    else:
        if cur_state == 1:
            sum = sum_megamuls = sum_megamuls + mul_multiply(operation)

print(sum_megamuls)
