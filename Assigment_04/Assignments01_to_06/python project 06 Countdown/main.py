# Project 6: Countdown Timer Python Project BY Hammad Ahmed..!

# Importing the required libraries
import time

def CountDown_timer(seconds):
    while(seconds):
        mins , secs = divmod(seconds , 60) #divmod() function takes two numbers and returns a tuple of their quotient and remainder.
        
        timer = f'{mins:02}:{secs:02}'
        
        print(timer , end="\r") #end="\r" is used to overwrite the previous line in the console.
        
        time.sleep(1) #time.sleep(1) is used to pause the program for 1 second.
        
        seconds -= 1 #decrementing the seconds by 1
        
    print("⏰ Time's up!") #prints the message when the countdown is over
    
    #taking the timer input from the user
seconds = int(input("Enter the time in seconds: "))
CountDown_timer(seconds)