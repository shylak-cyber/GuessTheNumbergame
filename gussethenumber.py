import random
import pyttsx3

engine=pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def play_game():
    speak("Welcome To the Game,  Hello , What is your name ?. ")
    name=input("Enter you name : ")

    print(f"\n Welcome {name}")
    speak(f"Welcome, {name}")

#user can choos the difficulty level
    print("\nChosse difficulty:")
    print("1. Easy (1 to 20)")
    print("2. Medium (1 to 50)")
    print("3. Hard (1 to 100)")

    choice=input("Enter your diffuculty level (1/2/3)")

    if choice == "1":
        max_num=20
        attempts =7
    elif choice=="3":
        max_num=100
        attempts=3
    else:
        max_num=50
        attempts=5


    secretnumber=random.randint(1,max_num)
    
    speak(f"I am thinking of a number between 1 and {max_num}")

    for attempts in range(1, attempts+1):
        print(f"\nAttempts {attempts} of {attempts}")
        speak("Take , a guess")
    
        try:
            gussed=int(input("your guess : "))
        except ValueError:
            print("Please enter a number")
            speak("Please enter a number")
            continue


        if gussed < secretnumber:
            print("That's too low")
            speak("That's too low")
        elif gussed > secretnumber:
            print("That's too high")
            speak("That's too high")
        else:
            print(f"Congratulations {name}! You gussed the right number")
            speak("congratulation , you gussed right number")
            return
        
    print(f"\nX Sorry{name}, the number was{secretnumber}")
    speak("Soory , you tried well")

while True:
    play_game()
    again=input("Do you want to play again(Yes/No)").lower()
    if again != "yes":
        speak("Thankyou for playing, Good bye")
        break    

