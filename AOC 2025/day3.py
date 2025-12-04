# Day 1, turning on batteries, or finding the largest n-digit number you can make from a string of numbers, picking the numbers in the order they appear
# Task 1: finding the largest 2-digit numbers and summing them

def locate_in_list(li,x):
   return([i for i, z in enumerate(li) if z==x])

def get_2batteries(bank):
  bank = [int(i) for i in bank]
  block1 = bank[0:len(bank)-1]
  b1 = max(block1)
  pos1 = locate_in_list(block1,b1)[0]
  block2 = bank[pos1+1:len(bank)]
  b2 = max(block2)
  return(10*b1+1*b2)

input = open("AOC 2025/input day 3.txt","r").read().splitlines()

# RESULT task 1:
sum([get_2batteries(i) for i in input])


# Task 2: finding the largest 12-digit numbers and summing them

def collapse_to_int(li):
  string = ""
  for i in li:
    string = string + str(i)
  return(int(string))

def get_nth_battery(block,nrest):
  block = [int(i) for i in block]
  subblock = block[0:len(block)-nrest]
  battery = max(subblock)
  pos = locate_in_list(subblock,battery)[0]
  restblock = block[pos+1:len(block)]
  return([battery,restblock])

def get_nbatteries(bank,n):
  curbank = bank
  batteries = []
  for i in range(1,n+1):
    # nth battery
    nrest = n-i
    search = get_nth_battery(curbank,nrest)
    batteries.append(search[0])
    curbank = search[1]
  return(collapse_to_int(batteries))

# RESULT Task 2
sum([get_nbatteries(i,12) for i in input])
