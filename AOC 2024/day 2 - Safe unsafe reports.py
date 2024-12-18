### General functions

def file_read_lines(filename):
    with open(filename) as fil:
        file=fil.readlines()
    return(file)

def prep_list(length):
   return([ [] for i in range(length)])

def remove_from_list(li,index):
    return(li[:index] + li[index+1 :])










### Part 1 Functions -----------------------------------------

# returns the "deltas" from a list
# that is, the differences between each elemnt of list
# [1,5,2,3] becomes [4,-3,1]
def get_list_deltas(li):
    li_new = prep_list(len(li)-1)
    for i in range(0,len(li)-1):
        delta = li[i+1] - li[i]
        li_new[i] = delta
    return(li_new)

# checks if a list of deltas are safe 
# no deltas higher than 3, or 0
def is_rate_safe(li_delta):
    for i in li_delta:
        if abs(i) > 3 or abs(i) == 0:
            return(False)
    return(True)

# checks if a list of deltas are unidirectional
# if they are all of the same sign,
# then the absolute of their sum should be equal
# to the sum of their absolutes
def is_rate_unidirectional(li_delta):
    absum = abs(sum(li_delta))
    sumabs = sum([abs(item) for item in li_delta])
    if (absum != sumabs):
        return(False)
    else:
        return(True)



# Executing part 1 -----------------------------------

# read file
table_reports = file_read_lines("input day 2.txt")

# remove newlines, then split by spaces
for i_row in range(0,len(table_reports)):
    # remove newlines
    table_reports[i_row] =  table_reports[i_row].replace("\n","").split(" ")
    # make all integers
    table_reports[i_row] = [int(item) for item in table_reports[i_row]]

# copy ot table_reports, but with deltas
table_deltas = prep_list(len(table_reports))
for i_row in range(0,len(table_reports)-1):
    table_deltas[i_row] = get_list_deltas(table_reports[i_row])

# check both
def is_report_safe(li_delta):
    if is_rate_safe(li_delta) and is_rate_unidirectional(li_delta):
        return(True)
    else:
        return(False)

# count the number of safe reports
count = 0
for li_delta in table_deltas:
    if is_report_safe(li_delta):
        count = count+1

print(count)











### Part 2  functions --------------------------------------

def is_raw_report_safe(report):
    li_delta = get_list_deltas(report)
    return(is_report_safe(li_delta))

def is_dampened_report_safe(report):
    if is_raw_report_safe(report):
        return(True)
    for i_report in range(0,len(report)):
        report_popped = remove_from_list(report,i_report)
        if is_raw_report_safe(report_popped):
            return(True)
    return(False)



# Executing part 2 -----------------------------------------

count_damp = 0
for report in table_reports:
    if is_dampened_report_safe(report):
        count_damp = count_damp+1
print(count_damp)

