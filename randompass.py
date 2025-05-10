import random
import string

characters = []

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

counter = 0

all_chars = lower + upper + num + symbols
all_chars = all_chars.replace("~", "").replace("|", "").replace("^", "")

def password_creator():
    length = int(input("Number of characters: "))
    amount = int(input("How many passwords do you want to generate? "))

    if length > 15 or length < 5:
        print("The password must be between 5 and 15 characters.")
        length = 0
        password_creator()
    else:
        password_generator(length, amount, counter)


def password_generator(length, amount, counter):
    for i in range(amount):
        temp = random.sample(all_chars, length)

        counter += 1
        password = "".join(temp)
        print(f"Your password number {counter} is: {password}")
        with open("randompass.txt", "a") as f:
            f.write(f"Your password number {counter} is: {password}\n")

    next_step = input("Next password...")
    password_generator(length, amount, counter)

password_creator()
