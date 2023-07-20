import time
import os 
os.system("cls")
def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

def get_user_input():
    while True:
        try:
            seconds = int(input("Enter the countdown time in seconds: "))
            if seconds > 0:
                return seconds
            else:
                print("Please enter a positive integer for the countdown.")
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")

def main():
    print("Welcome to the Countdown Timer!")
    seconds = get_user_input()
    countdown_timer(seconds)

if __name__ == "__main__":
    main()
