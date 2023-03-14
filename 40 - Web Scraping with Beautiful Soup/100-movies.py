from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)

webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")
movies = [movie.getText() for movie in soup.find_all(name="h3", class_="title")]
movies.reverse()

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")