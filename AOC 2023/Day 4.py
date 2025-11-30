import re 

def file_read_lines(filename):
    with open(filename) as fil:
        file=fil.readlines()
    return(file)

def str_numbers_extract(string):
    res = re.findall(r'\d+', string)
    res=list(map(int, res))
    return(res)

def filter_in_list(list, reference):
    return([x for x in list if x in reference])

def prep_list(length):
    return([ [] for i in range(length)])

# https://stackoverflow.com/questions/952914/how-do-i-make-a-flat-list-out-of-a-list-of-lists
def flatten_list(l):
    return [item for sublist in l for item in sublist]

# https://stackoverflow.com/questions/1157106/remove-all-occurrences-of-a-value-from-a-list
def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

file = file_read_lines("Day 4 input.txt")

data = prep_list(len(file))
sum_points = 0
for i_row in range(0,len(file)):
    row = file[i_row]
    numbers_win = str_numbers_extract(re.search(r"\:([^_]*?)\|",row).group())
    numbers_got = str_numbers_extract(re.search(r"\|.*",row).group())
    data[i_row] = [numbers_win,numbers_got]
    numbers_match = filter_in_list(numbers_got,numbers_win)
    n_numbers_match = len(numbers_match)
    if (n_numbers_match==0):
        points=0
    else:
        points = 2**(n_numbers_match-1)
    sum_points = sum_points+points
    data[i_row]=[numbers_win,numbers_got,numbers_match,n_numbers_match]

# ANSWER 1
sum_points

# obtain all new cards obtained from a given card
def get_new_cards(card_number):
    points = data[card_number-1][3]
    if points==0:
        newcards=[]
    else:
        newcards = list(range(card_number+1,card_number+points+1))
        newcards = [x for x in newcards if x <= len(data)]
    return(newcards)

# resolves a card into all the cards it produces
# saves the output of that card for later use 
def resolve_card(card_number):
    list_cards = [card_number]
    list_cards_exhausted = []
    while len(list_cards) != 0:
        print(str(len(list_cards)) +" - "+ str(len(list_cards_exhausted)))
        list_new_cards = []
        for i_card in range(0,len(list_cards)):
            card = list_cards[i_card]
            if card in list_resolved_cards[0]:
                list_cards_exhausted = list_cards_exhausted+list_resolved_cards[1][card]
            else:   
                output = get_new_cards(card)
                list_new_cards = list_new_cards + output
                list_cards_exhausted.append(card)
            list_cards[i_card]="ø"
        list_cards = list_cards + list_new_cards
        list_cards = remove_values_from_list(list_cards,"ø")
    list_resolved_cards[0].append(card_number)
    list_resolved_cards[1][card_number]=list_cards_exhausted

    return(list_cards_exhausted)

# list of all resolved cards (first element is a list of all cards that are solved, second list contains their sollution)
list_resolved_cards = [[],prep_list(len(data)+1)] 

# resolve every card
for card in sorted(list(range(1,len(data)+1)),reverse=True):
    x=resolve_card(card)

# ANSWER 2
len(flatten_list(list_resolved_cards[1]))
