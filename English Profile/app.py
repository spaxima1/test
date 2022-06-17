import requests
from bs4 import BeautifulSoup

from functions import Information,getWordInfo
from mongoDb import insert

url="https://www.englishprofile.org/american-english"
__base_url="https://www.englishprofile.org"

wordList=[]
while True:  
    page=requests.get(url)
    soup=BeautifulSoup(page.content,'html.parser')
    tbody=soup.find('tbody')
    trList=tbody.find_all('tr')
    for tr in trList:
        tds=tr.find_all('td')
        innerUrl=__base_url+tds[-1].a['href']
        innerPage=requests.get(innerUrl)
        innerSoup=BeautifulSoup(innerPage.content,'html.parser')
        infoWord=Information(innerSoup)
        wordIn=getWordInfo(tds)
        wordIn.posSection=infoWord
        wordList.append(str(wordIn.__dict__))
        insert(wordIn.__dict__)
    if None!=soup.find('li',{'class':'pagination-next'}).a:
        url=__base_url+soup.find('li',{'class':'pagination-next'}).a['href']
    else:
        break
    if len(wordList)>100:
        break
    print(url)
