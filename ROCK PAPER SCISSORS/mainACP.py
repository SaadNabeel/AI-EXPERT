import random
from colorama import init, Fore, Style

init(autoreset=True)

def get_player_choice():

    choice = ""

    while choice not in ["rock", "paper", "scissors"]:

        choice = input(
            Fore.GREEN + "Choose Rock, Paper, or Scissors: " + Style.RESET_ALL
        ).lower()

        if choice not in ["rock", "paper", "scissors"]:
            print(Fore.RED + "Invalid choice. Try again.")

    return choice

def ai_choice(player_history):

    if not player_history:
        return random.choice(["rock", "paper", "scissors"])

    last_move = player_history[-1]

    if last_move == "rock":
        return "paper"

    elif last_move == "paper":
        return "scissors"

    else:
        return "rock"

def decide_winner(player, ai):

    if player == ai:
        return "tie"

    if (
        (player == "rock" and ai == "scissors")
        or (player == "paper" and ai == "rock")
        or (player == "scissors" and ai == "paper")
    ):
        return "player"

    return "ai"

def play_game():

    print(Fore.CYAN + "Welcome to Rock Paper Scissors!")

    name = input(Fore.GREEN + "Enter your name: " + Style.RESET_ALL)

    player_score = 0
    ai_score = 0
    player_history = []

    while True:

        print()
        print(Fore.YELLOW + f"Score -> {name}: {player_score} | AI: {ai_score}")

        player = get_player_choice()

        ai = ai_choice(player_history)

        print(Fore.BLUE + f"AI chose: {ai}")

        result = decide_winner(player, ai)

        if result == "player":

            print(Fore.GREEN + f"{name} wins this round!")
            player_score += 1

        elif result == "ai":

            print(Fore.RED + "AI wins this round!")
            ai_score += 1

        else:

            print(Fore.YELLOW + "It's a tie!")

        player_history.append(player)

        play_again = input(
            Fore.CYAN + "Play another round? (yes/no): " + Style.RESET_ALL
        ).lower()

        if play_again != "yes":

            print()
            print(Fore.CYAN + "===== FINAL SCORE =====")
            print(f"{name}: {player_score}")
            print(f"AI: {ai_score}")

            if player_score > ai_score:
                print(Fore.GREEN + f"Congratulations, {name}! You won!")
            elif ai_score > player_score:
                print(Fore.RED + "The AI wins the game!")
            else:
                print(Fore.YELLOW + "The game ended in a tie!")

            print(Fore.CYAN + "Thanks for playing!")
            break

if __name__ == "__main__":

    play_game()