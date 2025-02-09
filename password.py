# Password Generator
import random

# From 2 to 16
LENGTH_RANGE = range(2, 17)

length = 2
has_upper_case = None
has_special_characters = None

def get_password_length():
    global length
    l = int(input(f"Select a length [{LENGTH_RANGE.start}-{LENGTH_RANGE.stop-1}]: "))
    if l not in LENGTH_RANGE:
        print("Not the right length")
        return False
    else:
        length = l
        return True

def get_password_has_upper_case():
    global has_upper_case
    uc = str(input("Want upper case? [y/n]: "))
    if uc not in ["y", "n"]:
        print("Not the right answer [y/n]")
        return False
    else:
        if uc == "y":
            has_upper_case = True
        else:
            has_upper_case = False
        return True

def get_password_has_special_characters():
    global has_special_characters
    hsp = str(input("Want special characters? (%, &, $, #, @, +, =, -, _)[y/n]: "))
    if hsp not in ["y", "n"]:
        print("Not the right answer [y/n]")
        return False
    else:
        if hsp == "y":
            has_special_characters = True
        else:
            has_special_characters = False
        return True

def generate_new_password():
    global length, has_upper_case, has_special_characters
    lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upper_letters = list(map(str.upper, lower_letters))
    special_characters = ['!', '@', '#', '$', '%', '&', '-', '_', '=', '+']
    possibilities = []
    possibilities.append(lower_letters)
    if has_upper_case:
        possibilities.append(upper_letters)
    if has_special_characters:
        possibilities.append(special_characters)
    password = []
    for x in range(length):
        type = possibilities[random.randrange(len(possibilities))]
        item = type[random.randrange(len(type))]
        password.append(item)
    return "".join(password)

while True:
    if get_password_length():
        break
while True:
    if get_password_has_upper_case():
        break
while True:
    if get_password_has_special_characters():
        break
password = generate_new_password()
print("Your new password is:\n", password)
