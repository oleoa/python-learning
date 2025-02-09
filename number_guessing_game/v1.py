import random
_answer = random.randrange(100)
_try = int(input("Try a number from 0 to 100: "))

if _answer == _try:
    print("You won!")
else:
    print("You lost! The correct answer was: ", _answer)
