import re
import math

def get_n2(n1,d1,d2,z):
  return((n1*d1-z)/-d2)

def smallest_price(X,Y,dx1,dx2,dy1,dy2):
  # 1: N1, 2: N2, 3:Y valid? 4: Price
  l = [[i,None,None,None] for i in range(1,100)]

  for i_l in range(0,len(l)):
    n1 = l[i_l][0]
    n2 = get_n2(n1,dx1,dx2,X)
    if n2 % 1 != 0:
      n2 = None
      continue
    l[i_l][1] = n2
    if n1*dy1+n2*dy2 == Y:
      l[i_l][2] = True
    else:
      l[i_l][2] = False
      continue
    price = n1*3 + n2*1
    l[i_l][3] = price

  prices = [i[3] for i in l if i[3] != None]

  if len(prices) > 1:
    print(len(prices))

  if len(prices) != 0:
    return(min(prices))
  else: 
    return(False)


def read_machines(file):
  dx1 = re.findall("A: X\+(.*),", file)
  dx2 = re.findall("B: X\+(.*),", file)
  dy1 = re.findall("A:.*Y\+(.*)\n", file)
  dy2 = re.findall("B:.*Y\+(.*)\n", file)
  X   = re.findall("X=(.*),", file)
  Y   = re.findall("Y=(.*)\n", file)

  res = [[dx1[i],dx2[i],dy1[i],dy2[i],X[i],Y[i]] for i in range(0,len(dx1))]
  res = [[int(i) for i in a] for a in res]
  return(res)

def cost_machine(machines,i_machine):
  dx1 = machines[i_machine][0]
  dx2 = machines[i_machine][1]
  dy1 = machines[i_machine][2]
  dy2 = machines[i_machine][3]
  X = machines[i_machine][4]
  Y = machines[i_machine][5]
  return(smallest_price(X,Y,dx1,dx2,dy1,dy2))

input_day13 = open("Input day 13.txt","r").read()
machines = read_machines(input_day13)
sum([cost_machine(machines,i) for i in range(0,len(machines))])

### Part 2

def smallest_price(X,Y,dx1,dx2,dy1,dy2):
  X = X + 10000000000000
  Y = Y + 10000000000000
  # the two buttons (1 and 2) are vectors, 
  # 1 starts from  origo (#1: 0,0)
  # 2 starts from the prize (#2: X,Y)
  # slope of lines 1 and 2
  dydx1 = dy1/dx1
  dydx2 = dy2/dx2
  # intercepts of lines one and 2
  i1 = 0
  i2 = Y-X*dydx2

  # their intersect is where you need to stop pressing button 1
  # and start pressing button 2
  X_intersect = (i1-i2)/(dydx2-dydx1)
  if X_intersect < 0 or X_intersect > X:
    return(False)

  # number of times to press button 1:
  n1 = round(X_intersect / dx1)

  # since we ideally want to work with integers here
  # we need to round 1 down to the nearest one.
  # To ensure the rounding does not give us a faulty n1
  # - we also test n1+1 and n1-1


  for i in [n1-1,n1,n1+1]:
    # number of times to press button 2
    n2 = (n1*dx1-X)/-dx2
    if n2 % 1 == 0 and n1*dy1+n2*dy2 == Y:
      return(n1*3 + n2*1)

  return(False)

input_day13 = open("Input day 13.txt","r").read()
machines = read_machines(input_day13)
sum([cost_machine(machines,i) for i in range(0,len(machines))])
