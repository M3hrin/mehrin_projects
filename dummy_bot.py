Password=1234
user_pass=int(input("Enter password: "))
while user_pass!=Password:
    print("Wrong password, try again.")
    user_pass=int(input("Enter password: "))

print("Access granted.")
username = input("Hello user, enter your name:")
print(f"Welcome to the system {username}. I'm Axis, your virtual assistant!")
user_task = ["Check the weather","Set a reminder","Play music","Tell a joke"]
while True:
    task = input(f"Which of these would you like me to help you with? {user_task})")
    if task.lower() == "check the weather":
        print("The weather is sunny with a high of 25 degrees Celsius.")
    elif task.lower() == "set a reminder":
        reminder = input("What would you like to be reminded about?")
        print(f"Reminder set for: {reminder}")
    elif task.lower() == "play music":
        print("Playing your favorite music playlist....")
    elif task.lower() == "tell a joke":
        print("Here's a joke for you: Why don't scientists trust atoms? Because they make up everything!")
    elif task.lower()=="exit":
        exitt=input("Do you want to exit? (yes/no)")
        if exitt.lower()=="yes":
            print("Goodbye!")
            break
        elif exitt.lower()=="no":
            continue
        else:
            print("Invalid input, please enter 'yes' or 'no'.")   
            break
    else:
        print("Sorry, this task is not under my capabilities yet. Please choose from the list.if you want to exit, type 'exit'.") 
    




