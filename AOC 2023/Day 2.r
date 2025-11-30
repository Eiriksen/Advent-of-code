library(tidyverse)

read_input <- function(file) {
    lines <- readLines(file)
    df_input <- data.frame()
    for (line in lines){
        df_game <- read_game(line)
        df_input <- bind_rows(df_input,df_game)
    }
    df_input
}

read_game <- function(string){
    ID_game <- as.numeric(str_match(string, " (100|[1-9][0-9]|[1-9]):")[2])
    draws_string <- str_match(string, ": (.*)")[2]
    draws <- str_split(draws_string, "; ", simplify=T) 
    df_game <- data.frame()
    for (draw in draws){
        output <- read_draw(draw)
        df_game <- bind_rows(df_game, output)
    }
    df_game$ID <- ID_game
    df_game
}

read_draw <- function(string){
    cubes <- str_split(string, ", ", simplify = T)
    output <-  list()
    for (cube in cubes){
        color <- str_split(cube, " ", simplify=T)[2]
        number <- as.numeric(str_split(cube, " ", simplify=T)[1])
        output[[color]] <- number
    }
    output
}

df_input <- read_input("Day 2 input.txt")

df_input %>%
    mutate(
        possible = (is.na(red)|red<13) & (is.na(green)|green<14) & (is.na(blue)|blue<15)
    ) %>%
    group_by(ID) %>% 
    summarise(possible_game = all(possible)) %>%
    filter(possible_game==T) %>%
    pull(ID) %>%
    sum()

df_input %>%
    group_by(ID) %>%
    summarise(
        power = max(red,na.rm=T)*max(blue,na.rm=T)*max(green,na.rm=T)
    ) %>%
    pull(power) %>%
    sum()
