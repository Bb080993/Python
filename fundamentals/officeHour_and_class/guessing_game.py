import random

is_playing = True
answer=random.randint(1,10)
while is_playing :

    
    response = input("\nWhat number am I thinking of between 1-9")
    
    if response.lower() == "quit":
        is_playing = False
    elif int(response) == answer:
        print("You got it!")
        is_playing =False
    elif int(response) < answer:
        print("Too low!")
    elif int(response) > answer:
        print("Too high!")
    

    

print("Have a nice day!")

"""
    Requirements:
        - User enters their guess
        - User is told if their guess is too high or too low
            - continue guessing
        - User is told if they guessed correctly
            - print total number of guesses
            - end game
            - Thank the user for playing
"""