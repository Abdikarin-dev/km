
# guesser:

# secret = 4
# while True:
#     guess=int(input("Guess a number"))
#     if guess > secret:
#         print("Too hight!")
#     elif guess < secret:
#         print("Too low!") 
#     elif guess == secret:
#         print("Correct!")
#     else:
#      break



# #Random guesser:

import random
secret =random.randint(1,10)
while True:
    guess=int(input("Guess a number"))
    if guess > secret:
        print("Too hight!")
    elif guess < secret:
        print("Too low!") 
    elif guess == secret:
        print("Correct!")
    else:
     break












