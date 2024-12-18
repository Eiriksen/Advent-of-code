
### Part 1 Task specific functions -----------------------------

import re
import math
import time
import copy

def rotate_table(table,times=1):
    for i in range(0,times):
        table = list(zip(*table[::-1]))
    return(table)

def mirror_table(table):
    return([list(reversed(i)) for i in table])


def read_robots(file):
    px = re.findall("p=(.*),.*,",file)
    py = re.findall(",(.*) v",file)
    vx = re.findall("v=(.*),",file)
    vy = re.findall(",.*,(.*)\n",file)

    res = [[px[i],py[i],vx[i],vy[i]] for i in range(0,len(px))]
    res = [[int(i) for i in a]for a in res]
    return(res)

def get_pos(pos,vel):
    global map_width
    global map_height

    pos[0]+=vel[0]
    pos[1]+=vel[1]

    if pos[0] > map_width-1:
        pos[0] -= map_width
    if pos[0] < 0:
        pos[0] += map_width
    if pos[1] > map_height-1:
        pos[1] -= map_height
    if pos[1] < 0:
        pos[1] += map_height

    return(pos)

def draw_robots(suf=""):
    global robots
    global map_height 
    global map_width 
    botmap = [["." for a in range(0,map_height)] for i in range(0,map_width)]

    for robo in robots:
        print(robo)
        cur_symbol = botmap[robo[0]][robo[1]]
        if cur_symbol == ".":
            botmap[robo[0]][robo[1]] = 1
        else:
            botmap[robo[0]][robo[1]] += 1

    out = mirror_table(rotate_table(botmap,1))
    out = [list(map(str,i)) for i in out] 
    out = ["".join(i) for i in out]
    with open("robomaps/map_bots"+suf+".txt", 'w') as f:
        for line in out:
            f.write(f"{line}\n")
    
    #return(botmap)

def move_robots():
    global robots
    for i_robo in range(0,len(robots)):
        robo = robots[i_robo]
        pos_new = get_pos([robo[0],robo[1]],[robo[2],robo[3]])
        robots[i_robo][0] = pos_new[0]
        robots[i_robo][1] = pos_new[1]
        

def count_quadrants():
    global robots
    global map_height
    global map_width
    quadrants = [0,0,0,0]
    for robo in robots:
        if robo[0] >= math.ceil(map_width/2):
            x = 0 
        elif robo[0] < math.floor(map_width/2):
            x = 1
        else: 
            continue

        if robo[1] >= math.ceil(map_height/2):
            y = 0
        elif robo[1] < math.floor(map_height/2):
            y = 2
        else: 
            continue

        quadrants[y+x]+=1
    return(quadrants)



### Executing part 1 ----------------------------------------

input_day14 = open("Input day 14.txt","r").read()
robots = read_robots(input_day14)
map_width = 101
map_height = 103

for i in range(0,100):
    move_robots()

print(
    math.prod(count_quadrants())
)












### Part 2 functions ------------------------------------

#### Need an area counter
def get_relPos(pos,direction,speed):
    # return relative position
    radians = direction*math.pi/180
    delta_x = round(math.cos(radians)*speed)
    delta_y = round(math.sin(radians)*speed)
    return([pos[0]+delta_x,pos[1]+delta_y])

def out_of_bounds(p,table):
    if p[0] < 0 or p[1] < 0:
        return(True)
    elif p[0] > len(table)-1 or p[1] > len(table[p[0]])-1:
        return(True)
    else:
        return(False)

def get_symbol(pos,table):
  if out_of_bounds(pos, table):
    return(0)
  else:
    return(table[pos[0]][pos[1]])

# area counter robot (modified robot from the fence task)
def robot(pos):
    global countarea
    global countmap
    if not get_symbol(pos,countmap) in [".","Ø",0]:
        countmap[pos[0]][pos[1]] = "Ø"
        countarea += 1
    else:
        return(0)
    for i in [0,90,180,270]:
        pos_next = get_relPos(pos,i,1)
        symbol_next = get_symbol(pos_next,countmap)
        if symbol_next == "." or symbol_next == "Ø":
            symbol_next = 0
        if  int(symbol_next) > 0:
          robot(pos_next)

# launch area-robots at all areas
# track and report largest area
def find_largest_area():
    global map_height
    global map_width
    global countmap
    global countarea
    largest = 0
    for i_x in range(0,map_width-1):
        for i_y in range(0,map_width-1):
            countarea = 0
            robot([i_x,i_y])
            if countarea > largest:
                largest = countarea
    return(largest)

def draw_robots(suf=""):
    global robots
    global map_height 
    global map_width 
    global countmap

    # make a blank map
    botmap = [["." for a in range(0,map_height)] for i in range(0,map_width)]

    # fill the bots in on the map
    for robo in robots:
        cur_symbol = botmap[robo[0]][robo[1]]
        if cur_symbol == ".":
            botmap[robo[0]][robo[1]] = 1
        else:
            botmap[robo[0]][robo[1]] += 1
    
    # use another robot to check what the largest "painted" area on the map is
    countmap = copy.deepcopy(botmap)
    area = find_largest_area()

    # only print if area larger than 10
    if area > 10:
        out = mirror_table(rotate_table(botmap,1))
        out = [list(map(str,i)) for i in out] 
        out = ["".join(i) for i in out]
        with open("maps/"+str(area)+"_map_bots"+str(suf)+".txt", 'w') as f:
            for line in out:
                f.write(f"{line}\n")
        time.sleep(0.1)



# Executing part 2 -------------------------------------

input_day14 = open("Input day 14.txt","r").read()
robots = read_robots(input_day14)
countarea = 0
map_width = 101
map_height = 103
countmap = []


for i in range(1,10000):
    move_robots()
    draw_robots(i)

# SEE FOLDER "MAPS"
