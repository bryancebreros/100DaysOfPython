from bs4 import BeautifulSoup

with open("website.html", encoding='cp850') as file:
    content = file.read()

soup = BeautifulSoup(content, 'html.parser')

print(soup.prettify())

# soup.findall(name="a") CAN LOOP
