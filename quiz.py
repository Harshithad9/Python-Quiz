# simple quiz game
# import os
# print("---------- Welcome to Online Computer Quiz!!! -----------")
# name = input("Enter your name..\n")
# print(f"Hello, {name}")
# play = input("Do you want to play? (yes/no) ➡️   ").strip().lower()
# if play == "yes":
#         os.system("clear" if os.name == "posix" else "cls")  
#         print("\n🎯 Awesome! Let's begin the quiz...\n")

# while play.lower() != "yes" :
#     quit()

# print("ohohh!! Let's play:)\n ")
# score = 0 

# print("QUESTIONS")
# print("---------")


# question0 = input("Which language is known as simplest and easy language to learn ?\n>>")
# if question0.lower() == "python":
#     print("---Correct---\n")
#     score = score  + 1
# else:
#     print("Ohh noo, it's wrong:( \n")


# question1 = input("What is CSS stands for ?\n>> ")
# if question1.lower() == "cascading style sheets":
#     print("---Correct---\n")
#     score += 1
# else:
#     print("Ohh noo, it's wrong:( \n")


# question2 = input("Is HTML a programming language ?\n>>")
# if question2.lower() == "no":
#     print("---Correct---\n")
#     score += 1
# else:
#     print("Ohh noo, it's wrong:( \n")


# question3 = input("Which is the most trending language in 2024 ?\n>> ")
# if question3.lower() == "javascript" or "js":
#     print("---Correct---\n")
#     score += 1
# else:
#     print("Ohh noo, it's wrong:( \n")


# question4 = input("Who developed C language ?\n>> ")
# if question4.lower() == "Dennis Ritchie":
#     print("---Correct---\n")
#     score += 1
# else:
#     print("Ohh noo, it's wrong:( \n")


# question5 = input("Which is the first operating system ?\n>> ")
# if question5.lower() == "general motors":
#     print("---Correct---\n")
#     score += 1
# else:
#     print("Ohh noo, it's wrong:( \n")

# question6 = input("Which keyword is used to come out of recursion ?\n>> ")
# if question6.lower() == "return":
#     print("---Correct---\n")
#     score += 1
# else:
#     print("Ohh noo, it's wrong:( \n")

# question7 = input("What is the maximum length of the filename in DOS ?\n>> ")
# if question7.lower() == "8" :
#     print("---Correct---\n")
#     score += 1
# else:
#     print("Ohh noo, it's wrong:( \n")

# question8 = input("What is the extension of the notepad ?\n>> ")
# if question8.lower() == ".txt":
#     print("---Correct---\n")
#     score += 1
# else:
#     print("Ohh noo, it's wrong:( \n")

# question9 = input("Which type of value does compareTo() returns _____ ?\n>> ")
# if question9.lower() == "int":
#     print("---Correct---\n")
#     score += 1
# else:
#     print("Ohh noo, it's wrong:( \n")

# question10 = input("What does AWT stands for ?\n>> ")
# if question10.lower() == "abstract window toolkit":
#     print("---Correct---\n")
#     score += 1
# else:
#     print("Ohh noo, it's wrong:( \n")

# question11 = input("A variable declared in a method is called as ?\n>> ")
# if question11.lower() == "local data":
#     print("---Correct---\n")
#     score += 1
# else:
#     print("Ohh noo, it's wrong:( \n")

# question12 = input("In C++, the index of the final element in as array is ?\n>> ")
# if question12.lower() == "0":
#     print("---Correct---\n")
#     score += 1
# else:
#     print("Ohh noo, it's wrong:( \n")

# question13 = input("Queue data strcture works on ?\n>> ")
# if question13.lower() == "FIFO" or "fifo":
#     print("---Correct---\n")
#     score += 1
# else:
#     print("Ohh noo, it's wrong:( \n")

