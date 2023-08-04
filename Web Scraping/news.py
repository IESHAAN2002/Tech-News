import requests
from bs4 import BeautifulSoup

def SaveDataToFile(url,path):
    r = requests.get(url)
    r.encoding = 'utf-8'
    with open(path,'w',encoding='utf-8') as f:
        f.write(r.text)


def main():
    print("Welcome to Technology News \n")
    print("We will be providing you Latest Tech news as per your interest \n")

    print("Options here are the options from which you can choose your interest and we will bring you the news \n")
    userList = []
    UserInterest(userList)
    url1 = "https://www.thehindu.com/sci-tech/technology/"
    url2 = "https://indianexpress.com/section/technology/"
    url3 = "https://www.gadgetsnow.com/tech-news"

    SaveDataToFile(url1, "data\hinduTech.html")
    SaveDataToFile(url2, "data\indianExpressTech.html")
    SaveDataToFile(url3, "data\TOItech.html")

    news = []

    hindu_news  = fetch_news("data\hinduTech.html")
    indianExpress_news = fetch_news("data\indianExpressTech.html")
    TOI_news = fetch_news("data\TOItech.html")

    hindu_final=filtering_news_from_hindu(hindu_news,userList)
    indian_final=filtering_news_from_indian(indianExpress_news, userList)
    TOI_final=filtering_news_from_TOI(TOI_news, userList)

    news.extend(hindu_final)
    news.extend(indian_final)
    news.extend(TOI_final)

    sorted_news = sort_news(news)

    display_news(sorted_news)

def UserInterest(userList):
    print("Enter the KEYWORDS in which you are interested in \n")
    print("To exit form creating ths list enter exit\n")
    flag=True
    while(flag):
        KeyWords = input("Enter KeyWord\n")
        if(KeyWords=="exit" or KeyWords=="Exit"):
            break
        else: 
            userList.append(KeyWords)

def fetch_news(path):
    with open(path,'r',encoding='utf-8') as f:
        data = f.read()
    newsdata = BeautifulSoup(data,'html.parser')
    return newsdata

def filtering_news_from_hindu(news,userList):
    User_news = []
    if isinstance(news, BeautifulSoup):
        title_elements = news.find_all('h3')
        for title_ele in title_elements:
            title = title_ele.text.strip()
            link_ele = title_ele.find('a')
            if link_ele is not None:
                link = link_ele['href']
                for interest in userList:
                    if interest.lower() in title.lower():
                        User_news.append({'title': title, 'link': link})
                        break
    return User_news



def filtering_news_from_indian(news,userList):
    User_news = []
    if isinstance(news, BeautifulSoup):
        title_elements = news.find_all('h3')
        for title_ele in title_elements:
            title = title_ele.text.strip()
            link_ele = title_ele.find('a')
            if link_ele is not None:
                link = link_ele['href']
                for interest in userList:
                    if interest.lower() in title.lower():
                        User_news.append({'title': title, 'link': link})
                        break
    return User_news


def filtering_news_from_TOI(news, userList):
    User_news = []
    if isinstance(news, BeautifulSoup):
        title_elements = news.find_all('div', class_='gXWlF _3IvxE _3bMre')
        for title_element in title_elements:
            link_ele = title_element.find('a')
            if link_ele is not None:
                title = link_ele.get_text(strip=True)
                link = link_ele['href']
                for interest in userList:
                    if interest.lower() in title.lower():
                        User_news.append({'title': title, 'link': link})
                        break
    return User_news



    

def sort_news(news):
    sorted_news = sorted(news,key=lambda article : article['title'].lower())
    return sorted_news

def display_news(news):
    for article in news:
        print("Title: ", article['title'])
        print("Link: ",article['link'])
        print("\n")
    
main()

