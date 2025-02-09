# This is just a comment

# Variables
name = "Leonardo"
age = 19
books = ["Atomic Habits", "Rich Dad Poor Dad"]

# Casting Variables
string = str(3) # "3"
integer = int(3) # 3
flt = float(3) # 3.0

# Getting the type
type(integer)

# Case-Sensitive
a = 10
A = 20 # Won't overwrite a

# Legal Variables Name
myvar = "Leo"
my_var = "Leo"
_my_var = "Leo"
myVar = "Leo"
MYVAR = "Leo"
myvar2 = "Leo"
Myvar = "Leo"

# Camel Case
myVariableName = "Leo"

# Pascal Case
MyVariableName = "Leo"

# Snake Case
my_variable_name = "Leo"

# Multiple Differents Variables Inline
x, y, z = 10, "20", 30.0

# Multiple Equal Variables Inline
x = y = z = "yes"

# Unpacking
arr = ["Leonardo", "Abreu", "Paulo"]
first_name, middle_name, last_name = arr # Must be same length

# Global Variables
testing_var = "global variable"
testing_global_var = "aways global variable"

def myFunction():
    testing_var = "local variable"
    type(testing_var)
    global testing_global_var
    testing_global_var = "new global variable"

myFunction()

# Variables Types
_string = "This is a string" # str("Value")
_integer = 19 # int(19)
_float = 3.14 # float(3.14)
_complex = 1j # complex(1j)
_list = ["apple", "banana", "peach"] # list(("apple", "banana", "peach"))
_tuple = ("apple", "banana", "peach") # tuple(("apple", "banana", "peach"))
_range = range(6) # range(6)
_dict = {"name": "Leo", "age": 19} # dict(name="Leo", age=19)
_set = {"apple", "banana", "peach"} # set(("apple", "banana", "cherry"))
_frozenset = frozenset({"apple", "banana", "cherry"}) # frozenset({"apple", "banana", "cherry"})
_bool = True # bool(1)
_bytes = b"Bytes" # bytes(5)
_bytearray = bytearray(5) # bytearray(5)
_memoryview = memoryview(bytes(5)) # memoryview(bytes(5))
_none = None

# Conversion
_float = 3.70
_int = int(_float) # 3

# Random numbers
import random
_random = random.randrange(1, 10)

# Inside Quotes
qts = "This it's alright"
qts = "And 'this' is also fine"
qts = 'And letting it like "that" is also ok'

# Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

# Strings is arrays
name = "Leonardo"
e = name[1]

# Looping Through a String
for x in "Leonardo":
    type(x) # L e o n a r d o

# Getting the length
name = "Leonardo"
name_length = len(name) # 8
_arr = ["apple", "banana", "peach"]
array_length = len(_arr) # 3

# Negative Indexing
arr = ["apple", "banana", "peach"]
name = "Leonardo"
apple = arr[-3]
a = name[-4]

# Checking String
full_name = "Leonardo Abreu de Paulo"
_abreu = "Abreu" in full_name # True
_jose = "Jose" in full_name # False

# Checking if Not
full_name = "Leonardo Abreu de Paulo"
_abreu = "Abreu" not in full_name # False
_jose = "Jose" not in full_name # True

# Checking with If
full_name = "Leonardo Abreu de Paulo"
if "Abreu" in full_name:
    type("Abreu is in the full_name")
if "Jose" not in full_name:
    type("Jose is not in the full_name")

# Slicing Strings
full_name = "LeonardoAbreuDePaulo"
abreu = full_name[8:13] # 13 not included ("D")
leonardo = full_name[:8] # it slices from the start and 8 not included ("A")
paulo = full_name[15:] # it slices to the end
de = full_name[-7:-5] # -5 not included ("P")

# String Cases
Name = "Leonardo"
NAME = Name.upper()
name = Name.lower()

# No Whitespaces
bad_whitespaces = " Leonardo Abreu "
corrected_whitespaces = bad_whitespaces.strip() # "Leonardo Abreu"

# Replace String
fry = "fry"
fly = fry.replace("r", "l")
leonardo = "Leonardo"
leunardu = leonardo.replace("o", "u")

# Split String
full_name = "Leonardo Abreu de Paulo"
full_name_arr = full_name.split(" ") # ['Leonardo', 'Abreu', 'de', 'Paulo']

