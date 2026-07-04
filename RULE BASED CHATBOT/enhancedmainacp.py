import re
import random
from colorama import Fore, init

init(autoreset=True)

destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"]
}

jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!"
]

facts = [
    "Japan has over 6,000 islands.",
    "The Maldives consists of about 1,200 islands.",
    "Paris is known as the City of Light."
]

message_count = 0

def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

def recommend():

    print(Fore.CYAN + "TravelBot: Beaches, mountains, or cities?")

    preference = input(Fore.YELLOW + "You: ")
    preference = normalize_input(preference)

    if preference in destinations:

        suggestion = random.choice(destinations[preference])

        print(Fore.GREEN + f"TravelBot: How about {suggestion}?")

        print(Fore.CYAN + "TravelBot: Do you like it? (yes/no)")

        answer = input(Fore.YELLOW + "You: ").lower()

        if answer == "yes":

            print(Fore.GREEN + f"TravelBot: Awesome! Enjoy {suggestion}!")

        elif answer == "no":

            print(Fore.RED + "TravelBot: Let's try another.")
            recommend()

        else:

            print(Fore.RED + "TravelBot: I'll suggest again.")
            recommend()

    else:

        print(Fore.RED + "TravelBot: Sorry, I don't have that type of destination.")

def packing_tips():

    print(Fore.CYAN + "TravelBot: Where to?")

    location = normalize_input(input(Fore.YELLOW + "You: "))

    print(Fore.CYAN + "TravelBot: How many days?")

    days = input(Fore.YELLOW + "You: ")

    print(Fore.GREEN + f"TravelBot: Packing tips for {days} days in {location}:")

    print("- Pack comfortable clothes")
    print("- Carry important documents")
    print("- Take a phone charger")
    print("- Pack medicines if needed")

def tell_joke():

    print(Fore.GREEN + "TravelBot: " + random.choice(jokes))

def travel_fact():

    print(Fore.GREEN + "TravelBot: " + random.choice(facts))

def show_help():

    print(Fore.MAGENTA + "\nI can:")

    print(Fore.GREEN + "- Suggest travel spots (say 'recommendation')")
    print(Fore.GREEN + "- Offer packing tips (say 'packing')")
    print(Fore.GREEN + "- Tell a joke (say 'joke')")
    print(Fore.GREEN + "- Share a travel fact (say 'fact')")

    print(Fore.CYAN + "Type 'exit' or 'bye' to end.\n")

def chat():

    global message_count

    print(Fore.CYAN + "Hello! I'm TravelBot.")

    name = input(Fore.YELLOW + "Your name? ")

    print(Fore.GREEN + f"Nice to meet you, {name}!")

    show_help()

    while True:

        user_input = input(Fore.YELLOW + f"{name}: ")

        user_input = normalize_input(user_input)

        message_count += 1

        if "hello" in user_input or "hi" in user_input:

            print(Fore.GREEN + f"TravelBot: Hello, {name}!")

        elif "recommend" in user_input or "suggest" in user_input or "travel" in user_input:

            recommend()

        elif "pack" in user_input or "packing" in user_input:

            packing_tips()

        elif "joke" in user_input or "funny" in user_input:

            tell_joke()

        elif "fact" in user_input:

            travel_fact()

        elif "help" in user_input:

            show_help()

        elif "exit" in user_input or "bye" in user_input:

            print(Fore.CYAN + f"TravelBot: Thanks for chatting, {name}!")
            print(Fore.CYAN + f"Messages exchanged: {message_count}")
            print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!")
            break

        else:

            print(Fore.RED + "TravelBot: Could you rephrase?")

if __name__ == "__main__":

    chat()