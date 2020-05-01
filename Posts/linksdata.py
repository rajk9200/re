from bs4 import BeautifulSoup
import requests


def getResults():
    res =requests.get("https://www.sarkariresult.com/")
    soup  = BeautifulSoup(res.content, 'html.parser')
    resultslist =[]
    results =soup.select_one('#post')
    for link in results.select('a a'):
        data ={link.attrs['href']:link.text}
        resultslist.append(data)


    return resultslist
# print(getResults())
# print(set(resultslist))
# print(len(set(resultslist)))