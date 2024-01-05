# your code goes here!
import time

def countdown(second):
    # second= 20
    while second >= 1:
        print(f'{second} SECOND(S)!')
        second -= 1
    return print("HAPPY NEW YEAR!") 


def countdown_with_sleep(number):
    # number= 20
    while number >= 1:
        print(f'{number} SECOND(S)!')
        time.sleep(1)
        number -= 1
    return print("HAPPY NEW YEAR!") 

