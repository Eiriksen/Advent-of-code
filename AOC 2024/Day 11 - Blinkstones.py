### Part 1 functions ------------------------------------------

def blink_stone(stone):
  if stone == 0:
    #If the stone is engraved with the number 0, 
    # -it is replaced by a stone engraved with the number 1.
    return([1])
  if len(str(stone)) % 2 == 0:
    #If the stone is engraved with a number that has an even number of digits,
    # - it is replaced by two stones. 
    # -The left half of the digits are engraved on the new left stone, 
    # -and the right half of the digits are engraved on the new right stone. 
    # -(The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
    stone = str(stone)
    middle = int(len(stone)/2)
    first = int(stone[:middle].lstrip("0"))
    second = stone[middle:].lstrip("0")
    if second == "":
      second = 0
    else:
      second = int(second)
    return([first,second])
  else:
    # If none of the other rules apply, 
    # - the stone is replaced by a new stone;
      # - the old stone's number multiplied by 2024 is engraved on the new stone.
    return([stone*2024])

def blink(stones):
  blinkstones = []
  for stone in stones:
    blinkstones+=blink_stone(stone)
  return(blinkstones)




### Executing PART 1

input_day_11 = open("Input day 11.txt", "r").readlines()[0].split()
stones = [int(i) for i in input_day_11]

for i in range(25):
  stones = blink(stones)

len(stones)











### PART 2

## uses two lists, 
## one with the stones ("stones")
## and another telling how many there is of each stone ("n_stone") (per index)
## function "compress_stones" merges stones of the same number and updates the n_stones index

def blink2():
  global stones
  global stones_n
  # does the same thing as blink, 
  # but updates stones_n to maintain the correct number
  # e.g. if we had 2 x 2024, we now have 2 x 20 and 2 x 24
  new_stones = []
  new_stones_n = []
  for i_stone in range(0,len(stones)):
    # blink the stone
    stone_ori = stones[i_stone]
    stone_blinked = blink_stone(stone_ori)
    # check how many we had of it
    n = stones_n[i_stone]
    # add the resulting stones, and the count (which is the same as before)
    # - the two indexes
    new_stones += stone_blinked
    new_stones_n += [n]*len(stone_blinked)
  
  # update the global variables
  stones = new_stones
  stones_n = new_stones_n

def compress_stones():
  global stones
  global stones_n
  unique = list(set(stones))
  # for each unique stone type
  for stone_type in unique:
    # get indicies of this stone
    indices = [i for i, x in enumerate(stones) if x == stone_type]
    # count number
    n = 0
    for index in indices:
      n += stones_n[index]
    # remove all (based on indices)
    stones = [i for j, i in enumerate(stones) if j not in indices]
    stones_n = [i for j, i in enumerate(stones_n) if j not in indices]
    # add back
    stones.append(stone_type)
    stones_n.append(n)



# Executing part 2 -------------------------------------

input_day_11 = open("Input day 11.txt", "r").readlines()[0].split()
stones = [int(i) for i in input_day_11]
stones_n = [1 for i in stones]

for i in range(0,75):
  print(i)
  blink2()
  compress_stones()

sum(stones_n)










### Functions: part 2 but even faster ---------------------------

def blink3():
  global stones
  global stones_n
  # same as blink2, 
  # but maintains the stones_n index and "compression" as it goes
  # i.e. does not need the compress_stones() function
  
  # to not double-blink any stones, 
  # -we add any blinked stones and their count to this list
  new_stones = []
  new_stones_n = []

  # for each stone
  for i_stone in range(0,len(stones)):
    # blink the stone
    stone_ori = stones[i_stone]
    stone_blinked = blink_stone(stone_ori)
    # check how many we had of it originally
    n_ori = stones_n[i_stone]
    # iterate over each unique new stone after blinking
    # for each new type of stone
    for i in list(set(stone_blinked)):
      # if we already have it: just update the count
      if i in new_stones:
        index = new_stones.index(i)
        new_stones_n[index] += n_ori*stone_blinked.count(i)
      # if it is new: add it to both the stones list and the count
      else:
        new_stones += [i]
        new_stones_n += [n_ori*stone_blinked.count(i)]
  
  # update the global variables
  stones = new_stones
  stones_n = new_stones_n



# Executing part 2 but even faster ------------------------------

input_day_11 = open("Input day 11.txt", "r").readlines()[0].split()
stones = [int(i) for i in input_day_11]
stones_n = [1 for i in stones]

for i in range(0,70):
  blink3()

sum(stones_n)
