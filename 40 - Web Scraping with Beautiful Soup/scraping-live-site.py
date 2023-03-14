from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
articles = soup.select("span.titleline > a")

article_texts = []
article_links = []

for article in articles:
    text = article.getText()
    article_texts.append(text)
    link = article.get("href")
    article_links.append(link)

up_votes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_num = max(up_votes)
index = up_votes.index(largest_num)

print(largest_num)
print(article_texts[index])
print(article_links[index])
# print(up_votes)

