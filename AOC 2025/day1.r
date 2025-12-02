

# task 1 in R:
input_day1 <- scan("AOC 2025/input day 1.txt", character())
 
li_directions_char <- substr(input_day1, 0, 1)
li_directions      <- c("R" = 1, "L" = -1)[li_directions_char]
li_increments_abs  <- substr(input_day1, 2, 10) |> as.numeric()
li_increments      <- li_directions * li_increments_abs
li_positions       <- cumsum(c(50,li_increments))
li_positions_dial  <- li_positions %% 100

print(sum(li_positions_dial == 0))


