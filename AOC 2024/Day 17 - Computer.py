
### General functions ----------
import re
import copy



### Task specific functions

def read_input(file):
  A = int(re.findall("A: (.*)\n", file)[0])
  B = int(re.findall("B: (.*)\n", file)[0])
  C = int(re.findall("C: (.*)\n", file)[0])
  P = [int(i) for i in re.findall("Program: (.*)", file)[0].split(",")]
  return [A,B,C,P] 

def run_program_once(x):
    OUT = x%8 ^2 ^7 ^(f_division(x,x%8 ^2)) % 8
    return OUT

def f_division(x,y):
    return int(x / (2**y))

def run_program(A,B,C,program):
    out = []
    pointer = 0
    while pointer < len(program):
        opcode = program[pointer]
        # literal operand
        ø = program[pointer+1]
        # combo operand
        æ = {0:ø,1:ø,2:ø,3:ø,4:A,5:B,6:C,7:None}[ø]

        match opcode:
            case 0: A = f_division(A,æ)
            case 1: B = B^ø
            case 2: B = æ%8
            case 3:
                if A!=0: pointer = ø
                else:    pointer +=2
            case 4: B = B^C
            case 5: out.append(æ % 8)
            case 6: B = f_division(A,æ)
            case 7: C = f_division(A,æ)

        if opcode != 3: pointer += 2
    
    return out









# Execute Task 1 ---------------------

file = read_input(open("Input day 17.txt").read())
A = file[0]
B = file[1]
C = file[2]
program = file[3]

out = run_program(A,B,C,program)
print(",".join(map(str,out)))










### Execute part 2 ------------------

# For each time the program runs (from start 2 to end 3) and outputs
# some number which is entirely based of A: 
# - the value of A is then divided by 8 and taken the integer of
# - - this operation really just removes the 3 last binary digits of A
# - and the programs starts over again:
# - shaving off 3 binary digits until, outputing a number, restarting
# - until there is no binary digits left
# 
# so, if we were to run this operation in reverse,
# we could start by finding the 3-binary numbers which gives us our last-
# number of the program (0), which is 101.
# Then we keep adding 3-binary numbers for each number of the program,
# testing to find which ones gives us the correct number.
# After 101, the next number has to be 011, because only A=101011 outputs 3,
# ... which is the next number of the program (in reverse)


# all possible combinatons for 3 binary digits:
addons = ["000","001","010","011","100","101","110","111"]
# list to hold those binaries which may work:
# (we start with an empty one: "")
possible_binaries = [""]

for i in reversed(program):
    new = []
    # go through each possible binary combination
    for binary in possible_binaries:
        # then for that, go through each possible 3-binary digit
        for addon in addons:
            # check if adding that gives the correct output of the program
            if run_program_once(int(binary + addon,2)) == i:
                # if it does, add it to the list of possible combinations
                new.append(binary + addon)
    
    possible_binaries = copy.deepcopy(new)

# runs in 0.002 seconds
smallest_A = min([int(i,2) for i in possible_binaries])
print(program)
print(run_program(smallest_A,B,C,program))
print(smallest_A)









# Some notes:
#Program: 2,4,1,2,7,5,0,3,1,7,4,1,5,5,3,0
#
# 2,4 A%8 -> B
# 1,2 B^2 -> B
# 7,5 div(A,B) -> C
# 0,3 div(A,3) -> A
# 1,7 B^7 -> B
# 4,1 B^C -> B
# 5,5 out(B^8)      
# 3,0
#
# 2,4 A0%8 -> B1
# 1,2 B1^2 -> B2
# 7,5 div(A0,B2) -> C1
# 0,3 div(A0,3) -> A1
# 1,7 B2^7 -> B3
# 4,1 B3^C1 -> B4
# 5,5 out(B4^8)      
# 3,0
#
# OUT = ((((A0^8)^2)^7)^(div(A0,(A0^8)^2))))^8
# OUT = A%8 ^2 ^7 ^(f_division(A,A%8 ^2)) % 8
#
#
# division operator:
# shaves off the three first (read last) bits
#
# modulo 8: 
# Gives you the three first (read last) bits 
#
# xor:
# bit length not necessarily the same, but never longer


