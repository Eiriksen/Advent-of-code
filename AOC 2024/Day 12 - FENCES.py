
### general functions ---------------------------

import copy
import math
import time

def out_of_bounds(p,table):
    if p[0] < 0 or p[1] < 0:
        return(True)
    elif p[0] > len(table)-1 or p[1] > len(table[p[0]])-1:
        return(True)
    else:
        return(False)

def pad_map(table):
    width = len(table[0])
    table.insert(0,["Ø"]*width)
    table.append(["Ø"]*width)
    for i in range(0,len(table)):
        table[i].insert(0,"Ø")
        table[i].insert(len(table[i]),"Ø")
    return(table)


def get_relPos(pos,direction,speed):
    # return relative position
    radians = direction*math.pi/180
    delta_x = round(math.cos(radians)*speed)
    delta_y = round(math.sin(radians)*speed)
    return([pos[0]+delta_x,pos[1]+delta_y])

def get_symbol(pos,table):
  if out_of_bounds(pos, table):
    return(None)
  else:
    return(table[pos[0]][pos[1]])

def save_map_gen(t,filename):
    m = [[list(map(str,i)) for i in a] for a in t]
    m = [[item for col in row for item in col] for row in m]
    m = ["".join(i) for i in m]
    with open(filename, 'w') as f:
        for line in m:
            f.write(f"{line}\n")

def get_index_of_all(l,value):
    return([i for i,val in enumerate(l) if val==value])

def get_pos_of_all(what,table):
    list_pos = []
    # return positon of symbol in a table
    # table is x-y table
    # find which row:
    for i in range(0,len(table)):
        indexes = get_index_of_all(table[i],what)
        for j in indexes:
            list_pos.append([i,j])
    return(list_pos)

def correct_direction(direction):
    while direction > 360:
        direction -=360
    while direction < 0:
        direction +=360
    return(direction)











### Part 1 functions  -------------------------------------------


def robot(pos, index_memory=0, init=True):
    global map_base
    global map_covered
    global memory_robot

    symbol_at_pos = map_base[pos[0]][pos[1]]

    # if this is the first square
    if init:
       index_memory = len(memory_robot)
       # first in memory is area, second is fence, third is wallnumber (for part #2)
       memory_robot.append([0,0])
 
    # paint you current position "#"
    map_covered[pos[0]][pos[1]] = "Ø"
    # increase area count
    memory_robot[index_memory][0] += 1

    # go through each of the four directions
    for i in [0,90,180,270]:
        pos_next = get_relPos(pos,i,1)
        # check if we can place a new robot at this location (check against X, out of bounds, or other letter)        
        if get_symbol(pos_next,map_covered) == symbol_at_pos:
          # launch new robot
          robot(pos_next,index_memory,init=False)
    
        # check if this direction needs a fence (check against other letters or out of bounds)
        # we can't check map_covered here because of mixing X in this area with other areas
        if get_symbol(pos_next,map_base) != symbol_at_pos:
          # increase fence count
          memory_robot[index_memory][1] +=1
        # else do nothing



# Executing part 1 ----------------------------------


input_day_12 = open("input day 12.txt","r").read().splitlines()
map_base = [ [a for a in i] for i in input_day_12]
map_covered = copy.deepcopy(map_base)
memory_robot = []

for i_x in range(0,len(map_covered)):
    for i_y in range(0,len(map_covered[i_x])):
        symbol = get_symbol([i_x,i_y],map_covered)
        if symbol != "Ø":
            robot([i_x,i_y,map_covered])

n=0
for i in memory_robot:
    n += i[0]*i[1] 
print(n)












### Part 2 functions ---------------------------------

