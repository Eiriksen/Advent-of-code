

def issymbol(string):
    # code to identify if something is a symbol
    # return true or false
    return(string in list_symbols)

def in_symbol_square(row,index):
    # T/F if the given location is in the square of a symbol
    # check all symbols in the given row, plus those above and below
    if row != 0:
        above=True in (pos in range(index-1,index+1) for pos in loc_symbols[row-1])
    else:
        above=False

    same=True in (pos in range(index-1,index+1) for pos in loc_symbols[row])

    if row != (len(file)-1):
        below=True in (pos in range(index-1,index+1) for pos in loc_symbols[row+1])
    else:
        below=False
    
    if same | below | above:
        return(True)
    else:
        return(False)
    
def next_to_partnumber(row,index):
    # T/F if the given location is next to a part number
    nextto = True in (pos in range(index-1, index+1) for pos in loc_partnums[row])
    return(nextto)

def is_partnumber(row,index):
    # check if a given location is a partnumber

def is_number(row,index):
    return(str.isnumeric(file[row][index]))

def is_symbol(row,index):
    return(issymbol(file[row][index]))

def remove_notpartnumber(file,loc_partnumber):
    # go through every single index,
    # if it is a number, check if it is a partnumber

with open("Day 3 input.txt") as fil:
    file=fil.readlines()

loc_symbols = [ [] for i in range(len(file))]
loc_partnums = [ [] for i in range(len(file))]
list_symbols = "!@#$%^&*()-+?_=,<>"


# find the location of all symbols
# store them to variable loc_symb (??? how)
# maybe a n dimension variable, where each n is a vector where each number represents the index of a symbol
for i_row in range(len(file)):r
    for i_index in range(0,len(row)-1):
        if is_symbol(i_row,i_index):
            loc_symbols[i_row].append(i_index)

# then, go through all numbers
# for each number, check if it exists within the square of a symbol
# if it does, record that number as a part-number
for i_row in range(len(file)):
    for i_index in range(0,len(row)-1):
        if is_number(i_row,i_index) and in_symbol_square(i_row, i_index):
            loc_partnums[i_row].append(i_index)


# again, go trough numbers
# for each number, check if it is adjacent to a partnumber
# ...if it is, make it a part number
for i_row in range(len(file)):
    for i_index in range(0,len(row)-1):
        if is_number(i_row,i_index) and not is_partnumber(i_row,i_index) and next_to_partnumber(i_row,i_index):
            loc_partnums[i_row].append(i_index)

# next, again check all symbols, any symbold next to a part-number is also a part number, add it
# do this up to 5 times to make sure we get all part numbers

# finally, remove all numbers that are not partnumbers from the original file