# String Concatenation
first_name = "Leonardo"
last_name = "Paulo"
name = first_name + " " + last_name

# F-Strings
age = 19
f_string = f"My name is Leonardo and I'm {age} years old"
price = 59
f_string = f"The product is for €{price:.2f}"
f_string = f"Multiplying 7 x 19 is equal to {7*19} which is bigger than {7*18}"

# Escape Character
text = "My name is \"Leonardo\""

# Boolean Values
_greater = 10 > 9 # True
_equals = 5 == 5 # True
_less = 10 < 9 # False
_int = bool(15) # True
_int = bool(-1) # True
_int = bool(0) # False
_str = bool("Leo") # True
_str = bool("") # False
_arr = bool(["apple"]) # True
_arr = bool([""]) # True
_arr = bool([]) # False
_in = "banana" in ["apple", "banana", "peach"]
def returnTrue():
    return True

# Check Variable Type
_str = "10"
isInt = isinstance(_str, int) # False
isStr = isinstance(_str, str) # True

# Arithmetic Operators
addition = 5 + 8 # 13
subtraction = 10 - 7 # 3
multiplication = 3 * 5 # 15
division = 100 / 7 # 14.285714285714286
modulus = 10 % 3 # 1
exponentiation = 5 ** 2 # 25
floor_division = 7 // 4 # 1 (1.75)

# Assignment Operators
x = 5
x += 3 # x = x + 3
x -= 4 # x = x - 4
x *= 2 # x = x * 2
x /= 2 # x = x / 2
x %= 3 # x = x % 3
x **= 2 # x = x ** 2
x //= 4 # x = x // 4

# Comparison Operators
x = 5
y = 10
_eq = x == y
_neq = x != y
_gt = x > y
_lt = x < y
_get = x >= y
_let = x <= y

# Logical Operators
_and = 5 > 1 and 50 > 10
_or = 5 > 10 or 50 > 10
_reverse = not(True) # False

# Identity Operators
x = 10
y = "10"
type(x is y) # False
type(x is not y) # True

# Preferences
x = (100 + 5 * 3) # 115 because * goes first

# Arrays
# Lists is a collection ordered and changeable that allows duplicates
# Tuple is a collection ordered and unchangeable that allows duplicates
# Set is a collection unordered, unchangeable and unindexed that does not allows duplicates
# Dictionary is a collection ordered and changeable that does not allows duplicates
_list = ["my", "list", 1, True]

# List length
_list_length = len(_list) # 3

# List type
_list_type = type(_list) # <class 'list'>

# Get item from list
_1 = _list[2]
_True = _list[-1]

# Get list from range
_no_my = _list[1:]

# Check if item is in list
_is_list_in_list = "list" in _list

# Change item in list
_list[0] = "your"

# Change items in list
_list[0:2] = ["new", "method"]

# Add items before with changing
_new_list = ["my", "normal", "list", "length"]
_new_list[1:2] = ["not", "different"] # Replaces "normal" with "not" and adds "different" after "not"
_new_list[1:] = "list" # Replaces all the rest of the list with "list"

# Adding item to list
name_list = ["Leonardo", "de"]
name_list.insert(1, "Abreu")
name_list.append("Paulo")

# Adding list to list
name = ["Leonardo", "Abreu"]
last_name = ["de", "Paulo"]
name.extend(last_name)

# Removing item
my_wallet = ["€100", "€50", "€20", "€100", "€5"]
my_wallet.remove("€100")
pop_list = ["My", "life", "is", "not", "good", "really"]
pop_list.pop(3)
pop_list.pop() # Removes the last
del pop_list[1] # Removes the indexed
del pop_list # Deletes the list
clear_list = ["apple", "banana"]
clear_list.clear() # Deletes all the items but not the var

# Looping
thislist = ["apple", "banana", "peach"]
for x in thislist:
    type(x) # String "apple", "banana", "peach"
for i in range(len(thislist)):
    type(i) # Int 0, 1, 2
index = 0
while index < len(thislist):
    type(index) # Int 0, 1, 2
    index += 1

# Sets
_set = set(("apple", "banana", 1, 0, 2))
_len = len(_set)
_type = type(_set)
_in = "apple" in _set
_not_in = "peach" not in _set
_set.add("peach")
_now_in = "peach" in _set
for x in _set:
    type(x)

print(_now_in)
