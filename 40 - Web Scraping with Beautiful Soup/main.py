# **** Beautiful Soup Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/ **** #
from bs4 import BeautifulSoup
import lxml

with open("website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# soup = BeautifulSoup(contents, "lxml") <-- for lxml web sites, must import lxml module

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())

# returns a list of all anchor tags
anchor_tags = soup.find_all(name="a")
# print(anchor_tags)

for tag in anchor_tags:
    # print(tag.text)
    # print(tag.get("href"))
    pass

heading = soup.find(name="h1", id="name")
# print(heading)

h3 = soup.find(name="h3", class_="heading")
# print(h3)

# css selector
company_url = soup.select_one(selector="p a")
print(company_url.get("href"))

# select h1 with id = name
h1_name = soup.select_one(selector="#name")
print(h1_name)

# selects all elements with the class of "heading"
print(soup.select(".heading"))