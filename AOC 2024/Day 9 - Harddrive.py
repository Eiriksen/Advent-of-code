import re

# functions

def replace_at_index(string,index,new):
    return(string[:index] + [new] + string[index+1:])

def decompress(l):
    fulldata = []
    state = 0
    number = 0
    for i in l:
        if state == 0:
            fulldata+=[str(number)]*int(i)
            state=1
            number+=1
            continue
        if state == 1:
            fulldata+=["."]*int(i)
            state = 0
            continue
    return(fulldata)

def compact_one(string):
    # check if there is any empty space in there
    if not "." in string:
        return(string)

    # pick the last number
    last = string[-1]

    # if dot, just remove and return
    if last == ".":
        return(string[:-1])

    # find location of first dot in list:
    loc_firstdot = string.index(".")

    # replace that with the current number, and return list without that number
    return( replace_at_index(string[:-1],loc_firstdot,last))

def compact_string(string):
    i = 0 
    while "." in string and i < 1000000000:
        i+=1
        string = compact_one(string)
    return(string)

def calc_checksum(string):
    cur_num = 0
    res = 0
    for i in string:
        if i != ".":
            res += int(i)*cur_num
        cur_num+=1
    return(res)


# task 1

string_compressed = list(open("Input day 9.txt","r").read())
string_decompressed = decompress(string_compressed)
string_compacted =  compact_string(string_decompressed)
checksum = calc_checksum(string_compacted)
print(checksum)



### Part 2

def compact_list2(lis,ID):
    ID = str(ID)

    # trim of trailing empty space
    while lis[-1] == ":":
        lis = lis[:-1]

    length = lis.count(ID)
    location = lis.index(ID)


    ### find the location of the first dots that fit:
    # convert list to string, all files are single-digit zero:
    lis_single = ["0" if x!="." else "." for x in lis]
    lis_string = "".join(lis_single)
    # cut of all parts of that list which are to the right of our number
    lis_string = lis_string[:location]
    # find first location of .... that fits
    try:
        loc_of_emptyspace = lis_string.index("."*length)
    except:
        return(lis)
        # if none, skip this one

    # if empty space found
    # remove all files of ID from list
    # i.e. repalce it with dots
    lis_new = ["." if x==ID else x for x in lis]

    # then place that file, of same length at the correct location in the list
    for i in range(0,length):
        lis_new[loc_of_emptyspace+i]=ID
    
    return(lis_new)



lis = string_decompressed
ID = int(lis[-1])

while ID >= 0:
    lis = compact_list2(lis,ID)
    ID = ID - 1

calc_checksum(lis)