import random
from pip import main

def play():
    random_number = random.randint(0,100)
    number_selected = int(input("Select a number: "))

    while number_selected != random_number:
        if number_selected < random_number:
            print("Select a bugger number")
        else:
            print("Select a smaller number")
        
        number_selected = int(input("Select a number: "))

    print("You\'ve won")
        


if __name__ == '__main__':
    play()