# question14 = input("When a pop() operation is called on an empty queue, what is the condition called ?\n>> ")
# if question14.lower() == "underflow":
#     print("---Correct---\n")
#     score += 1
# else:
#     print("Ohh noo, it's wrong:( \n")

# print("Total score >> ",score)
# print("Thanks for playing.....")
# user_input= input("Do you want to play again??")
# while user_input.lower() != "yes" :
#     quit()
# print("Welcome back {name}")
# play = input("Do you want to play again? (yes/no) ➡️   ").strip().lower()
# if play != "yes":
#     print("Thanks for playing.See you next time!. 👋")
#     quit()
# if play == "yes":
#         os.system("clear" if os.name == "posix" else "cls")  
#         print("\n🎯 Awesome! Let's begin the quiz...\n")



# attractive quiz 
import os
import time

# Welcome message
print("✨🎉 Welcome to the Ultimate Computer Quiz! 🎉✨")
name = input("👤 Enter your name: ")
print(f"Hello, {name}! Ready to test your knowledge? 🤓")

# Ask if the user wants to play
play = input("Do you want to play? (yes/no) ➡️   ").strip().lower()
if play != "yes":
    print("No worries! Come back anytime. 👋")
    quit()
if play == "yes":
        os.system("clear" if os.name == "posix" else "cls")  
        print("\n🎯 Awesome! Let's begin the quiz...\n")

# Initialize score
score = 0

# Questions and answers dictionary
questions = {
    "Which language is known as the simplest and easiest to learn?": "python",
    "What does CSS stand for?": "cascading style sheets",
    "Is HTML a programming language? (yes/no)": "no",
    "Which is the most trending language in 2024?": ["javascript", "js"],
    "Who developed the C language?": "dennis ritchie",
    "Which was the first operating system?": "general motors",
    "Which keyword is used to come out of recursion?": "return",
    "What is the maximum length of a filename in DOS?": "8",
    "What is the file extension for Notepad?": ".txt",
    "What type of value does compareTo() return?": "int",
    "What does AWT stand for?": "abstract window toolkit",
    "A variable declared inside a method is called?": "local variable",
    "In C++, what is the index of the last element in an array?": "-1",
    "Queue data structure works on which principle?": ["fifo", "first in first out"],
    "When a pop() operation is called on an empty queue, what is the condition called?": "underflow"
}

# Iterate through questions
for question, answer in questions.items():
    print("\n📝 " + question)
    user_answer = input(">> ").strip().lower()

    # Check if the answer is correct
    if isinstance(answer, list):
        if user_answer in answer:
            print("✅ Correct!\n")
            score += 1
        else:
            print("❌ Wrong! The correct answer is:", answer[0], "\n")
    else:
        if user_answer == answer:
            print("✅ Correct!\n")
            score += 1
        else:
            print("❌ Wrong! The correct answer is:", answer, "\n")

    # Add a short delay for better user experience
    time.sleep(1)

# Display final score with a personalized message
print("\n🎯 QUIZ COMPLETED 🎯")
print(f"Your final score is: {score}/{len(questions)}")

if score == len(questions):
    print("🏆 Amazing! You got a perfect score! Genius level! 🤩")
elif score >= len(questions) * 0.7:
    print("👏 Great job! You're quite knowledgeable! 🚀")
elif score >= len(questions) * 0.4:
    print("🙂 Not bad! Keep learning and improving! 📚")
else:
    print("😔 Don't worry! Try again and you'll do better next time! 🔄")

# Ask if the user wants to play again
while True:
    retry = input("\n🔄 Do you want to play again? (yes/no) ➡️   ").strip().lower()
    if retry == "yes":
        os.system("clear" if os.name == "posix" else "cls")  
        print("\n🔄 Restarting the quiz... 🚀\n")
        time.sleep(1)
        os.system("python " + __file__)  
        quit()
    elif retry == "no":
        print("👋 Thanks for playing, see you next time! 🎮")
        break
    else:
        print("❓ Please type 'yes' or 'no'.")
