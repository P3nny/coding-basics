from random import randint

secret = randint(1, 10)
# print(f"#cheatmode secret: {secret}")
guess = 0

while guess != secret:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < secret:
        print("The number is bigger")
    if guess > secret:
        print("The number is smaller")

print("You guessed it!")
