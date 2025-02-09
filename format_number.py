from math import floor
def format_number(number: int):
    listed_number = list(str(number))
    if(len(str(number)) % 3 != 0):
        repeat = floor(len(str(number)) / 3)
    else:
        repeat= int((len(str(number)) / 3) - 1)
    while repeat != 0:
        listed_number[(repeat*3*-1):(repeat*3*-1)] = [","]
        repeat -= 1
    print("".join(listed_number))
format_number(1342423782345667)
