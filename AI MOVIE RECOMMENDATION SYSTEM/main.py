import time
import pandas as pd
from textblob import TextBlob
from colorama import init, Fore

init(autoreset=True)

try:
    df = pd.read_csv("imdb_top_1000.csv")
except FileNotFoundError:
    print(Fore.RED + "Error: The file 'imdb_top_1000.csv' was not found.")
    raise SystemExit

df["Genre"] = df["Genre"].fillna("")
df["Overview"] = df["Overview"].fillna("")

def senti(pol):
    if pol > 0.2:
        return "Positive"
    elif pol < -0.2:
        return "Negative"
    else:
        return "Neutral"

def recommend(genre=None, mood="neutral", rating=0, n=5):

    out = []

    for _, r in df.sort_values("IMDB_Rating", ascending=False).iterrows():

        genres = [g.strip().lower() for g in r["Genre"].split(",")]

        if genre and genre.lower() not in genres:
            continue

        if r["IMDB_Rating"] < rating:
            continue

        pol = TextBlob(r["Overview"]).sentiment.polarity

        if mood == "positive" and pol < 0:
            continue

        if mood == "negative" and pol > 0:
            continue

        out.append((r["Series_Title"], pol))

        if len(out) == n:
            break

    return out if out else "No suitable movie recommendations found."

def show(recs, name):

    print(Fore.YELLOW + f"\nAI-Analyzed Movie Recommendations for {name}:")

    for i, (title, polarity) in enumerate(recs, 1):

        print(
            f"{Fore.CYAN}{i}. {title} "
            f"(Polarity: {polarity:.2f}, {senti(polarity)})"
        )

print(Fore.GREEN + "Welcome to the AI Movie Recommendation System!")

name = input("Enter your name: ")

while True:

    genre = input("\nPreferred genre: ").strip().lower()

    mood = input(
        "Mood (positive/negative/neutral): "
    ).strip().lower()

    try:
        rating = float(input("Minimum IMDb rating (0-10): "))
    except ValueError:
        rating = 0

    print(Fore.YELLOW + "\nAnalyzing movies...")
    time.sleep(1)

    recs = recommend(
        genre=genre,
        mood=mood,
        rating=rating,
        n=5
    )

    if isinstance(recs, str):
        print(Fore.RED + recs)
    else:
        show(recs, name)

    a = input(
        "\nWould you like more recommendations? (yes/no): "
    ).strip().lower()

    if a == "no":
        print(Fore.GREEN + f"\nEnjoy your movie picks, {name}!\n")
        break

    elif a != "yes":
        print(Fore.RED + "Invalid choice. Exiting.")
        break