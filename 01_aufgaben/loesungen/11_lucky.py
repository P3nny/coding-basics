from random import randint

lucky_number = randint(1, 10)
print(f"lucky_number: {lucky_number}")

if lucky_number == 3:
    print("You are lucky!")
else:
    print("You are not lucky!")
