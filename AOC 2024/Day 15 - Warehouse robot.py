
### Basic functions ---------------------------------------------

import math
import time

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

def out_of_bounds(p,table):
    if p[0] < 0 or p[1] < 0:
        return(True)
    elif p[0] > len(table)-1 or p[1] > len(table[p[0]])-1:
        return(True)
    else:
        return(False)

def get_symbol(pos,table):
  if out_of_bounds(pos, table):
    return(None)
  else:
    return(table[pos[0]][pos[1]])


def get_relPos(pos,direction,speed):
    # return relative position
    radians = direction*math.pi/180
    delta_x = round(math.cos(radians)*speed)
    delta_y = round(math.sin(radians)*speed)
    return([pos[0]+delta_x,pos[1]+delta_y])

def save_map_warehouse():
    global map_warehouse
    m = ["".join(i) for i in map_warehouse]
    with open("map_warehouse.txt", 'w') as f:
        for line in m:
            f.write(f"{line}\n")











### Part 1 Task specific functions ------------------------------

def mover(pos, direction):
    # attempts to move an object according to an instruction (^<>v)
    # returns "True" if the object moves
    # if the object has a possibly movable obstacle in the way, it calls a new mover on that object
    # - If that object moves, the new mover returns True, allowing the original to move
    # - i.e, if a chain of objects need to move, a chain of movers are called down it until-
    # - one object gets a definitive "Yes" or "No"

    global map_warehouse

    if isinstance(direction, str):
        direction = {"^":180, ">":90, "v":0, "<":270}[direction]
    symbol_obj = get_symbol(pos, map_warehouse)
    pos_next = get_relPos(pos, direction, 1)
    symbol_posnext = get_symbol(pos_next, map_warehouse)

    # stop if wall
    if symbol_posnext == "#":
        return(False)
    
    # if another object,
    # stop if the object does not obey a move command
    if symbol_posnext == "O":
        if mover(pos_next, direction) == False:
            return(False)

    # move:
    map_warehouse[pos_next[0]][pos_next[1]] = symbol_obj
    map_warehouse[pos[0]][pos[1]] = "."

    return(True)



### Executing  Part 1 ----------------------------------------------

input_day_15 = open("Input day 15.txt", "r").read().splitlines()
map_warehouse = [list(i) for i in input_day_15[:input_day_15.index("")] ]
str_commands = "".join(input_day_15[input_day_15.index("")+1:])

for command in str_commands:
    pos_robot = get_pos_of("@",map_warehouse)
    mover(pos_robot, command)
    #save_map_warehouse()
    #time.sleep(0.36)

sum_gps = 0
for y in range(0,len(map_warehouse)):
    for x in range(0, len(map_warehouse[0])):
        sym = map_warehouse[y][x]
        if sym == "O":
            sum_gps += 100 * y + x
print(sum_gps)










### Part 2 funtions -----------------------------------------

def mover(pos, direction, test=False, neighbor=False):
    # attempts to move an object according to an instruction (^<>v)
    # returns "True" if the object moves
    # if the object has a potentially movable obstacle in the way, it calls a new mover on that object
    # - If that object moves, the new mover returns True, allowing the original to move
    # - i.e, if a chain of objects need to move, a chain of movers are called down it until-
    # - one object gets a definitive "Yes" or "No"
    # if Test = True, the blocks don't move, only report if they can or not
    # the "neighbor" parameter tells the piece if the command to move came from its neighbor
    # - this keeps the piece from sending another move command back to the neighbor which gave it the original command

    global map_warehouse

    if isinstance(direction, str):
        direction = {"^":180, ">":90, "v":0, "<":270}[direction]
    symbol_obj = get_symbol(pos, map_warehouse)
    pos_next = get_relPos(pos, direction, 1)
    symbol_posnext = get_symbol(pos_next, map_warehouse)

    # stop if wall
    if symbol_posnext == "#":
        return(False)
    
    # if you are a "[" or a "]" only proceed if your neighbor is CAPABLE of moving
    # + ONLY CHECK THIS IF GOING UP OR DOWN
    # + only if "neighbor=False", if true, it means your neighbor was the one asking you to check this
    # + set "Test" to true, to issue a test without moving
    if direction in [0, 180] and neighbor==False and symbol_obj in ["[","]"]:
        pos_neighbor = {"[":1, "]":-1}[symbol_obj]
        if mover([pos[0],pos[1]+pos_neighbor], direction, neighbor=True, test=True) == False:
            return(False)    

    # Neighbor ready to move! (if exists)

    # if another object in front
    # stop if the object does not obey a move command
    # (or would if it could, if test=T)
    if symbol_posnext in ["[","]"]:
        if mover(pos_next, direction, test=test) == False:
            return(False)

    # We are also ready to move! 

    # Again, if we have a neighbor, give them the command to do the move
    # (we already know they can, since we checked above)
    if direction in [0, 180] and neighbor == False and test == False and symbol_obj in ["[","]"]:
        pos_neighbor = {"[":1, "]":-1}[symbol_obj]
        mover([pos[0],pos[1]+pos_neighbor], direction, neighbor=True, test=test)

    # make the move:
    if (test != True):
        map_warehouse[pos_next[0]][pos_next[1]] = symbol_obj
        map_warehouse[pos[0]][pos[1]] = "."
        #save_map_warehouse()
    return(True)



# Executing part 2 --------------------------------------------

input_day_15 = open("Input day 15.txt", "r").read().splitlines()
map_warehouse = [list(i) for i in input_day_15[:input_day_15.index("")]]
map_warehouse = [[list({"#":"##", ".":"..", "O":"[]", "@":"@."}[i]) for i in a] for a in map_warehouse]
map_warehouse = [[i for ii in row for i in ii] for row in map_warehouse]
str_commands = "".join(input_day_15[input_day_15.index("")+1:])

for command in str_commands[1:1000]:
    pos_robot = get_pos_of("@",map_warehouse)
    mover(pos_robot, command)
    #save_map_warehouse()
    #time.sleep(0.2)

sum_gps = 0
n=0
for y in range(0,len(map_warehouse)):
    for x in range(0, len(map_warehouse[0])):
        sym = map_warehouse[y][x]
        if sym == "[":
            n+=1
            sum_gps += 100 * y + x
print(sum_gps)

# possible errors:
# Error was that when asking the neighbor to move, the 
# neighbor might actually move! -before checking if the 
# original side itself could move.
# sollution was to do an initial "check" on the neighbor first,
# asking it if it COULD move without actually moving it
# ... this involved adding a "test" parameter to the move function
# which allowed it to do a full check on the move, but without performing 
# the moves in the end