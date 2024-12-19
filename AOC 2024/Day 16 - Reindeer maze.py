
### General functions ------------------------------------

import copy
import math
import time
import sys
import re
sys.setrecursionlimit(5000)

def table_minus_one(table):
    for i_x in range(0,len(table)):
        for i_y in range(0,len(table[0])):
            j = table[i_x][i_y]
            if isinstance(j, int) and j > 0:
                table[i_x][i_y] -=1
    return(table)

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

def get_pos_of(what,table):
    # return positon of symbol in a table
    # table is x-y table
    # find which row:
    for i in range(0,len(table)):
        try:
            # will only work if "what" is in the table row
            return([i, table[i].index(what)])
        except:
            next
    return -1

def get_symbol(pos,table):
    if out_of_bounds(pos, table):
        return(None)
    else:
        return(table[pos[0]][pos[1]])


def correct_direction(direction):
    while direction > 360:
        direction -=360
    while direction < 0:
        direction +=360
    return(direction)

def count_area(pos_center,symbol,table):
    count = 0
    for x in [-1,0,1]:
        for y in [-1,0,1]:
            if get_symbol([pos_center[0]+x,pos_center[1]+y],table) == symbol:
                count += 1
    return(count)

def save_map_gen(t,filename):
    m = [list(map(str,i))for i in t]
    m = [[item for col in row for item in col] for row in m]
    m = ["".join(i) for i in m]
    with open(filename, 'w') as f:
        for line in m:
            f.write(f"{line}\n")

def count_in_table(regexp,tab):
    n = 0
    for row in tab:
        n = n + len(re.findall(regexp,row))
    return(n)










### Task 1 V2 functions -----------------------------------

# fills deadways
def fillbot(pos):
    global map_maze

    # paint you current position "#"
    map_maze[pos[0]][pos[1]] = "#"

    # go through each of the four directions
    for i in [0,90,180,270]:
        # get next position in this direction
        pos_next = get_relPos(pos,i,1)
        # get symbol
        sym_nexpos = get_symbol(pos_next,map_maze)
        # check that symbol is not "X", "None, or "#"
        # check also that the next position has no more than 2
        # - "." in its vicinity
        available_directions = sum([(get_symbol(get_relPos(pos_next,i,1),map_maze)==".") for i in [0,90,180,270]])
        if not sym_nexpos in ["X","S","#","None"] and available_directions < 2:
            # legal next step! Spawn a new fillbot there
            fillbot(pos_next)

def reindeer3(pos, direction=0, score=0, trace=[]):
    global memory_reindeer
    global map_maze_3d

    direction = correct_direction(direction)
    axis = {0:0,90:1,180:0,270:1,360:0}[direction]
    sym_pos = get_symbol(pos, map_maze_3d)[axis]
    trace.append(pos)

    if sym_pos == "E":
        # report counts
        print("GOT TO E at ", score, "(", memory_reindeer[0], ")")
        if memory_reindeer[0] == score:
            memory_reindeer[1].append(trace)

        if memory_reindeer[0] == None or memory_reindeer[0] > score:
            memory_reindeer[0] = score
            memory_reindeer[1] = [trace]
        return([])

    # paint you current position with your score
    map_maze_3d[pos[0]][pos[1]][axis] = score
    map_maze[pos[0]][pos[1]] = 3
    #map_live[pos[0]][pos[1]] = "ø"
    #save_map_gen(map_maze,"map_live.txt")
    #time.sleep(0.1)

    # make list of new children
    list_next = []

    # go through each of the four directions
    for i in [direction, direction+90, direction-90]:
        # find what the score would be if moving to this location
        diff_direction = correct_direction(direction-i)
        n_change_direction = {0:0, 90:1, 180: 2, 270:1}[diff_direction]
        new_score = score + n_change_direction*1000 + 1 
        # new score must be lower than the lowest registered score of completion
        if memory_reindeer[0] == None or new_score <= memory_reindeer[0]:
             # get next position in this direction
            pos_next = get_relPos(pos,i,1)
            # get symbol
            sym_nexpos = get_symbol(pos_next,map_maze_3d)[axis]
            # check that symbol is not "X", "None, or "#",
            # if the position contains a score, it must be lower than your current one
            if not sym_nexpos in ["X","#",None]:
                if not isinstance(sym_nexpos, int) or sym_nexpos >= new_score:
                    # legal next step! Spawn a new reindeer there
                    list_next.append([pos_next,i,new_score,copy.deepcopy(trace)])
                #else:
                #print("blocked by path ", new_score, "->", sym_nexpos)
    return(list_next)



### Execute day 1 ------------------------------------

input_day_16 = [list(i) for i in open("Input day 16.txt").read().splitlines()]
map_maze = copy.deepcopy(input_day_16)
memory_reindeer = [None,[]]
pos_start = get_pos_of("S",map_maze)
pos_end = get_pos_of("E",map_maze)
list_reindeer = [[pos_start,90,0,[],200]]


for i_x in range(0,len(map_maze)):
    for i_y in range(0,len(map_maze[0])):
        if get_symbol([i_x,i_y],map_maze) == ".":
            if count_area([i_x,i_y], "#", map_maze) == 7:
                fillbot([i_x,i_y])


map_maze_3d = [[[y,y] for y in x] for x in copy.deepcopy(map_maze)]


a = 0
while a < 1000000:
    a+=1
    list_reindeer = sorted(list_reindeer, key = lambda x: x[4])
    list_reindeer_act  = list_reindeer[0:4]
    list_reindeer_wait = list_reindeer[4:]

    list_reindeer_next = []
    for i in list_reindeer_act:
        list_reindeer_next += reindeer3(i[0],i[1],i[2],i[3])

    for i in range(0,len(list_reindeer_next)):
        pr = list_reindeer_next[i][0]
        pe = pos_end
        dist_to_end = int(math.sqrt((pr[0]-pe[0])**2+(pr[1]-pe[1])**2))
        list_reindeer_next[i].append(dist_to_end)

    list_reindeer = list_reindeer_next + list_reindeer_wait
    #save_map_gen(map_maze,"map_maze.txt")
    #map_maze = table_minus_one(map_maze)












### PArt 2 -------------------------------------

map_traces = copy.deepcopy(input_day_16)
for trace in memory_reindeer[1]:
    for pos in trace:
        print(pos)
        map_traces[pos[0]][pos[1]] = "o"
save_map_gen(map_traces,"map_live.txt")

count_in_table("o",["".join(i) for i in map_traces])

