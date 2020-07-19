from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
def onLoadFile():
    try:
        hdr= headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        req = Request("https://www.indiatoday.in/", headers=hdr)
        openURL = urlopen(req)
        coreHtml = BeautifulSoup(openURL, 'html.parser')
        classData = coreHtml.find(class_="top_stories_ordering")
        for item in classData.find_all('a'):
            print('\n item Link',item['href'],'Item Text',item.text)
            
    except Exception as e:
        print("error", e)



onLoadFile()