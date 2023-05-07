import time

timer_start = time.time() # Grab Currrent Time Before Running the Code

from cryptogram_solver import * # This will run the whole module

timer_end = time.time() # Grab Currrent Time After Running the Code
timer_total_time = timer_end - timer_start # Subtract Start Time from The End Time

f = open("log.txt", "a") # Update the log:
log_text = str(version) + ' ' + str(timer_start) + ' ' + str(timer_total_time)
f.write(log_text+"\n")
f.close()
