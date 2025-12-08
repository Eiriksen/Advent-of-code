# Day 8: We are connecting many many "junction boxes" in a 3D room
# Task 1: Of all the possible connections among 1000 boxes, find the 10 shortes ones, connect those. Multiply the length of the three longest circuits (groups of connected boxes)
# Task 2: Keep adding connections (in order of short-to-long) until all the boxes are connected in one group. Multiply the two x coordinates of the last connection

### Set up some general functions -------------------------------------------------------

import math

def space_distance(p,q):
  return math.sqrt( (p[0]-q[0])**2 + (p[1]-q[1])**2 + (p[2]-q[2])**2 )

def does_intersect(a,b):
  # checks if two list contain any overlapping items
  # used to check if two lists of box are connected
  return not set(a).isdisjoint(b)

def unique(a):
  return list(set(a))

def merge_cons_at(i,li):
  # merging function for a list of connections e.g. [[1,2],[2,4],[3,5]]
  # checks the connection at i against all *following* connections, and merges those
  # [[1,2],[2,4],[3,5],[1,8]] at i=1 becomes [[1,2,3,8],[3,5]]
  # ideally, run on all i, starting at 0
  j=i+1
  while j < len(li):
    compare = li[j]
    if does_intersect(compare, li[i]):
      li[i] += compare
      li = [li[z] for z in range(0,len(li)) if z!= j]
      j = i+1
    else:
      j = j+1
  li[i] = unique(li[i])
  return li

def merge_cons_all(li):
  # merges all connections in a list 
  i = 0
  while i < len(li):
    li = merge_cons_at(i,li)
    i+=1
  return li

# Task 1 --------------------------------------------------------------------------------
# The general idea is to create a list of all possible connections, and their distance
# i.e. [[1,2,10],[1,3,40],[1,4,4.4] ... etc]
# (the first two items in a connection are box IDs as per their index in "input")
# Then sort by the distance, use the requested number of shortes connections, and merge those to find all connected groups given those connections
input = open("AOC 2025/input day 8.txt","r").read().splitlines()
input = [[int(j) for j in i.split(",")] for i in input]


# find all distances
list_distances = []
for q in range(0, len(input)):
  for p in range(q+1, len(input)):
    list_distances.append([q,p,space_distance(input[q],input[p])])

# sort by distance
list_distances.sort(key=lambda x: int(x[2]))
# add all indidivdual non-connected boxes to the list of connections
# here we are using the 1000 shortes connections, as requested
# NOTE NOTE NOTE: If using the test data, use the 10 shortest connections
list_boxes = [[i] for i in list(range(0,len(input)))]
list_cons = [i[0:2] for i in list_distances[:1000]]
# merge all connections
list_cons_merged = merge_cons_all(list_boxes + list_cons)
# RESULT: find the product of the 3 largest connected groups
math.prod(sorted([len(c) for c in list_cons_merged])[-3:])





# Task 2 --------------------------------------------------------------------------------
# Here, we just keep adding one connection (in the order of short-to-long) until merging them gives us one single group. Then we print out the requested multiplication of the x coordinates of the last connection made

# starting with a "bare" list of connections, i.e. only all the unconnected boxes
list_cons = [[i] for i in list(range(0,len(input)))]

# add 1 connection at a time:
for z in range(0,len(list_distances)):
  list_newconnection = [i[0:2] for i in list_distances[z:z+1]]
  list_cons = merge_cons_at(0, list_newconnection + list_cons)
  # check if we wneded up with just one group:
  if len(list_cons) == 1:
    merged = list_distances[z:z+1][0][0:2]
    # RESULT:
    print(input[merged[0]][0]*input[merged[1]][0])
    break
