import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)

soup = BeautifulSoup(response.text,'html.parser')

movies = soup.find_all(name='h3',class_="title")

movies_title = []

i = len(movies) - 1

while i >= 0:
    movies_title.append(movies[i].getText())
    i-=1

with open("movie.txt","w",encoding="utf-8") as file:
    for movie in  movies_title:
        file.write(movie+"\n")