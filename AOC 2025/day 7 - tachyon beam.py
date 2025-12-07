# Day 7: We´re propagating a tachyon beam down through a range of splitters
# Task 1: How many of the splitters get used?
# Task 2: If each splitter duplicates each beam, how many beams do we end up with?


### Task 1 ------------------------------------------------------------------------------

input = open("AOC 2025/input day 7.txt","r").read().splitlines()
basemap = [ list(i) for i in input]

# Some basic map/table functions
def out_of_bounds(p,table):
    if p[0] < 0 or p[1] < 0:
        return(True)
    elif p[0] > len(table)-1 or p[1] > len(table[p[0]])-1:
        return(True)
    else:
        return(False)

def table_get_pos_of(what,table):
    for i in range(0,len(table)):
        if what in table[i]:
            return([i, table[i].index(what)])
    return [-1]

def save_map_gen(t,filename):
    m = [[list(map(str,i)) for i in a] for a in t]
    m = [[item for col in row for item in col] for row in m]
    m = ["".join(i) for i in m]
    with open(filename, 'w') as f:
        for line in m:
            f.write(f"{line}\n")

# This algorithm works of a list of active beams, giving the current position of each beam at this moment in time e.g. [[2,4],[2,5],[2,8] for three beams 
# for each step (iteration), we update the list with the next positions of the beams. (Actually we just make a new list with the new positions). This may involve creating new beams at splitters
# if a beam hits another beam, it stops and does not get propagated further
# if a beam hits out_of_bounds, it also stops
# finally, we count each time a beam hits a splitter and report that
  
# The initial beam:
libeams = [table_get_pos_of("S",basemap)]
libeams[0][0]+=1
count_splits = 0

# iterate over the beam positions until they reach the end (and the list of new positions thus becomes empty)
while len(libeams) != 0:
  libeams_n = []
  for beam in libeams:
    if not out_of_bounds(beam,basemap):
      sym_nexpos = basemap[beam[0]][beam[1]]
    else:
      sym_nexpos = "outofbounds"
    match sym_nexpos:
      case ".":
        libeams_n.append([beam[0]+1,beam[1]])
        basemap[beam[0]][beam[1]] = "|"
      case "^":
        count_splits+=1
        libeams_n.append([beam[0],beam[1]+1])
        libeams_n.append([beam[0],beam[1]-1])
  libeams = libeams_n

# RESULT:
print(count_splits)
# Save a map of the beams' paths
save_map_gen(basemap, "map - day 7.txt")
  


### TASK 2 ------------------------------------------------------------------------------
# Same as above, but we want to keep track of the total number of beams. Beams hitting each other do no longer cancel each other out. 
# To reduce the computing cost, we track the number of tachyons in a beam, not each tachyon individually, so the list of beams gets another index with that number, e.g. [[2,4,1],[2,5,2],[2,8,1] 
# After each iteration, in which new tachyons may have been created from splits, we merge the list of beams, adding together the number of tachyons in each beam
# Continue as above, and cound the number of tachyions in the end


input = open("AOC 2025/input day 7.txt","r").read().splitlines()
basemap = [ list(i) for i in input]

# The initial beam
libeams = table_get_pos_of("S",basemap)
libeams.append(1)
libeams[0]+=1
libeams = [libeams]

# subfunction for merging beams
def merge_beams_at(li,i):
  j = i+1
  while j < len(li):
    if li[i][0:2] == li[j][0:2]:
      li[i][2]+=li[j][2]
      li = [li[z] for z in range(0,len(li)) if z!= j]
      j = i+1
    else:
      j = j+1
  return(li)

def merge_all_beams(li):
  i = 0 
  while i < len(li):
    li = merge_beams_at(li,i)
    i+=1
  return(li)

# iterate over the list of beams until we hit the end
while len(libeams) != 0:
  libeams_n = []
  for beam in libeams:
    if not out_of_bounds(beam,basemap):
      sym_nexpos = basemap[beam[0]][beam[1]]
    else:
      sym_nexpos = "outofbounds"
    if sym_nexpos == "^":
      libeams_n.append([beam[0]+1,beam[1]+1,beam[2]])
      libeams_n.append([beam[0]+1,beam[1]-1,beam[2]])
    elif sym_nexpos != "outofbounds":
      libeams_n.append([beam[0]+1,beam[1],beam[2]])

  # if the list of new positions is empty, we have hit the.
  # report the total number of tachyons
  if len(libeams_n)==0:
    # RESULT:
    print(sum([b[2] for b in libeams]))

  libeams = merge_all_beams(libeams_n)

  
