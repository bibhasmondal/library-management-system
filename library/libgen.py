import requests
import bs4
import json
def searchbooks(group,name):
    try:
        url="http://libgen.is/search.php?&res=100&page=1&req="
        url += name
        res = requests.get(url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, "lxml")
        elem = soup.select('tr[valign="top"]')
        for i in range(1,len(elem)):
            res = requests.get(elem[i].select('td a[title="Libgen.io"]')[0].attrs['href'], "lxml")
            res.raise_for_status()
            soup = bs4.BeautifulSoup(res.text, "lxml")
            result = {'booklink':soup.select('a')[1].attrs['href'],\
            'title':elem[i].select('td')[2].getText(),\
            'size':elem[i].select('td')[7].getText(),\
            'type':elem[i].select('td')[8].getText(),\
            'author':elem[i].select('td')[1].getText()}
            group.send({'text':json.dumps(result)})
    except Exception as e:
        print(e)