1.import json

with open("students.json", "r", encoding="utf-8") as file:
    students = json.load(file)

for student in students:
    print("ID:", student["id"])
    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Major:", student["major"])
    print("-" * 20)
2.import requests

api_key = "YOUR_API_KEY"
city = "Tashkent"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Weather:", data["weather"][0]["description"])
else:
    print("Error fetching data")
3.import json

FILE = "books.json"

def load_books():
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_books(books):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(books, f, indent=4)

def add_book():
    books = load_books()
    new_book = {
        "id": int(input("ID: ")),
        "title": input("Title: "),
        "author": input("Author: ")
    }
    books.append(new_book)
    save_books(books)

def update_book():
    books = load_books()
    book_id = int(input("Enter book ID to update: "))
    for book in books:
        if book["id"] == book_id:
            book["title"] = input("New title: ")
            book["author"] = input("New author: ")
            save_books(books)
            return
    print("Book not found")

def delete_book():
    books = load_books()
    book_id = int(input("Enter book ID to delete: "))
    books = [book for book in books if book["id"] != book_id]
    save_books(books)

print("1. Add Book")
print("2. Update Book")
print("3. Delete Book")

choice = input("Choose: ")

if choice == "1":
    add_book()
elif choice == "2":
    update_book()
elif choice == "3":
    delete_book()
else:
    print("Invalid choice")
4.import requests
import random

api_key = "YOUR_API_KEY"
genre = input("Enter movie genre (Action, Comedy, Drama): ")

search_url = f"http://www.omdbapi.com/?apikey={api_key}&s={genre}&type=movie"
response = requests.get(search_url)
data = response.json()

if data["Response"] == "True":
    movies = data["Search"]
    movie = random.choice(movies)

    movie_id = movie["imdbID"]
    details_url = f"http://www.omdbapi.com/?apikey={api_key}&i={movie_id}"
    details = requests.get(details_url).json()

    print("🎬 Movie Recommendation")
    print("Title:", details["Title"])
    print("Year:", details["Year"])
    print("Genre:", details["Genre"])
    print("Plot:", details["Plot"])
else:
    print("No movies found for this genre")
