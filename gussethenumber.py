import random
import pyttsx3

engine=pyttsx3.init()

engine.say("Hello, what's your names")
engine.runAndWait()


names=input("Enter you name : ")

print("well,", names ,",I am thinking of a number between 1 to 50")
engine.say(f"well,{names},I am thinking of a number between 1 to 50")
engine.runAndWait()

secretnumber=random.randint(1,50)

for numbertaken in range(1,8):
    print("Take a guess")
    engine.say("Take a guess")
    
    try:
        gussed=int(input("your guess : "))
    except ValueError:
        engine.say("Please enter a number")
        engine.runAndWait()
        continue


    if gussed < secretnumber:
        print("That's too low")
        engine.say("That's too low")
    elif gussed > secretnumber:
        print("That's too high")
        engine.say("That's too high")
    else:
        break
    engine.runAndWait()


if gussed == secretnumber:
    print("Ohh ," + names + ", you guess the right number",str(secretnumber))
    engine.say("Congratulations you guessed the right answer")
else:
    print("Nope. The number i was thinking is ",str(secretnumber))
    engine.say("Sorry, you did not gussed the right number")
engine.runAndWait()
