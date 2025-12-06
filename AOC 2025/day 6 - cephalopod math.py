# Day 6, we're doing cephalopod math. This one is mostly about reading inputs in weird formats
# Task 1: sum or multiply all numbers per column, depending on what operator that column ends with
# Task 2: The actually columns have to be transposed 90 degrees and read "down and right"

import math

#### Task 1 -----------------------------------------------------------------------------

input = open("AOC 2025/input day 6.txt").read().splitlines()

in_nums = [[int(i) for i in line.rsplit()] for line in input[0:-1]]
in_operators = input[-1].rsplit()

list_output = []

for icol in range(0,len(in_operators)):
  operator = in_operators[icol]
  nums = [in_nums[irow][icol] for irow in range(0,len(in_nums))]
  match operator:
    case "*":
      list_output += [math.prod(nums)]
    case "+":
      list_output += [sum(nums)]

# RESULT
sum(list_output)


### Task 2 --------------------------------------------------------------------------------
# Here, we simply rotate the entire inout 90 degrees before proceeding

def prep_list(length):
  return([ [] for i in range(length)])

def rotate_table_90(table):
    n_cols = len(table[0])
    table_rotated = prep_list(n_cols)
    for i_row in range(0,len(table)):
        for i_col in range(0,len(table[i_row])):
            print(i_row) 
            print(i_col)
            cur_newrow = len(table[i_row]) - 1 - i_col
            table_rotated[cur_newrow].append(table[i_row][i_col])
    return(table_rotated)

def flatten_list(l):
    return [item for sublist in l for item in sublist]

# turn the input into a table
input_table = [[i for i in row] for row in input]
# rotate that table 90 degrees
input_table_90deg = rotate_table_90(input_table)
# turn the table into a list of numbers, each problem is separeated by an empty item
input_listed = ["".join(row[0:-1]).strip() for row in input_table_90deg]

def list_split(li,x):
  out = []
  cursublist = []
  for item in li:
    if item == x:
      out.append(cursublist)
      cursublist=[]
    else:
      cursublist.append(item)
  out.append(cursublist)
  return(out)

# turn the listed table into a list of sublist, in which each sublist is one "problem" i.e. set of numbers to either multiply or sumw
list_problems = list_split(input_table3,"")

# iterate over each problem, sum or multiply based on the list of operators
list_output = []
for i in range(0,len(list_problems)):
  operator = in_operators[-(i+1)]
  problem = [int(j) for j in list_problems[i]]
  match operator:
    case "*":
      list_output += [math.prod(problem)]
    case "+":
      list_output += [sum(problem)]

# RESULT
sum(list_output)
