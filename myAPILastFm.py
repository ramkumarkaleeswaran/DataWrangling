# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 15:54:03 2015

@author: ramku
"""

import requests
import json
import pandas

def getTopArtist():
    url = "http://www.last.fm/api/auth/?api_key=cd04815196f0a58983ee398e118a6f51&token=5b10d6961947d10bcf8ce5fe00503787";

    print data["topartists"]["artist"][0]["name"];

#print data["topartists"]["artist"][2]["name"];

#print (data["album"]['artist']);
#print 'spain top';
print 5 +5;
    
    

def getAlbumInfo():
    
    url = "http://ws.audioscrobbler.com/2.0/?method=album.getInfo&api_key=cd04815196f0a58983ee398e118a6f51&artist=Cher&album=Believe&format=json";  
    
    data = requests.get(url).text ;
    
    data = json.loads(data);
    
    print type(data)
    
    print data
    
#    print data[]
    


getAlbumInfo()