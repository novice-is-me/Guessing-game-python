# guessing game

import random

random_num = random.randint(1,20)
print("-"*20)
print("Guessing Game")
print("-"*20)
try:
    for i in range (5):
        guess = int(input("Enter the number: "))
        if guess == random_num:
            print("Wow amazing! You guessed it!!")
            break
        if guess > 20 or guess < 1:
            print("Thats out of range. Try another number...")
        if guess <= 20 and guess > random_num:
            print("Thats too high dude!!")
        if guess >= 10 and guess < random_num:
            print("You should make it more higher than that hehe")
        if guess < 10 and guess < random_num:
            print("Make it higher!")
except:
    print("Thats a wrong input!! Be good. Try again!!")