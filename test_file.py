import random 

number = random.randint(0, 100)

guesses = 0
guess = int (input("Your guess >>>"))
while guess !=number:
    guesses +=1
    if guess < number:
        print(guess, "is too low")
    elif guess > number:
        print(guess, "is too high")
    guess = int(input("Your guess >>>"))


print("Great, you got it in", guesses, "guesses!")