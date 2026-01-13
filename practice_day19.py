print("------------------------ Practice Day 19 ------------------------")

# mini project day 3

# timer app
import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")
# Set timer for 10 seconds for demonstration
countdown_timer(10)

# Timer with user input in hour min and sec format
def user_countdown_timer(hours, minutes, seconds):
    total_seconds = hours * 3600 + minutes * 60 + seconds
    while total_seconds:
        mins, secs = divmod(total_seconds, 60)
        hrs, mins = divmod(mins, 60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hrs, mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        total_seconds -= 1
    print("Time's up!")
# Example: 0 hours, 0 minutes, 10 seconds
user_countdown_timer(0, 0, 10)

# Stopwatch app
def stopwatch():
    input("Press Enter to start the stopwatch...")
    start_time = time.time()
    input("Press Enter to stop the stopwatch...")
    end_time = time.time()
    elapsed_time = end_time - start_time
    mins, secs = divmod(elapsed_time, 60)
    hrs, mins = divmod(mins, 60)
    print("Elapsed Time: {:02d}:{:02d}:{:05.2f}".format(int(hrs), int(mins), secs))
stopwatch()
    
print("------------------------ End of Practice Day 19 ------------------------")