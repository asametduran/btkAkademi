import requests
from bs4 import BeautifulSoup

url ="https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250"

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
}

html = requests.get(url,headers=headers).content
soup = BeautifulSoup(html,"html.parser")
liste = soup.find("ul",{"class":"ipc-metadata-list"}).find_all("li",limit=250)

for item in liste:
    filmadi = item.find("h3",{"class":"ipc-title__text"}).text
    print(filmadi)