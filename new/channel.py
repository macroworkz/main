# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 19:15:45 2022

@author: bluesky
"""

# channel.py
#
# A minimal object that implements a message channel over a pair
# of file descriptors (like a pipe)

# channel.py
import pickle

class Channel(object):
 def __init__(self,out_f,in_f):
      self.out_f = out_f
      self.in_f = in_f
 def send(self,item):
     
     pickle.dump(item,self.out_f)
     self.out_f.flush()
 def recv(self):
     return pickle.load(self.in_f)
