import sys
from file_handler import generate_data

print("Client/Server and Encryption Program")
print("------------------------------------")
print("Options :")
print("1: Generate random text and send to server")
print("2: Generate random text, encrypt and send to server")
print("3: Generate random JSON data and send to server")
print("4: Exit")
print("------------------------------------")

not_valid = True
while not_valid:
    not_valid = False
    try:
        user_sel = int(input("Please make a selection: "))
    except ValueError:
        print("Please ensure you have entered a valid number")
    else:
        if user_sel == 1 or user_sel == 2 or user_sel == 3:
            generate_data(user_sel)
        elif user_sel == 4:
            print("Exiting...")
            sys.exit()
        else:
            print("Please enter within the range provided")
            not_valid = True




