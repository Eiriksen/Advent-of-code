### General functions 

import re
import math

def prep_list(length):
   return([ [] for i in range(length)])

def list_remove_empty(li):
    output = []
    for i in li:
        if i:
            output.append(i)
    return(output)

def reverse(string):
    return(string[::-1])

def file_read_lines(filename):
    with open(filename) as fil:
        file=fil.readlines()
    return(file)

def file_save_lines(x,filename):
    with open(filename, 'w') as f:
        for line in x:
            f.write(f"{line}\n")












### Part 1 functions -----------------------------------------
 
def rotate_table_45(table):
    # assumes all rows have same n of rows
    n_cols = len(table[0])
    n_rows = len(table)
    table_rotated = prep_list(n_cols + n_rows)
    # iterate over every item in the old table
    # place the item in the new table as if rotated
    for i_row in range(0,len(table)):
        for i_col in range(0,len(table[i_row])):
            cur_newrow = i_row + (len(table[i_row]) - i_col)
            table_rotated[cur_newrow].append(table[i_row][i_col])
    # output
    return(table_rotated)

def rotate_table_315(table):
    n_cols = len(table[0])
    n_rows = len(table)
    table_rotated = prep_list(n_cols + n_rows)
    # iterate
    for i_row in range(0,len(table)):
        # Backwards!:
        for i_col in range(len(table[i_row])-1, -1, -1):
            cur_newrow = i_row + i_col 
            table_rotated[cur_newrow].append(table[i_row][i_col])
    # everything is reversed this time, so reverse again 
    for i_row in range(0,len(table_rotated)):
        table_rotated[i_row] = reverse(table_rotated[i_row])
    # output
    return(table_rotated)

def rotate_table_90(table):
    n_cols = len(table[0])
    table_rotated = prep_list(n_cols)
    for i_row in range(0,len(table)):
        for i_col in range(0,len(table[i_row])):
            cur_newrow = len(table[i_col]) - 1 - i_col
            table_rotated[cur_newrow].append(table[i_row][i_col])
    return(table_rotated)

def join_rows(table):
    new_table = []
    for row in table:
        new_table.append( "".join(row) )
    return(new_table)

def count_in_table(regexp,tab):
    n = 0
    for row in tab:
        n = n + len(re.findall(regexp,row))
    return(n)



# Executing part 1 -----------------------------------

# read file and remove newlines
table = open("input day 4.txt","r").read().splitlines()

# make rotated versions
table_diagonal1 = join_rows(rotate_table_45(table))
table_diagonal2 = join_rows(rotate_table_315(table))
table_vertical = join_rows(rotate_table_90(table))

def count_bothways_in_table(regexp,table):
    n = 0
    n = n + count_in_table(regexp,table) 
    n = n + count_in_table(reverse(regexp),table)
    return(n)

# count xmas in all rotated versions
n_normal = count_bothways_in_table("XMAS", table)
n_diagonal1 = count_bothways_in_table("XMAS",table_diagonal1)
n_diagonal2 = count_bothways_in_table("XMAS",table_diagonal2)
n_vertical = count_bothways_in_table("XMAS",table_vertical)

# sum
print(n_normal+n_diagonal1+n_vertical+n_diagonal2)












### Part 2 functions --------------------------------

def read_diagonal(table,row):
    output = []
    x = 0
    y = row # is reversed in this coordinate system
    len_rows = len(table[0])
    len_cols = len(table)
    while y >= 0 and x < len_rows:
        # check if coordinate is in the table
        # only Y can be outside, so just check that one
        if y < len_cols:
            output.append(table[y][x])
            # if it is, pick the number and add to output
        # if not, skip this one
        x = x+1
        y = y-1
    return(output)

def pad_list(li,length,direction):
    missing = length-len(li)
    if missing < 0:
        return -1
    if direction > 0:
        return(li + prep_list(missing))
    if direction < 0:
        return(prep_list(missing) + li)

def table_unjoin_rows(table):
    new_table = []
    for row in table:
        new_table.append(list(row))
    return(new_table)

def table_pad(table,length,direction):
    new_table = []
    for row in table:
        new_table.append( pad_list(row,length,direction) )
    return(new_table)

def table_remove_empty(table):
    res = []
    for row in table:
        clean = list_remove_empty(row)
        if clean:
            res.append(clean)
    return(res)

def rotate_table_m45(table):
    table_rotated = []
    for i_row in range(0,len(table)+len(table[0])):
        table_rotated.append(read_diagonal(table,i_row))
    return(table_rotated)

def table_get_longest_row(table):
    list_len = [len(i) for i in table]
    return(max(list_len))

def table_reverse_rows(table):
    new_table = []
    for row in table:
        new_table.append(reverse(row))
    return(new_table)

def rotate_table_45(table):
    tab_unjoined = table_unjoin_rows(table)
    tab_padded_upper = table_pad(tab_unjoined[0:math.ceil(len(tab_unjoined)/2)],table_get_longest_row(tab_unjoined),1)
    tab_padded_lower = table_pad(tab_unjoined[math.ceil(len(tab_unjoined)/2):len(tab_unjoined)],table_get_longest_row(tab_unjoined),-1)
    tab_padded = tab_padded_upper + tab_padded_lower
    tab_reversed = table_reverse_rows(tab_padded)
    tab_rota = rotate_table_m45(tab_reversed)
    tab_rerev = table_reverse_rows(tab_rota)
    tab_clean = table_remove_empty(tab_rerev)
    return(join_rows(tab_clean))

def rotate_table_minus45(table):
    tab_unjoined = table_unjoin_rows(table)
    tab_padded_upper = table_pad(tab_unjoined[0:math.ceil(len(tab_unjoined)/2)],table_get_longest_row(tab_unjoined),-1)
    tab_padded_lower = table_pad(tab_unjoined[math.ceil(len(tab_unjoined)/2):len(tab_unjoined)],table_get_longest_row(tab_unjoined),1)
    tab_padded = tab_padded_upper + tab_padded_lower
    #return(join_rows(table_remove_empty(tab_padded)))
    tab_rota = rotate_table_m45(tab_padded)
    
    tab_clean = table_remove_empty(tab_rota)
    return(join_rows(tab_clean))



### Part 2 functions test --------------------------

# does minus 45 work?
rotate_table_minus45(table) 
# YES

# does 45 work?
rotate_table_45(table)
# YES

# does m45 - 45 work?
rotate_table_minus45(rotate_table_45(table)) == table
# YES

rotate_table_45(rotate_table_minus45(table)) == table
# YESSSSS

# how about a double 45 (=90) ??
rotate_table_45(rotate_table_45(table))
join_rows(rotate_table_90(table))
# HOLY SHIT YES



### PART 2 FOR REAL ---------------------------------------

# rotate table diagonally
# upgrade any A within a SAM / MAS to Ø
table_diagonal1 = rotate_table_45(table)
table_Ø = []
for row in table_diagonal1:
    j = re.sub("(?<=S)A(?=M)","Ø",row)
    j = re.sub("(?<=M)A(?=S)","Ø",j)
    table_Ø.append(j)

table_Ø_ori = rotate_table_minus45(table_Ø)
table_Ø_diagonal2 = rotate_table_minus45(table_Ø_ori)

# rotate table back, diagonally, twice
# upgrade an Ø within a SAM / MAS to Æ
table_Æ = []
for row in table_Ø_diagonal2:
    j = re.sub("(?<=S)Ø(?=M)","Æ",row)
    j = re.sub("(?<=M)Ø(?=S)","Æ",j)
    table_Æ.append(j)

# Count Æ's
print(
    count_in_table("Æ",table_Æ)
)
