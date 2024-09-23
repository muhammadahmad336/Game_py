import random
taken_num=input("Type a number ")
if taken_num.isdigit():
     taken_num=int(taken_num)
     if taken_num <= 0:
            print("Please enter a number greater then 0")
            quit()
else:
    print("Please enter a number next time")
    quit()


guess_num = random.randrange(0,taken_num)
guess=0

while True:
    guess += 1
    user_guess = input("Guess a number ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("Please enter a number next time")
        continue

    if user_guess == guess_num:
        print("You guessed it!")
        print("it took you", guess , "guesses")
        break
    else:
        if user_guess > guess_num:
              print("Too high!")
        else:
            print("Too low!")
        

