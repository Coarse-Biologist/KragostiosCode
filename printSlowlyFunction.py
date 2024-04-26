import time
import sys

def sloprint(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()  # Ensure the character is immediately displayed
        time.sleep(.05)
    print(" ", end = '\n')
    

def supersloprint(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()  # Ensure the character is immediately displayed
        time.sleep(.2)
    print(" ", end = '\n')
    
def slow_think():
    text = f"..... \n ....."
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()  # Ensure the character is immediately displayed
        time.sleep(.4)
    print(" ", end = '\n')
