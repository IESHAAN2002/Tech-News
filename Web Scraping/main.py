import requests
from bs4 import BeautifulSoup

# def SaveDataToFile(url,path):
#     r = requests.get(url)
#     r.encoding = 'utf-8'
#     with open(path,'w',encoding='utf-8') as f:
#         f.write(r.text)

url = "https://timesofindia.indiatimes.com/?from=mdr"

# SaveDataToFile(url, "data/times.html")
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

soup=BeautifulSoup(htmlContent,'html.parser')
# print(soup.prettify())

# Commonly used types of objects:
# 1. Tag
# 2. NavigableString
# 3. BeautifulSoup
# 4. Comment

# titel of HTML page
title = soup.title
# print(type(title))
# print(type(soup))
# print(type(title.string))

# print(soup.find_all('p'))
# print(soup.find('p').get_text().prettify)

print(soup.get_text())
