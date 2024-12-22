
### Generic functins -----------------------------

import copy
import math
import time

def rotate_table(table,times=1):
    for i in range(0,times):
        table = list(zip(*table[::-1]))
    return(table)

def mirror_table(table):
    return([list(reversed(i)) for i in table])

def save_map_gen(t,filename):
    m = mirror_table(rotate_table(t))
    m = [list(map(str,i))for i in m]
    m = [[item for col in row for item in col] for row in m]
    m = ["".join(i) for i in m]
    with open(filename, 'w') as f:
        for line in m:
            f.write(f"{line}\n")

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

def out_of_bounds(p,table):
    if p[0] < 0 or p[1] < 0:
        return(True)
    elif p[0] > len(table)-1 or p[1] > len(table[p[0]])-1:
        return(True)
    else:
        return(False)

def table_minus_one(table):
    for i_x in range(0,len(table)):
        for i_y in range(0,len(table[0])):
            j = table[i_x][i_y]
            if isinstance(j, int) and j > 0:
                table[i_x][i_y] -=1
    return(table)










### Part 1 specific functions --------------------

def walk(pos, direction, steps, dist_to_end, map_main,width,height):
    # make list of new children
    list_next = []

    # go through each of the four directions
    for i in [direction, direction+90, direction-90]:
            # get next position and symbol in this direction
            pos_next = get_relPos(pos,i,1)
            sym_nexpos = get_symbol(pos_next,map_main)
            # check that symbol is not "X", "None, or "#", and lower than current dist
            if not sym_nexpos in ["X","#",None]:
                if not isinstance(sym_nexpos, int) or sym_nexpos > steps+1:
                    # legal next step! Spawn a new walker there
                    # i_parent becomes i_self, and i_self becomes None
                    dist_to_end = (width - pos_next[0]) + (height - pos_next[1]) -2
                    list_next.append([pos_next, i, steps+1, dist_to_end])
    return(list_next)

def get_insertionindex(lis, value, column):
    for i in range(0,len(lis)):
        val_i = lis[i][column]
        if value < val_i:
            return(i)
    return(len(lis))


def walk_map(map_main, start):
    width = len(map_main)-1
    height = len(map_main[0])-1
    map_main[width][height] = width*height+20

    # 0 pos - 1 direction - 2 steps - 4 distance to end 
    list_walkers = [[start,0,0,0]]
    j = 0
    while j < 10000:
        j+=1
        list_walkers_act  = list_walkers[0:20] #REDEFINE
        list_walkers_wait = list_walkers[20:] #REDEFINE
        list_walkers_next = []

        # iterating through walkers_act
        for i in list_walkers_act:
            new_walkers = walk(i[0],i[1],i[2],i[3],map_main,width,height)
            list_walkers_next += new_walkers
            for q in new_walkers:
                map_main[q[0][0]][q[0][1]] = q[2]

        # place next walkers into list 
        for i in range(0,len(list_walkers_next)):
            dist_to_end = list_walkers_next[i][3]
            insertionindex = get_insertionindex(list_walkers_wait,dist_to_end,3)
            list_walkers_wait.insert(insertionindex, list_walkers_next[i])

        # join together
        list_walkers = copy.deepcopy(list_walkers_wait)
    return(map_main)



### Execute Part 1 -------------------------------

input_day_18 = open("Input day 18.txt").read().splitlines()
list_fallingbytes = [list(map(int, i.split(","))) for i in input_day_18]

width = 70
height = 70
map_main = [[ "." for i in range (0,width+1)] for a in range(0,height+1)]

# simulate falls
for fallbyte in list_fallingbytes[:1024]:
    map_main[fallbyte[0]][fallbyte[1]] = "#"

g = walk_map(map_main,[0,0])

print(g[70][70])








### Execute part 2 -------------------------------

map_main_base = [[ "." for i in range (0,width+1)] for a in range(0,height+1)]
upper = len(list_fallingbytes)
lower = 1024
while upper > lower+1:
    mid = round(lower + (upper-lower)/2)

    map_main_i = copy.deepcopy(map_main_base)
    for fallbyte in list_fallingbytes[:mid]:
        map_main_i[fallbyte[0]][fallbyte[1]] = "#" 
    steps = walk_map(map_main_i, [0,0])[70][70]

    if steps == 4920:
        # is closed, go down
        upper = mid
    else:
        # is open, go up
        lower = mid

    if upper == lower+1 or upper==lower:
        print("Route closed at i = ", upper, "falling at position", list_fallingbytes[upper-1])
        break



def Point():
    def __init__(self, xx, yy):
        self.x = xx
        self.y = yy
    def __add__(self, other):
        n = Point(self.x + other.x, self.y + other.y)
        return n

a = Point(1, 1)
b = Point(2, 2)
c = a + b
print(c.x, c.y)