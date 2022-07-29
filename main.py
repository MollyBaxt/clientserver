import sys
from src.file_handler import generate_data


def main():
    print("Client/Server and Encryption Program")
    print("------------------------------------")
    print("Options :")
    print("1: Generate random text and send to server")
    print("2: Generate random text, encrypt and send to server")
    print("3: Generate random JSON data and send to server")
    print("4: Exit")
    print("------------------------------------")

    not_valid = True  # Boolean flag to check is validity of choice.
    while not_valid:
        not_valid = False  # Set not_valid flag to False to exit while loop
        try:
            user_sel = int(input("Please make a selection: "))
        except ValueError:  # Catch value errors if Int is not entered
            print("Please ensure you have entered a valid number")
        else:
            if user_sel == 1 or 2 or 3:
                generate_data(user_sel)
            elif user_sel == 4:
                print("Exiting...")
                sys.exit()  # Use sys module to exit program.
            else:
                print("Please enter within the range provided")
                not_valid = True  # If not valid, then set flag back to True


if __name__ == '__main__':
    main()
