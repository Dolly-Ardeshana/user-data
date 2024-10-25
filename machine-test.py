import pandas as pd
import os
import re

file_name = "user_data.xlsx"

def validate_name(name):
    if re.match("^[A-Za-z ]+$", name):
        return True
    print("Invalid name. Only alphabetic characters and spaces are allowed.")
    return False

def validate_email(email):
    if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
        return True
    print("Invalid email format. Please enter a valid email address.")
    return False

def validate_phone(phone):
    if re.match("^\d{10}$", phone):
        return True
    print("Invalid phone number. Please enter a 10-digit phone number.")
    return False

def get_valid_input(prompt, validation_func):
    while True:
        user_input = input(prompt)
        if validation_func(user_input):
            return user_input

def add_user():
    name = get_valid_input("Enter Name: ", validate_name)
    email = get_valid_input("Enter Email: ", validate_email)
    phone = get_valid_input("Enter Phone Number: ", validate_phone)

    new_user = pd.DataFrame([[name, email, phone]], columns=['Name', 'Email', 'Phone Number'])
    
    if os.path.exists(file_name):
        df = pd.read_excel(file_name)
        df = pd.concat([df, new_user], ignore_index=True)
    else:
        df = new_user

    df.to_excel(file_name, index=False)
    print("User added successfully!")


def display_users():
    if os.path.exists(file_name):
        df = pd.read_excel(file_name)
        if df.empty:
            print("No users found.")
        else:
            print("User Data:\n", df)
    else:
        print("No user data found. Add users to see them here.")

def main():
    while True:
        print("\nMake a choice to proceed:-")
        print("Press '1' to Add user.")
        print("Press '2' to Display users.")
        print("Press '3' to Exit.")
        
        choice = input("Press any key to continue: ")
        
        if choice == '1':
            add_user()
        elif choice == '2':
            display_users()
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
