import random
import time
import pandas as pd
from textblob import TextBlob
from colorama import init, Fore

init(autoreset=True)

try:
    df = pd.read_csv("imdb_top_1000.csv")
except FileNotFoundError:
    print(Fore.RED + "Error: imdb_top_1000.csv not found.")
    raise SystemExit

df["Genre"] = df["Genre"].fillna("")
df["Overview"] = df["Overview"].fillna("")

def sentiment(pol):

    if pol > 0.2:
        return "Positive"

    elif pol < -0.2:
        return "Negative"

    else:
        return "Neutral"

def ai_recommend(genre="", rating=0):

    movies = []

    for _, row in df.iterrows():

        if genre and genre.lower() not in row["Genre"].lower():
            continue

        if row["IMDB_Rating"] < rating:
            continue

        pol = TextBlob(row["Overview"]).sentiment.polarity

        movies.append((
            row["Series_Title"],
            row["Genre"],
            row["IMDB_Rating"],
            pol
        ))

    return movies[:5]

def random_recommend():

    row = df.sample(1).iloc[0]

    pol = TextBlob(row["Overview"]).sentiment.polarity

    return (
        row["Series_Title"],
        row["Genre"],
        row["IMDB_Rating"],
        pol
    )

def show_movie(movie):

    title, genre, rating, pol = movie

    print(Fore.CYAN + "\nMovie Recommendation")
    print("Title:", title)
    print("Genre:", genre)
    print("IMDb Rating:", rating)
    print("Sentiment:", sentiment(pol))
    print("Polarity:", round(pol, 2))

print(Fore.GREEN + "=== Movie Recommendation System ===")

name = input("Enter your name: ")

while True:

    print("\n1. AI Recommendation")
    print("2. Random Recommendation")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == "1":

        genre = input("Preferred Genre: ")
        rating = float(input("Minimum IMDb Rating: "))

        print(Fore.YELLOW + "\nFinding movies...")
        time.sleep(1)

        movies = ai_recommend(genre, rating)

        if len(movies) == 0:

            print(Fore.RED + "No movies found.")

        else:

            print(Fore.YELLOW + f"\nTop Picks For {name}")

            for movie in movies:

                show_movie(movie)

    elif choice == "2":

        print(Fore.YELLOW + "\nPicking a random movie...")
        time.sleep(1)

        movie = random_recommend()

        show_movie(movie)

    elif choice == "3":

        print(Fore.GREEN + f"Goodbye, {name}!")
        break

    else:

        print(Fore.RED + "Invalid choice.")