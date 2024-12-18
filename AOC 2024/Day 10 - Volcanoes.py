### Basic functions

import math
import copy
import re
import time

def out_of_bounds(p,table):
    if p[0] < 0 or p[1] < 0:
        return(True)
    elif p[0] > len(table)-1 or p[1] > len(table[p[0]])-1:
        return(True)
    else:
        return(False)

def get_relPos(pos,direction,speed):
    # return relative position
    radians = direction*math.pi/180
    delta_x = round(math.cos(radians)*speed)
    delta_y = round(math.sin(radians)*speed)
    return([pos[0]+delta_x,pos[1]+delta_y])

def save_map_gen(t,filename):
    m = [[str(j) for j in i] for i in t]
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


### Part 1

def robot(pos, pos_trailhead=[]):
    global map_base
    global map_peaks
    global map_robot
    global width_map
    global width_map
    global z
    # z+=1
    # if z > 10000:
    #     return(0)

    # check if this position is a trailhead
    if map_base[pos[0]][pos[1]] == "0":
        pos_trailhead = pos
        map_peaks[pos[0]][pos[1]] = 0
        map_robot = copy.deepcopy(map_base)
 

    sym_pos = map_robot[pos[0]][pos[1]]
    if sym_pos == "9":
        # increase the number stored at the trailhead by 1
        map_peaks[pos_trailhead[0]][pos_trailhead[1]]+=1
        # stop procesing
        #save_map_gen(map_peaks, "map_peaks.txt")
        #save_map_gen(map_robot,"map_robot.txt")
        #time.sleep(0.2)
        map_robot[pos[0]][pos[1]] = "X"
        return(0)

    # paint you current position "#"
    map_robot[pos[0]][pos[1]] = "X"

    # go through each of the four directions
    for i in [0,90,180,270]:
        # get next position in this direction
        pos_next = get_relPos(pos,i,1)
        # check that pos is not out of bounds
        if not out_of_bounds(pos_next,map_robot):
            # get symbol
            sym_nexpos = map_robot[pos_next[0]][pos_next[1]]
            # check that symbol is not "X" and that it is an increase by 1
            if (sym_nexpos != "X" and int(sym_nexpos) == int(sym_pos)+1):
                # legal next step! Spawn a new robot there
                #save_map_gen(map_robot,"map_robot.txt")
                #time.sleep(0.2)
                robot(pos_next,pos_trailhead)


input_day10 = open("input day 10.txt","r").read().splitlines()
map_base = [ list(i) for i in input_day10]
width_map = len(map_base)
height_map = len(map_base[1])
map_peaks = [ [ "." for i in range(height_map)] for i in range(width_map)]
map_robot = copy.deepcopy(map_base)

for pos in get_pos_of_all("0",map_base):
    robot(pos)


sum([i for i in [item for sublist in map_peaks for item in sublist] if i != "."])


### 2

## This variant does not have shared global memory of the robot map
## but instead inherits it
## this means that one trail will never have issues crossing one that has been made "paralell"
## - only those made before
def robot2(pos, map_robot=[], pos_trailhead=[]):
    global map_base
    global map_peaks
    #global map_robot
    global width_map
    global width_map
    global z
    # z+=1
    # if z > 10000:
    #     return(0)

    # check if this position is a trailhead
    if map_base[pos[0]][pos[1]] == "0":
        pos_trailhead = pos
        map_peaks[pos[0]][pos[1]] = 0
        map_robot = copy.deepcopy(map_base)
 

    sym_pos = map_robot[pos[0]][pos[1]]
    if sym_pos == "9":
        # increase the number stored at the trailhead by 1
        map_peaks[pos_trailhead[0]][pos_trailhead[1]]+=1
        # stop procesing
        #save_map_gen(map_peaks, "map_peaks.txt")
        #save_map_gen(map_robot,"map_robot.txt")
        #time.sleep(0.2)
        map_robot[pos[0]][pos[1]] = "X"
        return(0)

    # paint you current position "#"
    map_robot[pos[0]][pos[1]] = "X"

    # go through each of the four directions
    for i in [0,90,180,270]:
        # get next position in this direction
        pos_next = get_relPos(pos,i,1)
        # check that pos is not out of bounds
        if not out_of_bounds(pos_next,map_robot):
            # get symbol
            sym_nexpos = map_robot[pos_next[0]][pos_next[1]]
            # check that symbol is not "X" and that it is an increase by 1
            if (sym_nexpos != "X" and int(sym_nexpos) == int(sym_pos)+1):
                # legal next step! Spawn a new robot there
                #save_map_gen(map_robot,"map_robot.txt")
                #time.sleep(0.2)
                robot2(pos_next,copy.deepcopy(map_robot),pos_trailhead)


input_day10 = open("input day 10.txt","r").read().splitlines()
map_base = [ list(i) for i in input_day10]
width_map = len(map_base)
height_map = len(map_base[1])
map_peaks = [ [ "." for i in range(height_map)] for i in range(width_map)]
map_robot = copy.deepcopy(map_base)

for pos in get_pos_of_all("0",map_base):
    robot2(pos)

save_map_gen(map_peaks, "map_peaks.txt")


sum([i for i in [item for sublist in map_peaks for item in sublist] if i != "."])



#Considering its trailheads in reading order, 
#they have ratings of 20, 24, 10, 4, 1, 4, 5, 8, and 5. 
#The sum of all trailhead ratings in this larger
# example topographic map is 81.