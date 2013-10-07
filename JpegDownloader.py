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
    theFile = open(IMAGECONTENT,'r')
    
    url_li = theFile.readlines()
    url_li = [url[:-1] for url in url_li]
    theFile.close()
    #先将所有的item，put到queue;
    for i in range(10):
        t = MutilThread(queue)
        t.setDaemon(True)
        t.start()
    for url in url_li:
        queue.put(url)
        queue.join()

def getImageFromWeb(url):
    print(url)
    tn.append(url+'\n')
    socket.setdefaulttimeout(60)
    path = IMMAGEPATH+url.split('/')[-1]
    try:
        webpage = getTypeRequest(url)
        data = webpage.read()
        with open(path, "wb") as jpg:
            jpg.write(data)
            webpage.close()
            imageUrlList.append(url)

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
    successFile = '/Volumes/JZ/SMUGIMG/JPEG'+START+'.txt'
    errorFile = "/Volumes/JZ/SMUGIMG/EJPEG"+START+'.txt'
    triedNumbers = "/Volumes/JZ/SMUGIMG/TJPEG"+START+'.txt'
    
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
    START = sys.argv[1]
    IMMAGEPATH = '/Volumes/JZ/SMUGIMG/'+START+'/'
    IMAGECONTENT = 'ImagesURLFILE'+START+'.txt'
    queue = Queue.Queue()
    errorImageList = []
    imageUrlList = []
    count = []
    tn = []    
    main()