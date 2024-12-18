### general functions
import numpy


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


input_day_7 = open("Input day 7.txt","r").read().splitlines()
list_results = [ int(i.split(": ")[0]) for i in input_day_7]
table_numbers = [ i.split(": ")[1:][0].split(" ") for i in input_day_7]
table_numbers = [ [ int(a) for a in i ] for i in table_numbers  ]

def execute_operators(list_numbers,operators,result):
    output = list_numbers[0]

    for i in range(0, len(operators)):
        operator = operators[i]
        num = list_numbers[i+1]

        if operator == 0:
            output = output*num
        if operator == 1:
            output = output+num
        if operator == 2:
            output = concat(output,num)
    
    if output == result:
        return(output)
    else:
        return(0)
    
def check_for_solvable_combination(result,list_numbers,oprtrs=2):
    n_operators = len(list_numbers)-1

    for combination in list_combinations(oprtrs,n_operators):
        if execute_operators(list_numbers,combination,result) != 0:
            return(result)
    return(0)

# PART 1: + and * 

out = []
for i in range(0, len(list_results)):
    result = list_results[i]
    list_numbers = table_numbers[i]
    out.append(check_for_solvable_combination(result,list_numbers))

print(out)
print(sum(out))

# PART 2: + and * and ||

out = []
for i in range(0, len(list_results)):
    result = list_results[i]
    list_numbers = table_numbers[i]
    out.append(check_for_solvable_combination(result,list_numbers,3))

print(out)
print(sum(out))



