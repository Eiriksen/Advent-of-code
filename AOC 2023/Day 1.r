# Day 1

library(readr)
library(tidyverse)

lines <- readLines("Day 1 input.txt")
lines_df <- data.frame(string =lines)

get_numbers_in_string <- function(string){
    matches <- regmatches(string, gregexpr("[[:digit:]]+", string))
    as.numeric(unlist(matches))
}

get_fl_digits_in_string <- function(string){
    numbers <- get_numbers_in_string(string)
    merged <- paste(numbers,sep="",collapse="")
    first <- substr(merged,0,1)
    len <- nchar(merged)
    last <- ifelse(len!=1,  substr(merged,len,len), first)
    return(paste(c(first,last),sep="",collapse=""))
}

convert_textdigits_tonumeric <- function(string){
    string <- str_replace_all(string, "one", "1")
    string <- str_replace_all(string, "two", "2")
    string <- str_replace_all(string, "three", "3")
    string <- str_replace_all(string, "four", "4")
    string <- str_replace_all(string, "five", "5")
    string <- str_replace_all(string, "six", "6")
    string <- str_replace_all(string, "seven", "7")
    string <- str_replace_all(string, "eight", "8")
    string <- str_replace_all(string, "nine", "9")
    string
}

get_firstdigit_string_conv <- function(string){
    read <- ""
    len <- nchar(string)
    for (pos in 1:len){
        read <- substr(string,0,pos)
        read_conv <- convert_textdigits_tonumeric(read)
        numbers <- get_numbers_in_string(read_conv)
        if(length(numbers)!=0) return(numbers[1])
        string <- paste(read_conv,substr(string,pos+1,len),sep="")
    }
    return("")
}
get_lastdigit_string_conv <- function(string){
    read <- ""
    len <- nchar(string)
    for (pos in len:1){
        read <- substr(string,pos,len)
        read_conv <- convert_textdigits_tonumeric(read)
        numbers <- get_numbers_in_string(read_conv)
        if(length(numbers)!=0) return(numbers[1])
        string <- paste(substr(string,0,pos-1),read_conv,sep="")
    }
    return("")
}

get_fl_digits_in_string_conv <- function(string){
    first <- get_firstdigit_string_conv(string)
    last <- get_lastdigit_string_conv(string)
    return(paste(c(first,last),sep="",collapse=""))
}

lines_df  %>%
    rowwise() %>%
    mutate(
        number = as.numeric(get_fl_digits_in_string(string))
    ) %>% 
    pull(number) %>%
    sum()

lines_df %>% 
    rowwise() %>%
    mutate(
        number = as.numeric(get_fl_digits_in_string_conv(string))
    ) %>% 
    pull(number) %>%
    sum()