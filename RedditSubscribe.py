# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
#all code by threebones except for modules obviously
import time
import string
import requests
from bs4 import BeautifulSoup
import sys
from config import *

print "by github.com/threebarber"

accountlist = open(filename,'r+')

with requests.Session() as c:

        for line in accountlist.readlines():
            account  = line.strip('\n')
            username = account.split(':')[0]
            password = account.split(':')[1]
            
        USER                = username
        PASSWD              = password
        API_TYPE            = 'json'
        OP                  = 'login-main'
        RENDERSTYLE         = 'html'
        ACTION              = 'sub'
        R                   = 'subname'
        
        
        loginpost           = 'https://www.reddit.com/api/login/'+USER
        homeurl             = 'https://www.reddit.com'
        subreddit           = 'https://www.reddit.com/r/'+subname
        subscribepost       = 'https://www.reddit.com/api/subscribe'
        
        print "[+]Logging in as "+USER+"..."  
        print loginpost 
    
        login_data = dict(user = USER, passwd = PASSWD, api_type = API_TYPE, op = OP)
        login = c.post(loginpost, data=login_data, headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36","x-requested-with":'XMLHttpRequest','referer':'https://www.reddit.com','origin':'https://www.reddit.com'})
    
        if 'reddit_session' in str(login.headers):
            print '[+]Successfully logged in'
        else:
            print '[-]Could not login'
        
        r = c.get(subreddit,headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36","x-requested-with":'XMLHttpRequest','referer':'https://www.reddit.com','origin':'https://www.reddit.com'}).content
        soup = BeautifulSoup(r,'html.parser')
    
        SR =  soup.find('input',{ 'name': 'thing_id' })['value']
        UH =  soup.find('input',{ 'name': 'uh' })['value']
        
        REDDIT_SESSION = c.cookies['reddit_session']
    
        subscribe_data = dict(sr = SR, action = ACTION, r = R, uh = UH, renderstyle = RENDERSTYLE)
        subscribe = c.post(subscribepost,data=subscribe_data,headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36","x-requested-with":'XMLHttpRequest','referer':'https://www.reddit.com/r/streetwear','origin':'https://www.reddit.com','reddit_session':REDDIT_SESSION})
        if str('<Response [200]>') == str(subscribe):
            print '[+]Subscribed to /r/'+subname
        else:
            print '[+]Error Subscribing to /r/'+subname
        time.sleep(delay)
        