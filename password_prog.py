password=2468
count=0
guess=int(input("Enter the password: "))
for i in range(2):
    if guess==password:
        print("Access granted.")
        break
    else:
        print("Wrong password, try again.")
        guess=int(input("Enter the password: "))
        count+=1
def stop():
    if count==2:
        print("Too many attempts. Access denied.")
stop()