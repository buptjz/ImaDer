from HTMLParser import HTMLParser
import urllib
import sys
from tools import getTypeRequest
import BeautifulSoup
class parselinks(HTMLParser):
    def __init__(self):
        self.data=[]
        self.href=0
        self.linkname=''
        HTMLParser.__init__(self)
    def handle_starttag(self,tag,attrs):
        if tag =='a':
            for name,value in attrs:
                if name == 'href':
                    self.href=1
    def handle_data(self,data):
        if self.href:
            self.linkname+=data
    def handle_endtag(self,tag):
        if tag=='a':
            self.linkname=''.join(self.linkname.split())
            self.linkname=self.linkname.strip()
            if  self.linkname:
                self.data.append(self.linkname)
            self.linkname=''
            self.href=0
    def getresult(self):
        for value in self.data:
            print value
if __name__=="__main__":
    IParser = parselinks()
    url = 'http://michigan.mugshotsdatabase.com/21002'
    data = getTypeRequest(url).read()
    #IParser.feed()
    
    soup = BeautifulSoup.BeautifulSoup(data)
    imgurl = soup.find('img')['src']
    
    IParser.getresult()
    IParser.close()