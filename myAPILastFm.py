# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 15:54:03 2015

@author: ramku
"""

import requests
import json
import pandas

def getTopArtist():
    url2 = "http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country=spain&api_key=cd04815196f0a58983ee398e118a6f51&format=json";

    print 'hello'
    
    data = requests.get(url2).text ;
    
    data = json.loads(data);
    
    print data

    print "top artist in spain is " 
        
    print data['topartists']['artist'][0]
        
    print data['topartists']['artist'][0]['name']

    
    

def getAlbumInfo():
    
    url = "http://ws.audioscrobbler.com/2.0/?method=album.getInfo&api_key=cd04815196f0a58983ee398e118a6f51&artist=Cher&album=Believe&format=json";  
    
    data = requests.get(url).text ;
    
    data = json.loads(data);
    
    print type(data)
        
    print data
    


#getAlbumInfo()

getTopArtist()
