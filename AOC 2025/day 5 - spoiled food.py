# Day 5: we have two lists, one list of ranges (e.g 1-20) and one list of numbers
# The list of numbers represent food items: any food items existing within any of the ranges are considered not spoiled
# Task 1: Find the number of non-spoiled food items in the list of food items
# Task 2: Find the total number of non-spoiled food items 



### 1: Load data and find number of non-spoiled items in the list -----------------------

input = open("AOC 2025/input day 5.txt").read().splitlines()
index_split = input.index("")

input_rng = [[int(i) for i in line.split("-")] for line in input[:input.index("")]]
input_food = [int(line) for line in input[input.index("")+1:]]

def is_spoiled(i):
  global input_rng
  for rng in input_rng:
    if i >= rng[0] and i <= rng[1]:
      return(False)
  return(True)

# RESULT 1:
len([food for food in input_food if not is_spoiled(food)])





### 2: Find the total number of non-spoiled food items ----------------------------------
# Solution: resolve all overlaps in the list of ranges, then count the total width of all the ranges


def does_overlap(a,b):
  if a[0] > b[1] or b[0] > a[1]:
    return(False)
  else:
    return(True)

def resolve_overlap(a,b):
  if does_overlap(a,b):
    return([min(a+b),max(a+b)])
  else:
    return(False)

def attempt_merge_index(li,i):
  j = i+1
  while j < len(li):
    overlap = resolve_overlap(li[i],li[j])
    if not overlap:
      j=j+1
    else:
      li[i] = overlap
      li = [li[z] for z in range(0,len(li)) if z!= j]
      j=i+1
  return(li)

def merge_all(li):
  i = 0 
  while i < len(li):
    li = attempt_merge_index(li,i)
    i+=1
  return(li)

def flatten(lili):
    return [i for li in lili for i in li]

# RESULT 2
sum([i[1]-i[0]+1 for i in merge_all(input_rng)])


