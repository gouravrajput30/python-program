def greet_birthday(name):
    return f"Happy Birthday, {name}"
def greet_morning(name):
    return f"Good Morning, {name}"
def greet_evening(name):
    return f"Good Morning, {name}"
def greet_night(name):

    return f"Good Night, {name}"
def legend(name):
    return f"JAM KE PADHAI KAR {name} BETA ji !!!"

def main():
    print("Choose a greeting type:")
    print("1. Happy Birthday")
    print("2. Good Morning")
    print("3. Good Evening")
    print("4. Good Night")
    print("5. LEGEND")

    choice = input("Enter your choice (1, 2, 3 ,4 or 5): ")

    if choice == '1':
        name = input("Enter the birthday person's name: ")
        greeting_message = greet_birthday(name)
    elif choice == '2':
        name = input("Enter your name: ")
        greeting_message = greet_morning(name)
    elif choice =='3' :
        name = input("Enter your name: ")
        greeting_message = greet_evening(name)
    elif choice == '4':
        name = input("Enter your name: ")
        greeting_message = greet_night(name)
    elif choice == '5':
        name = input("Enter your name: ")
        greeting_message = legend(name)
    else:
        greeting_message = "Invalid choice. Please enter 1, 2, 3,4 or 5."

    print(greeting_message)

if __name__ == "__main__":
    main()
