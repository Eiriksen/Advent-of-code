def prep_list(length):
   return([ [] for i in range(length)])

def list_remove_empty(li):
    output = []
    for i in li:
        if i:
            output.append(i)
    return(output)

def remove_from_list(li,index):
    return(li[:index] + li[index+1 :])

def get_center_number(l):
    return(l[math.floor(len(l)/2)])

def reverse(string):
    return(string[::-1])

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

def table_unjoin_rows(table):
    new_table = []
    for row in table:
        new_table.append(list(row))
    return(new_table)

def table_join_rows(table):
    new_table = []
    for row in table:
        new_table.append( "".join(row) )
    return(new_table)

def read_file_splitlines(filename):
    return(open(filename,"r").read().splitlines())


def leading_zeroes(number,zeroes):
    # adds leading zeroes
    return(str(number).zfill(zeroes))

def list_combinations(digits,length):
    # gives all possible combinations of n digits
    # at a given length
    list_out = []
    for i in range(0,digits**length):
        combination = list(leading_zeroes(numpy.base_repr(i,digits),length))
        combination = [int(i) for i in combination]
        list_out.append(combination)
    return(list_out)

def concat(a, b):
    # e.g. concat(20,34)=2034
    return int(f"{a}{b}")

def does_list_contain(l,symbol):
    try:
        l.index(symbol)
        return(True)
    except:
        return(False)

def count_in_table(regexp,tab):
    n = 0
    for row in tab:
        n = n + len(re.findall(regexp,row))
    return(n)

def get_relPos(pos,direction,speed):
    # return relative position
    radians = direction*math.pi/180
    delta_x = round(math.cos(radians)*speed)
    delta_y = round(math.sin(radians)*speed)
    return([pos[0]+delta_x,pos[1]+delta_y])

def get_pos_of(what,table):
    # return positon of symbol in a table
    # table is x-y table
    # find which row:
    for i in range(0,len(table)):
        try:
            # will only work if "what" is in the table row
            return([i, table[i].index(what)])
        except:
            next
    return -1

def save_map_gen(t,filename):
    m = [[list(map(str,i)) for i in a] for a in t]
    m = [[item for col in row for item in col] for row in m]
    m = ["".join(i) for i in m]
    with open(filename, 'w') as f:
        for line in m:
            f.write(f"{line}\n")

def out_of_bounds(p,table):
    if p[0] < 0 or p[1] < 0:
        return(True)
    elif p[0] > len(table)-1 or p[1] > len(table[p[0]])-1:
        return(True)
    else:
        return(False)

def pad_map(table):
    width = len(table[0])
    table.insert(0,["Ø"]*width)
    table.append(["Ø"]*width)
    for i in range(0,len(table)):
        table[i].insert(0,"Ø")
        table[i].insert(len(table[i]),"Ø")
    return(table)



# function that finds all indexes of vlaue in list
def get_index_of_all(l,value):
    return([i for i,val in enumerate(l) if val==value])

# function that finds all locations of a symbol in a table
def get_pos_of_all(what,table):
    list_pos = []
    # return positon of symbol in a table
    # table is x-y table
    # find which row:
    for i in range(0,len(table)):
        indexes = get_index_of_all(table[i],what)
        for j in indexes:
            list_pos.append([i,j])
    return(list_pos)

# paints locations in a table
def paint_locations(locations,table,symbol):
    for pos in locations:
        if not out_of_bounds(pos,table):
            table[pos[0]][pos[1]] = symbol
    return(table)
    
def replace_at_index(string,index,new):
    return(string[:index] + [new] + string[index+1:])


