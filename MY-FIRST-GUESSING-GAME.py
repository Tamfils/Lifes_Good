import random

random_min = random.randint(1,20)
random_max = random.randint(1,20)

def lowest():
    if random_min < random_max:
        return random_min
    else:
        random_max is random_min
        return random_max
def highest():
    if random_min < random_max:
        return random_max
    else:
        random_max is random_min
        return random_min

def main():
    print(" I am guessing a number between ", lowest(), " and ", highest())
    secret_number = random.randint(lowest(),highest())
    while True:
        user_guess = input(" Please Guess a Number: ")
        if int(user_guess) == secret_number:
            print("you've guessed the right number!")
            break
        elif int(user_guess) > secret_number:
            print("too high")
        elif int(user_guess) < secret_number:
         print("too low")
        
main()