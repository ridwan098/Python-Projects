# time to wake up
current_time_string = input("what is the current time(in hours)?")
waiting_time_string = input("How many hours do you have to wait?")

current_time_int = int(current_time_string)
waiting_time_int = int(waiting_time_string)

hours = current_time_int + waiting_time_int

timeofday = hours % 24

print(timeofday)

# this programme does not work if you input the time in the time format, e.g 12:26, how do you make something like an if statement that will remind the users to make sure their number is in hours?
#also this program exceeds time of more than 24 hours, which doesnt make sense- e.g 34.
