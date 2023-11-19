from bs4 import BeautifulSoup
#import lxml

with open('website.html','r',encoding='utf-8') as file:
    contents = file.read()

soup = BeautifulSoup(contents,'html.parser')

xx = soup.find_all('li')
#[print(x.text) for x in xx]

#get heading by name(type --> h1 or h3 and so on) and id
heading = soup.find(name='h1', id='name')
#print(heading)

heading2 = soup.find(name='h3', class_='heading')
#print(heading2)

#find an anchor tag inside the paragraph tag
# in css can write as
#  p a{
    #color:red;
# }

pa_anchor = soup.select(selector='p a')
print(pa_anchor)

## can use soup.select also to find an id or class
                            #.heading
                            #  (#name)
id2 = soup.select(selector='#name')
print(id2)

id2 = soup.select(selector='.heading')
print(id2)