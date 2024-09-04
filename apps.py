import os

FILE_PATH = "atm_data.txt"


def read_data():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            lines = file.readlines()
            if len(lines) == 2:
                stored_pin = lines[0].strip()
                balance = float(lines[1].strip())
                return stored_pin, balance
    return None, 100000.00


def write_data(pin, balance):
    with open(FILE_PATH, 'w') as file:
        file.write(f"User's pin = {pin} \nUser's balance = ₦{balance}")


def create_new_pin():
    global stored_pin
    user_pin = input("\nEnter your new 4-digit PIN> ")
    stored_pin = user_pin
    write_data(stored_pin, balance)
    print("Your new PIN has been saved!")


def enter_existing_pin():
    global stored_pin
    pin = input("\nEnter your existing 4-digit PIN> ")
    if pin == stored_pin:
        print("PIN is correct!")
        return True
    else:
        pin_count = 0
        pin_limit = 3
        while pin_count < pin_limit:
            print(f"Wrong PIN! You have {pin_limit - pin_count - 1} attempt(s) left")
            pin_count += 1
            if pin_count == pin_limit:
                print("Your card has been blocked!")
                exit(1)
            retried_pin = input()
            if retried_pin == stored_pin:
                print("PIN is correct!")
                return True
        return False


def check_balance():
    global balance
    print(f"Your balance is ₦{balance}")


def withdraw_money():
    global balance
    withdraw_amount = float(input("How much do you want to withdraw?> "))
    if withdraw_amount > balance:
        print("Insufficient Funds!")
    else:
        balance -= withdraw_amount
        write_data(stored_pin, balance)
        print(f"You have successfully withdrawn ₦{withdraw_amount}")
        print(f"Your new balance is ₦{balance}")


# Main code
input('Please insert your card and "Press Enter"')

stored_pin, balance = read_data()

while True:
    if not stored_pin:
        create_new_pin()
    else:
        option = input("""\nChoose Option: 
    >To change your PIN "Press 1" 
    >To enter existing PIN "Press 2"
    """)

        if option == "1":
            # Allow the user to change their PIN
            current_pin = input("Please enter your current 4-digit PIN> ")
            if current_pin == stored_pin:
                create_new_pin()
            else:
                print("Incorrect PIN. You cannot change the PIN without entering the correct one.")
            continue

        elif option == "2":
            if enter_existing_pin():
                break
        else:
            print("Invalid option! Try again \n")

while True:
    transaction_option = input("""\nChoose Option:
    >To check balance "Press 3"
    >To withdraw money "Press 4"
    """)
    if transaction_option == "3":
        check_balance()
    elif transaction_option == "4":
        withdraw_money()
    else:
        print("Invalid option! Try again")

    continuation_option = input("""\nChoose Option:
    >To perform more transactions "Press 5"
    >To exit "Press 6"
    """)
    if continuation_option == "5":
        continue
    elif continuation_option == "6":
        print("Thank you for banking with us!")
        exit(1)
    else:
        print("Invalid option! Try again")
