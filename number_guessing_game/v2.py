import random
_answer = random.randrange(100)
_won = False
_tentatives = 0

print("You will have to try a number from 0 to 100:")

while _won == False:
    _try = int(input("Your new try: "))
    _tentatives += 1
    if(_try == _answer):
        print("You won!\nIt took you "+str(_tentatives)+" tries")
        _won = True
    else:
        _logic = "greater than" if _try < _answer else "less than"
        print("Nope, the answer is "+_logic+" "+str(_try))
