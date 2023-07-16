'''Create three separate processes. 
Make each one wait a random number of seconds between zero and one, 
print the current time, and then exit.'''

import multiprocessing
import random
import time
import datetime

def print_current_time():
    # Wait for a random number of seconds between 0 and 1
    t = random.randint(0, 1)
    print('Waiting for ' + str(t) + ' seconds.')
    time.sleep(t)

    # Print the current time
    print("Current time:", datetime.datetime.now())

if __name__ == "__main__":
    # Create three separate processes
    for num in range(3):
        p = multiprocessing.Process(target=print_current_time)
        p.start()
        p.join()