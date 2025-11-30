
import re

def loc_in_symbol_square(row,index):
    # T/F if the given location is in the square of a symbol
    # check all symbols in the given row, plus those above and below
    if row != 0:
        above=True in (pos in range(index-1,index+2) for pos in loc_symbols[row-1])
    else:
        above=False

    same=True in (pos in range(index-1,index+2) for pos in loc_symbols[row])

    if row != (len(file)-1):
        below=True in (pos in range(index-1,index+2) for pos in loc_symbols[row+1])
    else:
        below=False
    
    if same | below | above:
        return(True)
    else:
        return(False)
    
def loc_next_to_partnumber(row,index):
    # T/F if the given location is next to a part number
    nextto = True in (pos in range(index-1, index+2) for pos in loc_partnums[row])
    return(nextto)

def loc_is_partnumber(row,index):
    # check if a given location is a partnumber
    if index in loc_partnums[row]:
        return(True)
    else:
        return(False)

def loc_is_gear(row,index):
    # check if a given location is a partnumber
    if index in loc_gears[row]:
        return(True)
    else:
        return(False)

def loc_is_symbol(row,index):
    return(str_is_symbol(file[row][index]))


### From: https://stackoverflow.com/questions/41752946/replacing-a-character-from-a-certain-index
def replacer(s, newstring, index, nofail=False):
    # raise an error if index is outside of the string
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")
    # if not erroring, but the index is still not in the correct range..
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring
    # insert the new string between "slices" of the original
    return s[:index] + newstring + s[index + 1:]

def str_is_symbol(string):
    # code to identify if something is a symbol
    # return true or false
    list_symbols = "!@#$%^&*()-+?_=,<>/"
    return(string in list_symbols)

def loc_is_number(row,index):
    return(str.isnumeric(file[row][index]))

def str_is_number(string):
    return(str.isnumeric(string))

def str_numbers_extract(string):
    res = re.findall(r'\d+', string)
    res=list(map(int, res))
    return(res)

def file_read_lines(filename):
    with open(filename) as fil:
        file=fil.readlines()
    return(file)

def file_save_lines(x,filename):
    with open(filename, 'w') as f:
        for line in x:
            f.write(f"{line}\n")


# START SCRIPT ----------------------------------------------------------

with open("Day 3 input.txt") as fil:
    file=fil.readlines()

for i_row in range(0,len(file)):
    file[i_row] = file[i_row][0:140]

loc_symbols = [ [] for i in range(len(file))]
loc_partnums = [ [] for i in range(len(file))]
loc_gears = [ [] for i in range(len(file))]

# find the location of all symbols
# store them to variable loc_symb (??? how)
# maybe a n dimension variable, where each n is a vector where each number represents the index of a symbol
for i_row in range(0,len(file)):
    row = file[i_row]
    for i_index in range(0,len(row)-1):
        if loc_is_symbol(i_row,i_index):
            loc_symbols[i_row].append(i_index)

# then, go through all numbers
# for each number, check if it exists within the square of a symbol
# if it does, record that number as a part-number
for i_row in range(0,len(file)):
    for i_index in range(0,len(row)-1):
        if loc_is_number(i_row,i_index) and loc_in_symbol_square(i_row, i_index):
            loc_partnums[i_row].append(i_index)

# again, go trough numbers
# for each number, check if it is adjacent to a partnumber
# ...if it is, make it a part number
for a in range(1,10):
    for i_row in range(0,len(file)):
        for i_index in range(0,len(row)):
            if loc_is_number(i_row,i_index) and not loc_is_partnumber(i_row,i_index) and loc_next_to_partnumber(i_row,i_index):
                loc_partnums[i_row].append(i_index)

# finally, remove all numbers that are not partnumbers from the original file
file_edited = file
for i_row in range(len(file_edited)):
    for i_index in range(0,len(row)):
        if loc_is_number(i_row,i_index) and not loc_is_partnumber(i_row, i_index):
            file_edited[i_row] = replacer(file_edited[i_row], "ø", i_index)

# Save as a separate file for inspection
file_save_lines(file_edited, "Day 3 input changes.txt")

# Get the sum of all partnumbers
all_partnums=[]
for row in file_edited:
    all_partnums.append(sum(str_numbers_extract(row)))
sum(all_partnums)


# CODE 2 -------------------------------------------------

def str_index_of_matches(string,regexp):
    # gives indexes of all matches of regexp in string
    a = re.finditer(regexp, string)
    b = [m.start(0) for m in a]
    return(b)

def str_index_of_last(string,regexp):
    # gives index of last match of regexp
    b = str_index_of_matches(string,regexp)
    if len(b)==0:
        return(None)
    return(b[-1])

def str_index_of_first(string,regexp):
    # gives index of first match of regexp
    b = str_index_of_matches(string,regexp)
    if len(b)==0:
        return(None)
    return(b[0])

def str_check_whole_number(string,index):
   # returns the whole number found at an index in a loc (to fix:should be string), as well as the first and last index of said number
    # 1 check if there is a number there
    if not str_is_number(string[index]):
        return([False,[False,False]])
   
    # if there is, find the index range which contains numbers from there 
    index_max = len(string)

    str_upper = string[index:index_max]
    if (str_index_of_first(str_upper,r"\D")==None):
        index_upper=index_max
    else:
        index_upper = index + str_index_of_first(str_upper,r"\D")
    
    str_lower = string[0:index]
    if (str_index_of_last(str_lower,r"\D")==None):
        index_lower=0
    else:
        index_lower = index-(len(str_lower)-str_index_of_last(str_lower,r"\D")-1)

    number = int(string[index_lower:index_upper])
    return([number,[index_lower,index_upper]])

def loc_check_number(row,index):
    return(str_check_whole_number(file[row],index))

def loc_range_whole_numbers(row, index_upper, index_lower):
    # return all unique whole numbers in a range, as well as their positions
    li = []
    for i in range(index_upper,index_lower+1):
        number = loc_check_number(row,i)
        if not number[0]== False and not number in li:
            li.append(number)
    return(li)

def loc_area_whole_numbers(row_u,row_l,index_l,index_u):
    res = []
    for row in range(row_u,row_l+1):
        nums = loc_range_whole_numbers(row,index_l,index_u)
        if len(nums) != 0:
            res = res+nums
    return(res)#

def loc_around_whole_numbers(row,index):
    nums = []
    allnums = loc_area_whole_numbers(row-1,row+1,index-1,index+1)
    for num in allnums:
        nums.append(num[0])
    return(nums)


# find all gear numbers in file and add them together
gearnums=[]
for i_row in range(0,len(file)):
    row = file[i_row]
    for i_index in range(0,len(row)-1):
        if file[i_row][i_index] == "*":
            print(str(i_row)+" - "+str(i_index))
            numarounds = loc_around_whole_numbers(i_row,i_index)
            if len(numarounds) == 2:
                loc_gears[i_row].append(i_index)
                gearnum = numarounds[0]*numarounds[1]
                gearnums.append(gearnum)


# finally, remove all * that are not gears from the original file
file_edited_2 = file
for i_row in range(len(file_edited_2)):
    for i_index in range(0,len(row)):
        if file[i_row][i_index] == "*" and not loc_is_gear(i_row, i_index):
            file_edited_2[i_row] = replacer(file_edited_2[i_row], "ø", i_index)

# Save as a separate file for inspection
file_save_lines(file_edited_2, "Day 3 input changes v2.txt")

# get sum of gearn numbers
gearnums
sum(gearnums)