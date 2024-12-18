
import pandas as pd

def file_read_lines(filename):
    with open(filename) as fil:
        file=fil.readlines()
    return(file)

file = file_read_lines("input day 1.txt")

tb_txt = pd.read_csv("input day 1.txt",delimiter="  ",names=["col1","col2"], engine="python")

tb_txt.assign(
    col1 = sorted(tb_txt["col1"]),
    col2 = sorted(tb_txt["col2"]),
    )

# giving up here, need an intro to pandas before doing this
