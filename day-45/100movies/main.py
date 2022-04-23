from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
demo = response.text

soup = BeautifulSoup(demo, "html.parser")
movies = soup.find_all("h3", class_='title')

for i in movies:
    print(i.text)