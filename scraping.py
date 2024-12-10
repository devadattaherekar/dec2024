import requests
from bs4 import BeautifulSoup

response=requests.get("https://quotes.toscrape.com/")
html_text=response.text
#print(html_text)

soup=BeautifulSoup(html_text,'html.parser')
#print(dir(soup))
#print(soup)
with open("myfavquotes.txt","w") as fp:
     for each_tag in soup.find_all('span',{"class":"text"}):
         print(each_tag.text)
         fp.write(each_tag.text+"\n")

with open("myfavauthors.txt","w") as fp:
    for each_tag in soup.find_all('small',{"class":"author"}):
        print(each_tag.text)
        fp.write(each_tag.text+"\n")

