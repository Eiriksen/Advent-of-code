import time
import copy

# Day 4: We have a table map of a warehouse
# the warehouse countains rolls of paper "@"
# a roll of paper can be moved out if no more than three rolls of paper surrounds it
# Task 1: Count number of rolls which can be moved out
# Task 2: Count total number of rolls which can be moved out 



### 1: Loap map and generic map functions: --------------------------------------

input = open("AOC 2025/input day 4.txt","r").read().splitlines()
map_base = [ [a for a in i] for i in input]

def out_of_bounds(p,table):
  if p[0] < 0 or p[1] < 0:
      return(True)
  elif p[0] > len(table)-1 or p[1] > len(table[p[0]])-1:
      return(True)
  else:
      return(False)

def get_pos_surround(x,y):
  list_pos = [[x-1,y-1],[x,y-1],[x+1,y-1],[x-1,y],[x+1,y],[x-1,y+1],[x,y+1],[x+1,y+1]]
  return(list_pos)

def pos_remove_outofbounds(list_pos, table):
  return([pos for pos in list_pos if not out_of_bounds(pos,table)])

def pos_get_values(list_pos,table):
  return([table[pos[0]][pos[1]] for pos in list_pos])

def count_x_aroundpos(pos,table,symbol):
  lipo = get_pos_surround(pos[0],pos[1])
  lipo = pos_remove_outofbounds(lipo,table)
  liva = pos_get_values(lipo,table)
  nsymbol = liva.count(symbol)
  return(nsymbol)

def table_get_all_pos(table):
  list_pos = []
  for row in range(0,len(table)):
    for col in range(0,len(table[0])):
      list_pos.append([row,col])
  return(list_pos)




### 2: Task 1 ----------------------------------------------------------
# count number of rolls accessible by forklift
# i.e. count number of @ with no more than 3 @ around them

n_liftable = 0

for p in table_get_all_pos(map_base):
  val = map_base[p[0]][p[1]]
  if val != "@":
    continue
  if count_x_aroundpos(p,map_base,"@") < 4:
    n_liftable = n_liftable + 1

print(n_liftable)



### 3: Task 2 -------------------------------------------------------------
# count TOTAL number of rolls removable by forklift

def paint_locations(locations,table,symbol):
    for pos in locations:
        if not out_of_bounds(pos,table):
            table[pos[0]][pos[1]] = symbol
    return(table)

def get_pos_liftable(table):
  list_liftable = []
  for p in table_get_all_pos(table):
    val = table[p[0]][p[1]]
    if val != "@":
      continue
    if count_x_aroundpos(p,table,"@") < 4:
      list_liftable.append(p)
  return(list_liftable)

def save_map_gen(t,filename):
    m = [[list(map(str,i)) for i in a] for a in t]
    m = [[item for col in row for item in col] for row in m]
    m = ["".join(i) for i in m]
    with open(filename, 'w') as f:
        for line in m:
            f.write(f"{line}\n")

list_pos_liftable = get_pos_liftable(map_base)
map_work = copy.deepcopy(map_base)
n_lifted = 0
counter = 0

while(len(list_pos_liftable) != 0):
  counter += 1
  map_work = paint_locations(list_pos_liftable,map_work,".")
  n_lifted += len(list_pos_liftable)
  list_pos_liftable = get_pos_liftable(map_work)
  save_map_gen(map_work,"map-day4-paperrols.txt")
  time.sleep(0.1)
  if (counter > 100):
    print("broke")
    break

print(n_lifted)
