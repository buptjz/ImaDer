# -*- coding: utf-8 -*-

import urllib2

def zh2unicode(stri): 
    """转换编码到unicode,
    编码方式从utf-8,gbk,iso-8859-1,big5,ascii中选择.""" 
    for c in ('ascii', 'utf-8', 'gb2312', 'gbk', 'gb18030', 'big5'): 
	flag = 0
        try: 
	    decodeString = stri.decode(c)
	    flag = 1
            return decodeString
        except: 
            pass 
    if flag == 0:
	stri.decode("gbk","ignore")
	return stri
    
def getTypeRequest(url):
    headers = {
        'Host':'michigan.mugshotsdatabase.com',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:24.0) Gecko/20100101 Firefox/24.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language':'q=0.8,en-us;q=0.5,en;q=0.3',
        'Connection':'keep-alive',
        'Cache-Control':'max-age=10',
    }

    req = urllib2.Request(
        url = url,
        headers = headers
    )
    result = urllib2.urlopen(req)
    
    return result