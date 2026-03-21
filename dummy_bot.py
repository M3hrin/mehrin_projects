Password=201012
user_pass=int(input("Enter password: "))
while user_pass!=Password:
    print("Wrong password, try again.")
    user_pass=int(input("Enter password: "))

print("Access granted.")
username=input("Hello user, enter your name:")
user_task=["Check the weather","Set a reminder","Play music","Tell a joke"]    
task=input(f"Welcome to the system {username}. I'm Axis, your virtual assistant! Which of these would you like me to help you with? {user_task})")
if task=="1":
    print("The weather is sunny with a high of 25 degrees Celsius.")
elif task=="2":
    reminder=input("What would you like to be reminded about?")
    print(f"Reminder set for: {reminder}")
elif task=="3":
    print("Playing your favorite music playlist....")
elif task=="4":
    print("Here's a joke for you: Why don't scientists trust atoms? Because they make up everything!")
else:
    ("Sorry, I didn't understand that task. Please choose from the list.")


