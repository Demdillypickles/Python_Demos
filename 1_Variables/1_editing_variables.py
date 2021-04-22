# ----------------------------------------
# Try changing these variables and looking for the different outputs

my_name = "Bob"

fav_animal = "dog"

number = 3

string = "fizz"

crazy_number = 6

# ----------------------------------------
# Then try looking at these lines to see how these outputs were made

# Output 1
print(f"Hello, my name is {my_name} and I want a pet {fav_animal}!")

# Output 2
print(number)

# Output 3
print(number + 2)

# Output 4
# --------------------
number = number + 2
print(number)
# --------------------

# Output 5
# --------------------
number += 2
print(number)
# --------------------

# Output 6
print(string + string)

# Output 7
print(string * 5)

# Output 8
# --------------------
string *= 3
print(string)
# --------------------

# Output 9
# --------------------
x = crazy_number
print((x**4 + (x + 1)) ** x)
# --------------------
