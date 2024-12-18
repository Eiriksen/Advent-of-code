## Generalf functions -------------------

import math
import time
import re
import copy

def out_of_bounds(p,table):
    if p[0] < 0 or p[1] < 0:
        return(True)
    elif p[0] > len(table)-1 or p[1] > len(table[p[0]])-1:
        return(True)
    else:
        return(False)

def count_in_table(regexp,tab):
    n = 0
    for row in tab:
        n = n + len(re.findall(regexp,row))
    return(n)

def does_list_contain(l,symbol):
    try:
        l.index(symbol)
        return(True)
    except:
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
        








# Part 1 functions ------------------------------------

def guard():
    global direction_guard
    global guardpos
    # for each interval ,
    # Behvaiours of the guard
    nexpos = get_relPos(guardpos,direction_guard,1)
    
    if out_of_bounds(nexpos,map_base):
        return(0)
    
    symbol_nexpos = map_base[nexpos[0]][nexpos[1]]

    if symbol_nexpos == "#":
        direction_guard = direction_guard - 90
        return(1)
    else:
        map_base[guardpos[0]][guardpos[1]] = "X"
        guardpos = nexpos
        map_base[guardpos[0]][guardpos[1]] = "^"

def save_map():
    m = ["".join(i) for i in map_base]
    with open("map.txt", 'w') as f:
        for line in m:
            f.write(f"{line}\n")

def save_map_gen(t,filename):
    m = ["".join(i) for i in t]
    with open(filename, 'w') as f:
        for line in m:
            f.write(f"{line}\n")


### Executing part 1 ------------------------------

map_base = open("Input day 6.txt","r").read().splitlines()
map_base = [ list(i) for i in map_base]
guardpos = get_pos_of("^",map_base)
direction_guard = 180

for i in range(0,10000000000):
    if guard()==0:
        break

n_x = count_in_table("X",[ "".join(i) for i in map_base])
print(n_x)











### Part 2 functions 

def out_of_bounds(p,table):
    if p[0] < 0 or p[1] < 0:
        return(True)
    elif p[0] > len(table)-1 or p[1] > len(table[p[0]])-1:
        return(True)
    else:
        return(False)

j=1
def save_map_drone():
    global j
    m = [[ i[0] for i in a] for a in map_drone]
    out = ["".join(i) for i in m]
    with open("dronemaps/map_drone"+str(j)+".txt", 'w') as f:
        for line in out:
            f.write(f"{line}\n")
    j+=1

def launch_drone(pos,direction):
    global pos_drone
    global direction_drone
    global map_drone
    global map_obstacles
    global memory_drone

    map_drone = copy.deepcopy(map_base)
    pos_drone = pos
    memory_drone = []
    direction_drone = direction
    
    # get the posiiton in front of the drone
    nexpos = get_relPos(pos_drone,direction_drone,1)
    if (out_of_bounds(nexpos,map_base)):
        return(0)

    # place obstacle there
    map_drone[nexpos[0]][nexpos[1]] = "#"

    drone_status = 1
    iterations = 0
    while drone_status == 1 and iterations < 10000000:
        drone_status = drone()
        iterations+=1

    if drone_status == 2:
        map_obstacles[nexpos[0]][nexpos[1]] = "$"

def drone():
    global direction_drone
    global map_drone
    global pos_drone
    global memory_drone
    nexpos = get_relPos(pos_drone,direction_drone,1)
    
    if out_of_bounds(nexpos, map_base):
        return(0)

    symbol_nexpos = map_drone[nexpos[0]][nexpos[1]]
    
    #2.1 Are we hitting an object?
    if symbol_nexpos == "#":
        # Yes! 
        ID_obstacle = pos_drone + nexpos
        # have we hit this object before?
        if ID_obstacle in memory_drone:
            # yes, is this the original one?
            if ID_obstacle == memory_drone[0]:
                # Yes! We're in a loop!
                return(2)
            else:
                # No! We're in a false loop!
                # but for now, lets count that as a loop also
                return(2)
        else:
            # No! -not hit before
            # add to memory
            memory_drone.append(ID_obstacle)

        # Avoid collison, change direction by -90 degrees
        direction_drone = direction_drone - 90
        if direction_drone == -90:
            direction_drone = 270
        # exit, move to next cycle
        return(1)
    #2.2 not hitting an object
    else:
        # move drone
        map_drone[pos_drone[0]][pos_drone[1]]="*"
        pos_drone = nexpos
        # exit, move to next cycle
        return(1)

def guard_drone():
    global direction_guard
    global guardpos
    # for each interval ,
    # Behvaiours of the guard
    nexpos = get_relPos(guardpos,direction_guard,1)
    if out_of_bounds(nexpos,map_base):
        return(0)
    
    symbol_nexpos = map_base[nexpos[0]][nexpos[1]]

    if symbol_nexpos == "#":
        direction_guard = direction_guard - 90
        if direction_guard == -90:
            direction_guard = 270
        return(1)
    else:
        # before moving, launch the drone,
        # BUT ONLY IF YOU HAVE NOT WALKED THERE ALREADY
        if symbol_nexpos != "X":
            launch_drone(guardpos,direction_guard)
        map_base[guardpos[0]][guardpos[1]] = "X"
        guardpos = nexpos
        map_base[guardpos[0]][guardpos[1]] = "^"



# Executing part 2 ---------------------------------

map_base = open("Input day 6.txt","r").read().splitlines()
map_base = [ list(i) for i in map_base]
map_obstacles = copy.deepcopy(map_base)
map_drone = copy.deepcopy(map_base)

guardpos = get_pos_of("^",map_base)
direction_guard = 180

memory_drone = []
pos_drone = [0,0]
direction_drone = 0

for i in range(0,1000000):
    if guard_drone()==0:
        break

save_map_gen(map_obstacles,"map_obs.txt")

n_x = count_in_table("\$",[ "".join(i) for i in map_obstacles])
print(n_x)

# 1705 if including false loops CORRECT!!!
# 1522 (after excluding pre-walked locations)
# 1597
# 1616  

