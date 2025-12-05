# https://adventofcode.com/2025/day/1
# Input: a list of commands for a dial, e.g. "R90" means click 90 times right
# Environment: a dial which goes from 0 to 99, and which does not stop at the 0 location
# Task 1: How many times does the dial touch "0" after a command, for the the given input?



### 1: read input and count number of zeroes --------------------------------------------
input_day1 = open("AOC 2025/input day 1.txt","r").read().splitlines()

# establis a list of all the positions the dial has had
list_positions = [50]

# for each command:
for row in input_day1:
  # separate the direction and the increment
  direction_letter = row[0]
  increment = int(row[1:20])
  # turn the direction letter into "1" or "-1"
  direction = 0
  match direction_letter:
    case "R":
      direction = 1
    case "L":
      direction = -1
  # get the previous position
  pos_old = list_positions[-1]
  # get the new position
  pos_new = pos_old + direction*increment
  # account for the fact that the dial goes past 0 and 99, and reset back to a number 0-99
  # divmod does just this
  pos_new = divmod(pos_new,100)[1]
  # append the new location to the list
  list_positions.append(pos_new)

# RESULT: count the number of zeroes
print(list_positions.count(0))





#### 2: How many times does the dial touch 0 altogether? --------------------------------
# establis a list of all the positions the dial has had

list_positions = [50]
n_clicks = 0

# for each command:
for row in input_day1:
  # separate the direction and the increment
  direction_letter =  row[0]
  increment = int(row[1:20])
  # turn the direction letter into "1" or "-1"
  direction = 0
  match direction_letter:
    case "R":
      direction = 1
    case "L":
      direction = -1
  # get the previous position
  pos_old = list_positions[-1]
  # get the new position
  pos_new = pos_old + direction*increment
  # get all positions between (+1 because of weird range function, and to not reuse the old pos)
  list_pos = list(range(pos_old+direction,pos_new+direction,direction))
  # turn all positions to dial positions
  list_pos_dial = [divmod(pos,100)[1] for pos in list_pos]
  # count zeroes
  clicks = list_pos_dial.count(0)
  # add zeroes to n_clicks
  n_clicks = n_clicks+clicks
  # update the latest position
  pos_new_dial = divmod(pos_new,100)[1]
  list_positions.append(pos_new_dial)


# RESULT: count the number of "clicks"
print(n_clicks)
