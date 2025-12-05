# input is essentially a list of numbers, but formatted in a way that we need to expand first
# task is the sum all the "fake" numbers
# task1 : a number is fake if it is entirely made up of two repeating numbers eg "22" or "2323" or "123123"
# task2: a number is fake it is is entirely made up of *some sequence* of repeating numbers e.g "22" "232323" "123123123123"



### 1 load input and get number of fake numbers -----------------------------------------
input_day2 = open("AOC 2025/input day 2.txt").read().split(",")
# epand the list of numbers:
input_split = [str.split("-") for str in input_day2]
input_expanded = [list(range(int(i[0]),int(i[1])+1)) for i in input_split]

def flatten(lili):
    return [i for li in lili for i in li]

input_all = flatten(input_expanded)

def is_repeated(item):
  item = str(item)
  # if the length is odd, the item can't be a repeat
  if len(item) % 2 != 0:
    return(False)
  # check if the first half equals the latter half
  firsthalf = item[0:int(len(item)/2)]
  secondhalf = item[int(len(item)/2):len(item)]
  if firsthalf == secondhalf:
    return(True)
  else:
    return(False)

def is_fake(item):
  item = str(item)
  if item[0:1] == 0:
    return(True)
  if is_repeated(item):
    return(True)
  else:
    return(False)

# RESULT: Sum of fake numbers
input_onlyfake = [(item if is_fake(item) else 0) for item in input_all]
print(sum(input_onlyfake))





### part 2 different definition of fake numbers -----------------------------------------

#find all the ways you can evenly split a sequence
def get_possible_splits(item):
  out = []
  leni = len(item)
  for i in range(2,leni):
    if leni % i == 0:
      out.append(i)
  out.append(leni)
  return(out)

# split a string in n equal parts
def split_in(item,n):
  sl = int(len(item)/n)
  parts = []
  for i in range(0,n):
    parts.append(item[i*sl:(i+1)*sl])
  return(parts)

# check if all elements in a list are equal
def all_equal(li):
  if [i == li[0] for i in li].count(True) == len(li):
    return(True)
  else:
    return(False)

# v2 of the fake check
def is_fake2(item):
  item = str(item)
  # numbers of length 1 can't be repeats:
  if len(item) == 1:
    return(False)
  # use the functions above to perform all possible splits, and check if they result in equal numbers
  for split in get_possible_splits(item):
    if all_equal(split_in(item,split)):
      return(True)
  return(False)


# RESULT: sum of all fake items
input_onlyfake2 = [(item if is_fake2(item) else 0) for item in input_all]
print(sum(input_onlyfake2))

