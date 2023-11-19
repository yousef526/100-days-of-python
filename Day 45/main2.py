from bs4 import BeautifulSoup
import requests

ss = requests.get(url="https://news.ycombinator.com/news")
#print(ss.raise_for_status())

soup = BeautifulSoup(ss.text,'html.parser')


## soup.find()  to get the first instance only of specified element

# to give the html page that i grabbed html shape must use prettify()
""" links = soup.find_all(class_='titleline')

print(links[0].text) """
#[print(x.text) for x in links]

anchor_tags = soup.find_all(name='span',class_='titleline')
article_links = []
article_texts = []
#print(anchor_tag)
for anchor_tag in anchor_tags:
    text = anchor_tag.a.text
    article_texts.append(text)

    link = anchor_tag.a['href']
    article_links.append(link)

upvotes = [x.text for x in soup.find_all(name='span',class_="score")]
article_upvote = [int(x.split()[0]) for x in upvotes]

""" print(article_texts)
print("SPACE")
print(article_links)
print("SPACE")
print(article_upvote.index()) """

index_biggest = article_upvote.index(max(article_upvote))
print(article_texts[index_biggest])
print(article_links[index_biggest])
print(article_upvote)
print(max(article_upvote))