# Program Name: Assignment1.py
# Course: IT3883 / Section W02
# Student Name: Tamia Jackson
# Assignment Number: Assignment 1
# Due Date: 01/28/2026
# Purpose: This program shows a text-based menu that lets the user append text to an input buffer, clear the buffer, display the buffer, or exit.
# Resources Used: Class notes 

# variable to save user input
input_buffer = ""

# loop keeps the program running until the user exits
while True:
    print("\nMenu Options:")
    print("1. Append data to the input buffer")
    print("2. Clear the input buffer")
    print("3. Display the input buffer")
    print("4. Exit the program")

    # user's menu choice
    choice = input("Enter your choice (1-4): ")

    # append text
    if choice == "1":
        user_text = input("Enter text to add: ")
        input_buffer += user_text
        print("Text added to buffer.")

    # clear buffer
    elif choice == "2":
        input_buffer = ""
        print("Input buffer cleared.")

    # display buffer
    elif choice == "3":
        print("Current buffer contents:")
        print(input_buffer)

    # exit program
    elif choice == "4":
        print("Exiting program. Goodbye!")
        break

    # invalid menu choices
    else:
        print("Invalid choice. Please select a number between 1 and 4.")
