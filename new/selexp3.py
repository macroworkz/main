# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 19:16:50 2022

@author: bluesky
"""

import channel
import subprocess
import json
import numpy
from parent import Brth
import sys
# sys.path.append('C:/Users/bluesky/googlemaps')
# d = subprocess.Popen(['python','scraper.py'],
#                       stdin=subprocess.PIPE,
#                     stdout=subprocess.PIPE)
# dh = channel.Channel(d.stdin,d.stdout)




path_to_file='C:/Users/bluesky/Desktop/chromedriver/ccode.txt'
with open(path_to_file) as fe:
    contents = fe.readlines()

y = json.loads(contents[0])

list_1=[792]
list_2=list(y.values())[1:]
list_2=list(y.values())
#market=[410,156,191,251,792,276]
exporter=list_1


from itertools import product

market = []
 
# Extract Combination Mapping in two lists
# using zip() + product()
market = list(list(zip(list_1, element)) for element in product(list_2, repeat = len(list_1)))
# market=market[:5]
l =[]
chunk=5
jh=int(len(market)/chunk)
for i in range(jh+1):
    l.append(market[chunk*i:chunk*i+chunk])  


# dh.send([y,exporter,l[25]])
gg=Brth(l)

gg.openpool()

for i in range(jh+1):
    gg.send(i,[y,exporter,l[i],str(i)])



print("ended")



