print("------------------------ Practice Day 20 ------------------------")

# mini project day 4
# Pomodoro Timer App
import time
def pomodoro_timer(work_duration, short_break, long_break, cycles):
    for cycle in range(1, cycles + 1):
        print(f"Cycle {cycle}: Work for {work_duration} minutes.")
        countdown_timer(work_duration * 60)
        if cycle % 4 == 0:
            print(f"Long Break for {long_break} minutes.")
            countdown_timer(long_break * 60)
        else:
            print(f"Short Break for {short_break} minutes.")
            countdown_timer(short_break * 60)
    print("Pomodoro session complete!")
def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")
# Example: 25 minutes work, 5 minutes short break, 15 minutes long break, 4 cycles
pomodoro_timer(25, 5, 15, 4)

# Simple Alarm Clock
def alarm_clock(alarm_time):
    print(f"Alarm set for {alarm_time}.")
    while True:
        current_time = time.strftime("%H:%M")
        if current_time == alarm_time:
            print("Wake up! Alarm ringing!")
            break
        time.sleep(30)  # Check every 30 seconds
# Example: Set alarm for 1 minute from now
import datetime
now = datetime.datetime.now()
alarm_time = (now + datetime.timedelta(minutes=1)).strftime("%H:%M")
alarm_clock(alarm_time)

print("------------------------ End of Practice Day 20 ------------------------")