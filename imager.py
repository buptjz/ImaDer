#coding:utf-8
#!/usr/bin/python

import os
import hashlib
import threading
import Queue
import urllib2
import socket 
from tools import getTypeRequest,zh2unicode
from BeautifulSoup import BeautifulSoup
import time
import sys

class MutilThread(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue = queue
    def run(self):
        #按照顺序执行，先put所有的的queue然后再逐步处理；
        #while queue.qsize() != 0:
        while True:
            imageID = self.queue.get()
            #size = queue.qsize()
            #print "Thread's Size: %s" % size
            getImageFromWeb(imageID)
            self.queue.task_done()

def DownloadImage():
    url_li = getImageUrls(START,END)
    #先将所有的item，put到queue;
    for i in range(10):
        t = MutilThread(queue)
        t.setDaemon(True)
        t.start()
    for url in url_li:
        queue.put(url)
        queue.join()

def getImageFromWeb(url):
    #time.sleep(0.2)
    
    print(url)
    tn.append(url+'\n')
    socket.setdefaulttimeout(60)
    try:
        htmlbody =getTypeRequest(url)
        data = htmlbody.read()
        soup = BeautifulSoup(data)
        imgurl = soup.find('img')['src']
        if not (imgurl == None or imgurl in imageUrlList):
            imageUrlList.append(imgurl)
        htmlbody.close()
    except Exception as e:
        print e
        print "Happens when download Image : "+ url
        errorImageList.append(url) 

def getImageUrls(start,end):
    pre = 'http://michigan.mugshotsdatabase.com/'
    return  [pre+str(i) for i in range(start,end+1)]

def main():
    global imageUrlList
    DownloadImage()
    successFile = 'ImagesURLFILE'+str(START)+'.txt'
    errorFile = "errorImages"+str(START)+'.txt'
    triedNumbers = "tried"+str(START)+'.txt'
    
    imgFile = open(successFile,'w')   
    imageUrlList = [i+'\n'for i in imageUrlList]
    imgFile.writelines(imageUrlList)
    imgFile.close()
    
    ef = open(errorFile,'w')
    ef.writelines(errorImageList)
    ef.close()
    
    trF = open(triedNumbers,'w')
    trF.writelines(tn)
    trF.close()
    
if __name__=='__main__':
    queue = Queue.Queue()
    errorImageList = []
    imageUrlList = []
    count = []
    tn = []
    START = int(sys.argv[1])
    END = int(sys.argv[2])
    
    main()