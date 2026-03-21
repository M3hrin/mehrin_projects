print("Welcome to the quiz! Let's get started.")
def quiz():
    score=0
    answer1=input("What is the capital of France? ")
    if answer1.lower()=="paris":
        print("Correct!")
        score+=1
    else:
        print("Incorrect. The correct answer is Paris.")
        score-=1
    answer2=input("What is the largest planet in our solar system? ")
    if answer2.lower()=="jupiter":
        print("Correct!")
        score+=1
    else:
        print("Incorrect. The correct answer is Jupiter.")
        score-=1
    answer3=input("What is the chemical symbol for gold? ")
    if answer3.lower()=="au":
        print("Correct!")
        score+=1
    else:
        print("Incorrect. The correct answer is Au.")
        score-=1

    print(f"Your final score is: {score} out of 3.")
    if score==3:
        print("Excellent work! You got all the answers right!")
    elif score==2:
        print("Good job! You got 2 out of 3 correct.")
    elif score==1:
        print("Not bad! You got 1 out of 3 correct.")
    elif score<=0:
        print("You suck at this quiz.")
    if score<0:
        again=input("You have a negative score, would you like to try again?")
        if again.lower()=="yes":
            score=0
            print("Let's try again!")
            answer1=input("What is the capital of France? ")
            if answer1.lower()=="paris":
                print("Correct!")
                score+=1
            else:
                print("Incorrect. The correct answer is Paris.")
            score-=1
            answer2=input("What is the largest planet in our solar system? ")
            if answer2.lower()=="jupiter":
                print("Correct!")
                score+=1
            else:
                print("Incorrect. The correct answer is Jupiter.")
                score-=1
            answer3=input("What is the chemical symbol for gold? ")
            if answer3.lower()=="au":
                print("Correct!")
                score+=1
            else:
                print("Incorrect. The correct answer is Au.")
                score-=1

            print(f"Your final score is: {score} out of 3.")
        if again.lower()=="no":
            print("Thanks for playing! Goodbye!")
    repeat=input("Would you like to take the quiz again?")
    if repeat.lower()=="yes":
        quiz()
    elif repeat.lower()=="no":
        print("Thanks for playing! Goodbye!")

quiz()