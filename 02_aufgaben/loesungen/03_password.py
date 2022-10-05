password = "maus"
user_input = ""

while user_input != password:
    user_input = input("Enter the password: ")
    # print(user_input)

    if user_input != password:
        print("Wrong password!")
    else:
        print("You are logged in.")