def robot2(pos, index_memory=0, init=True):
    global map_base
    global map_covered
    global map_fence
    global memory_robot

    symbol_at_pos = map_base[pos[0]][pos[1]]

    # if this is the first square
    if init:
        index_memory = len(memory_robot)
        map_fence = copy.deepcopy(map_base)
        # first in memory is area, second is fence, third is wallnumber (for part #2)
        memory_robot.append([0,0,0])

    # paint you current position "#"
    map_covered[pos[0]][pos[1]] = "Ø"
    map_fence[pos[0]][pos[1]] = "#"
    # increase area count
    memory_robot[index_memory][0] += 1

    # go through each of the four directions
    for i in [0,90,180,270]:
        pos_next = get_relPos(pos,i,1)
        # check if we can place a new robot at this location (check against X, out of bounds, or other letter)        
        if get_symbol(pos_next,map_covered) == symbol_at_pos:
            # launch new robot
            robot2(pos_next,index_memory,init=False)
    
        # check if this direction needs a fence (check against other letters or out of bounds)
        # we can't check map_covered here because of mixing X in this area with other areas
        if get_symbol(pos_next,map_base) != symbol_at_pos:
            # increase fence count
            memory_robot[index_memory][1] +=1
            # mark the fence map with $ for fence outside the fence map
            map_fence[pos_next[0]][pos_next[1]] = "$"
            # else do nothing


def detect_wall(pos,symbol,direction,t_map):
    sym_pos = get_symbol(pos,t_map)
    sym_wall = get_symbol(get_relPos(pos,direction,1),t_map)

    if sym_pos == symbol and sym_pos != sym_wall:
        return(True)
    else:
        return(False)

# wallwalker:
def wallwalker(pos, direction, init=True, index_memory=None,  pos_start=None, direction_start=None):
    global map_base
    global memory_robot

    pos_fence = get_relPos(pos,direction+90,1)
    map_fence[pos_fence[0]][pos_fence[1]] = "Ø"

    if init:
        # first instance
        # assumes it has been launched right after the robot which searched the same area
        pos_start = pos
        direction_start = direction
    else:
        # if not first, check if it is back at the OG location
        if pos == pos_start and correct_direction(direction) == direction_start:
            return(0)

    # check for walls at next position
    sym_pos = get_symbol(pos,map_base)
    pos_next = get_relPos(pos,direction,1)
    if detect_wall(pos_next, sym_pos, direction+90,map_base):
        # wall found as expected, continue
        wallwalker(pos_next, direction, False, index_memory, pos_start, direction_start)

    else:
        # if not: add +1 walls (since we essentially found  a new one)
        memory_robot[index_memory][2] += 1
        # find where the next wall continues, 
        # i.e. either +90 degrees or -90 degrees
        # -90, "to the right"
        if detect_wall(pos, sym_pos, direction, map_base):
            wallwalker(pos, direction-90, False, index_memory, pos_start, direction_start)
        # +90, next wall must be to the left, around the corner
        else:
            # 
            wallwalker(pos_next, direction+90, False, index_memory, pos_start, direction_start)

# wallfinder:
def launch_wallwalker(pos, index_memory):
    global map_base
    global map_fence
    # starts at some posititon

    # checks if it stands on a fence "$"
    sym_pos = get_symbol(pos,map_fence)
    if sym_pos == "$":
        # 1: check for walls
        for direction in [0,90,180,270]:
            pos_next = get_relPos(pos,direction,1)
            sym_next = get_symbol(pos_next, map_fence)
            if sym_next == "#":
                wallwalker(pos_next, correct_direction(direction+90), index_memory=index_memory )
                return(1)
    # 2: if not, do nothing

def count_sides():
    global map_fence
    index_memory = len(memory_robot)-1
    for i_x in range(0,len(map_fence)):
        i_y = 0
        column = map_fence[i_x]
        while column.count("$") != 0:
            launch_wallwalker([i_x,i_y], index_memory)
            i_y+=1



###  Executing part 2 --------------------------------

input_day_12 = open("input day 12.txt","r").read().splitlines()
map_base = pad_map([ [a for a in i] for i in input_day_12])
map_covered = copy.deepcopy(map_base)
map_fence = copy.deepcopy(map_base)
memory_robot = []

for i_x in range(0,len(map_covered)):
    for i_y in range(0,len(map_covered[i_x])):
        symbol = get_symbol([i_x,i_y],map_covered)
        if symbol != "Ø":
            robot2([i_x,i_y])
            count_sides()

n=0
for i in memory_robot:
    n += i[0]*i[2] 
print(n)
