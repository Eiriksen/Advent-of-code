### General functions -----------------


### Functions part 1 ------------------

def shave(design,towel):
    # for a given design and towel
    # tries to "shave off" the beginning of the design
    # with the given towel patterns
    # returns the resulting pattern, or "False" if not possible:
    # e.g. uugw,uu -> gw
    # e.g. uugw, g -> False
    if design == "": return design

    try:
        can_shave = (design.index(towel) == 0)
    except:
        can_shave = False

    if can_shave == True:
        return design[len(towel):]
    else:
        return False

def check_design(design, towels):
    # loops through every towel multiple times
    # each time any towel can shave off the design:
    #   save a new copy of that design, shaved off
    #   only operate on designs which were saved last round
    #   any design which did not find a matchin towel is thrown away
    #   that way, only designs which can be "shaved" with any one towel is kept
    possible_designs = [design]
    towels = [t for t in towels if t in design]

    while len(possible_designs) != 0:
        new = []
        for d in possible_designs:
            for t in towels:
                shaved = shave(d,t)
                if shaved == "":
                    return(True)
                if shaved != False and not shaved in new:
                    new.append(shaved)
        
        possible_designs = new

    return False



### Executer part 1 -------------------


towels = open("Input day 19.txt").read().splitlines()[0].split(", ")
designs = open("Input day 19.txt").read().splitlines()[2:]

print(
    sum(
        [check_design(d,towels) for d in designs]
    )
)








### Functions part 2 -------------------

def check_design2(design, towels):
    # same as previous, but keeps track of how many copies
    # possible_designs is now two-dimensional, with [1] keeping count
    possible_designs = [[design,1]]
    towels = [t for t in towels if t in design]
    count_sollutions = 0

    while len(possible_designs) != 0:
        new = []
        for d in possible_designs:
            for t in towels:
                shaved = shave(d[0],t)
                if shaved != False:
                    # if "", drop and increase count
                    if shaved == "":
                        count_sollutions +=d[1]
                    # if not already in list, append
                    elif not shaved in [i[0] for i in new]:
                        new.append([shaved,d[1]])
                    # if already in list, add count+1
                    else:
                        new[ [i[0] for i in new].index(shaved) ][1] += d[1]
        
        possible_designs = new

    return count_sollutions



### Execute part 2 -----------------

towels = open("Input day 19.txt").read().splitlines()[0].split(", ")
designs = open("Input day 19.txt").read().splitlines()[2:]

print(
    sum(
        [check_design2(d,towels) for d in designs]
    )
)

# 43156
# 743920 ( too low )
# 601201576113503 ( CORECT!)
