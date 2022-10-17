# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 20:26:43 2022

@author: bluesky
"""

# parent.py
import channel
import psutil
import subprocess
import os
import pandas as pd
import string
import random


# env = os.environ.copy()
# env['PYTHONIOENCODING'] = 'latin-1'
# p = subprocess.Popen(['python','child.py'],
#                       stdin=subprocess.PIPE,
#                     stdout=subprocess.PIPE)
# ch = channel.Channel(p.stdin,p.stdout)

# h = psutil.Process()
# print(f"Child: {h}")


class Brth():
    
    def __init__(self,token_pairs):
        self.pool=len(token_pairs)
        self.items = []
        self.ch=[]
        self.msg=[]
    def openpool(self):
        for i in range(self.pool):
            self.items.append(subprocess.Popen(['python','scraper.py'],
                     stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE))
            self.ch.append( channel.Channel(self.items[i].stdin,self.items[i].stdout))
            


            # gr=random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)
            # self.ch[i].send(gr)
            # self.items[i].wait()

            # self.items[i].terminate()
            # self.msg.append(self.ch[i].recv())
    def closepool(self):
        for i in range(self.pool):
            self.items[i].terminate()
    
    def send(self,k,tsg):
        self.ch[k].send(tsg)