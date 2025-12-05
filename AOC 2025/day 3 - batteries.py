# Day 3, turning on batteries, or finding the largest n-digit number you can make from a string of numbers, picking the numbers in the order they appear



### Task 1: finding the largest 2-digit numbers and summing them ------------------------

def locate_in_list(li,symbol):
   return([i for i, x in enumerate(li) if x == symbol])

def get_2batteries(bank):
  bank = [int(i) for i in bank]
  subbank1 = bank[0:len(bank)-1]
  b1 = max(subbank1)
  pos1 = locate_in_list(subbank1,b1)[0]
  subbank2 = bank[pos1+1:len(bank)]
  b2 = max(subbank2)
  return(10*b1+1*b2)

input = open("AOC 2025/input day 3.txt","r").read().splitlines()

# RESULT task 1:
sum([get_2batteries(i) for i in input])





### Task 2: finding the largest 12-digit numbers and summing them -----------------------

def collapse_to_int(li):
  # collapses a list of digis to a single integer
  string = ""
  for i in li:
    string = string + str(i)
  return(int(string))

def get_nth_battery(subbank,nrest):
  # takes a subbank, and finds the highest digit while holding off some number of digits at the end of the subbank (nrest), and returns 1) that highest digit and 2) the remaining subbank (in a list)
  block = [int(i) for i in subbank]
  subbank2 = block[0:len(block)-nrest]
  battery = max(subbank2)
  pos = locate_in_list(subbank2,battery)[0]
  subbank3 = block[pos+1:len(block)]
  return([battery,subbank3])

def get_nbatteries(bank,n):
  subbank = bank
  batteries = []
  for i in range(1,n+1):
    # nth battery
    nrest = n-i
    search = get_nth_battery(subbank,nrest)
    batteries.append(search[0])
    subbank = search[1]
  return(collapse_to_int(batteries))

# RESULT Task 2
sum([get_nbatteries(bank,12) for bank in input])
