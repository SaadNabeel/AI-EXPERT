print("Hello! Welcome to the AI Chatbot.")

name = input("What is your name? ")

if name == "":
    print("You didn't tell me your name.")
else:
    print("Nice to meet you,", name)

feeling = input("Are you feeling good or bad today? ").lower()

if feeling == "good":
    print("That's great! I'm glad you're having a good day.")

elif feeling == "bad":
    print("I'm sorry to hear that.")
    print("I hope things get better soon.")

elif feeling == "":
    print("We all can't share our feelings. It's okay.")

else:
    print("I only understand 'good' or 'bad'.")

bye = input("Type bye to exit: ").lower()

if bye == "bye":
    print("Goodbye!")
else:
    print("You didn't type bye, but the chatbot is closing anyway.")