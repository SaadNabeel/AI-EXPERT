print("Hello! Welcome to the AI Chatbot.")
name = input("What is your name? ")
print("Nice to meet you,", name)

feeling = input("Are you feeling good or bad today? ").lower()
if feeling == "good":
    print("I'm glad you're having a good day.")
elif feeling == "bad":
    print("I'm sorry to hear that")
else:
    print("We all cannot share our feelings ,it is okay")

bye = input("Write bye to exit: ").lower()

if bye == "bye":
    print("Goodbye,have a good day", name)