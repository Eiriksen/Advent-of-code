
### generic functions

import math
import re
import time

def count_in_table(regexp,tab):
    n = 0
    for row in tab:
        n = n + len(re.findall(regexp,row))
    return(n)

def out_of_bounds(p,table):
    if p[0] < 0 or p[1] < 0:
        return(True)
    elif p[0] > len(table)-1 or p[1] > len(table[p[0]])-1:
        return(True)
    else:
        return(False)

def save_map_gen(t,filename):
    m = ["".join(i) for i in t]
    with open(filename, 'w') as f:
        for line in m:
            f.write(f"{line}\n")

def table_join_rows(table):
    new_table = []
    for row in table:
        new_table.append( "".join(row) )
    return(new_table)

# function that finds all indexes of vlaue in list
def get_index_of_all(l,value):
    return([i for i,val in enumerate(l) if val==value])

# function that finds all locations of a symbol in a table
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

# paints locations in a table
def paint_locations(locations,table,symbol):
    for pos in locations:
        if not out_of_bounds(pos,table):
            table[pos[0]][pos[1]] = symbol
    return(table)











### Part 1 task specific functions ----------------------

# function that finds antilocations between two locations
def get_antilocations(pos1,pos2):
    distance = [pos2[0]-pos1[0],pos2[1]-pos1[1]]
    antilocation1 = [pos1[0] - distance[0], pos1[1] - distance[1]]
    antilocation2 = [pos2[0] + distance[0], pos2[1] + distance[1]]
    return([antilocation1,antilocation2])

# function that finds the antilocations of one tower:
def get_tower_antilocations(pos,m):
    symbol = m[pos[0]][pos[1]]
    list_positions = get_pos_of_all(symbol,m)
    # assumes the first in the list is the tower in question
    # since we will delete this tower afterwards
    # it will not cause problems down the line
    list_antipositions = []
    for pos2 in list_positions[1:]:
        antipositions = get_antilocations(pos,pos2)
        list_antipositions = list_antipositions + antipositions
    return(list_antipositions)

def handle_location(pos):
    global map_towers
    global map_anti

    symbol = map_towers[pos[0]][pos[1]]
    if symbol == ".":
        return(0)

    list_antilocations = get_tower_antilocations(pos,map_towers)
    map_anti = paint_locations(list_antilocations,map_anti,"#")
    map_towers[pos[0]][pos[1]] = "+"

    #time.sleep(0.1)
    #save_map_gen(map_towers,"map_towers.txt")



# Executing part 1 ------------------------------

input_day_8 = open("Input day 8.txt","r").read().splitlines()
map_towers = [ list(i) for i in input_day_8]
map_anti = [ list(i) for i in input_day_8]

for i_row in range(0,len(map_towers)):
    for i_column in range(0,len(map_towers[i_row])):
        handle_location([i_row,i_column])

save_map_gen(map_towers,"map_towers.txt")
save_map_gen(map_anti,"map_anti.txt")

print(count_in_table("#",table_join_rows(map_anti)))











# Functions part 2 ---------------------------------

def get_antilocations(pos1,pos2,m=map_towers):
    distance = [pos2[0]-pos1[0],pos2[1]-pos1[1]]
    # largest common denominator
    lcd = math.gcd(distance[0],distance[1])
    distance_s = [int(distance[0]/lcd), int(distance[1]/lcd)]
    antilocations = []

    # iterate in the negative direction until end of map
    i = 1
    while i != 0 and i < 10000:
        antilocation = [pos1[0] + distance_s[0]*i, pos1[1] + distance_s[1]*i]
        if not out_of_bounds(antilocation,m):
            antilocations = antilocations + [antilocation]
            i+=1
        else:
            i = 0
    # iterate in the negative direction until end of map
    i = 1
    while i != 0 and i < 10000:
        antilocation = [pos2[0] - distance_s[0]*i, pos2[1] - distance_s[1]*i]
        if not out_of_bounds(antilocation,m):
            antilocations = antilocations + [antilocation]
            i+=1
        else:
            i = 0
    return(antilocations)



# Executing part 2 ------------------------------------------

input_day_8 = open("Input day 8.txt","r").read().splitlines()
map_towers = [ list(i) for i in input_day_8]
map_anti = [ list(i) for i in input_day_8]

for i_row in range(0, len(map_towers)):
    for i_column in range(0,len(map_towers[i_row])):
        handle_location([i_row,i_column])


save_map_gen(map_towers,"map_towers.txt")
save_map_gen(map_anti,"map_anti.txt")

print(count_in_table("#",table_join_rows(map_anti)))
