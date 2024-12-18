library(tidyverse)

count_occurences <- function(a,b){
  # counts the number of times any element in a appears in b
  output <- c()
  for (i in 1:length(a)){
    occurences <- sum(b %in% a[i])
    output[i] <- occurences
  }
  return(output)
}

tb_input <- read_delim("input day 1.txt", delim = "   ",col_names=c("c1","c2")) |> 
  mutate(
    c1 = sort(c1),
    c2 = sort(c2),
    diff = abs(c1-c2),
    c1_repeats = count_occurences(c1,c2),
    score_repeats = c1 * c1_repeats
  )

print(
  sum(tb_input$diff)
)

print(
  sum(tb_input$score_repeats)
)