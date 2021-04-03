import random

number  = random.randint(0,24)
number_of_guesses = 0
print(number)

player_name = input("Hello, what's your name?")
number_of_guesses = 0
print("wELCOME" + player_name + ", guess a number between 1 and 10:")

while number_of_guesses < 5:
    guess = int(input("What is your guess? "))
    number_of_guesses += 1
    if guess < number:
        print("Your guess is too low")
    elif guess > number:
        print("Your guess is too high")
    
if guess == number:
    print("Congratulations! You guessed correctly.")
else:
    print("You did not guess the number, the number was ")
    print(number)
