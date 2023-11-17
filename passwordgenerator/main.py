import random
import string

digits = []
letters = []
symbols = []
password = ""

for element in string.digits:
    digits.append(element)

for element in string.ascii_letters:
    letters.append(element)

for element in string.punctuation:
    symbols.append(element)

print("Welcome to the password Generator!")
nr_letters = int(input("How many letters would you like in your password\n"))
nr_symbols = int(input("How many symbols?\n"))
nr_numbers = int(input("How many numbers?\n"))
nr_all = nr_numbers + nr_letters + nr_symbols

for element in range(0, nr_all):
    rand = random.randint(0, nr_all)

    if 0 <= rand <= nr_letters != 0:
        rand_let = random.randint(0, 51) #random.choice(letters)
        password += letters[rand_let]
        nr_letters -= 1
    elif nr_letters < rand <= nr_symbols != 0:
        rand_sym = random.randint(0, 31)
        password += symbols[rand_sym]
        nr_symbols -= 1
    else:
        rand_num = random.randint(0, 9)
        password += digits[rand_num]
        nr_numbers -= 1
    nr_all = nr_numbers + nr_letters + nr_symbols

print(f"Here is your password: {password}")