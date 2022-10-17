# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 19:29:37 2022
class based intracen scraper
@author: bluesky
"""
#children processes called from 
from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import sys
import subprocess
import channel
import time
import warnings
import json
import random

#Useless warnings closed
warnings.filterwarnings("ignore")
# for data sharing these 2 are necessary
sys.stdin = sys.stdin.detach()
sys.stdout = sys.stdout.detach()

dh = channel.Channel(sys.stdout,sys.stdin)



# enable browser logging
d = DesiredCapabilities.CHROME
d['goog:loggingPrefs'] = { 'browser':'ALL' }

time.sleep(1)
driver = webdriver.Chrome(executable_path='C:/Users/bluesky/Desktop/chromedriver/chromedriver.exe')
# driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
#when it is working webdriver execution time needs to be defined
driver.set_script_timeout(90)
# path_to_file='C:/Users/bluesky/Desktop/chromedriver/countrycode.txt'
# with open(path_to_file) as fe:
#     contents = fe.readlines()



y,exporter,market,csvi = dh.recv()

# driver.get("https://exportpotential.intracen.org/en/products/gap-chart?fromMarker=i&exporter="+str(792)+"&toMarker=j&market="+str(842)+"&whatMarker=k&product=a")
 
tg=[]
for j in range(len(market)):


    try:

        driver.get("https://exportpotential.intracen.org/en/products/gap-chart?fromMarker=i&exporter="+str(792)+"&toMarker=j&market="+str(market[j][0][1])+"&whatMarker=k&product=a")
        
        time.sleep(int(random.random()*10+5))
    
    
        surveypage=driver.execute_script('''var elementExists = document.getElementById("mat-dialog-0");
                                         if (elementExists==null)
                                         {var a =0;} else {var a=1;}
                                         return a''')
        time.sleep(2)
        if surveypage==1:
            #click konusu problem çıkarıyor
            driver.execute_script("""document.getElementsByClassName('mat-focus-indicator mat-button mat-button-base')[2].click()""")
            # driver.execute_script("document.querySelector('#mat-dialog-0 > app-survey-dialog > div:nth-child(3) > button:nth-child(2)').click()")
            time.sleep(2)
            n=1
        else:
                n=0
    
        string="mat-checkbox-"
        t=list()
        lencheck=driver.execute_script('''var a=document.querySelectorAll('input[type="checkbox"]').length
                                       return a''')
        for i in range(lencheck-1):
            t.append(string+str(i+1+n))
            
        f=1
        for bm in range(20):
            ww="'"+string+str(bm+2+n)+"'"
            g=driver.execute_script("var d=document.getElementById("+ww+"); var c=d.className.includes('indeterminate'); return c")
            time.sleep(1)
            if g==True:
                f=f+1
                
        for c,i in enumerate(t):
            driver.find_element("id",i).click();
            time.sleep(0.2)
            if c<f:
                driver.find_element("id",i).click();
        time.sleep(int(random.random()*10)+5)
    
    
    
        driver.execute_script('''
    
                          for (var i = 0; i < document.querySelectorAll("div.datavis, g[class^='node code']").length; i++) {
    console.log(document.querySelectorAll("div.datavis, g[class^='node code']")[i].__data__.item.code," ",
    document.querySelectorAll("div.datavis, g[class^='node code']")[i].__data__.value," ",
    document.querySelectorAll("div.datavis, g[class^='node code']")[i].__data__.exportValue)
    }''')
    
    
        time.sleep(5)
        fr=driver.get_log('browser')
    
        keyValList = ['INFO']
        
        expectedResult = [k for k in fr if k['level'] in keyValList]
        
        for m,n in enumerate(expectedResult):
            expectedResult[m]["TR"]=list(y.keys())[list(y.values()).index(market[j][0][1])] 
        # tg.append(expectedResult)
        fg=[[l.get("message")+'"'+l.get("TR")] for l in expectedResult]
   
        flattened = [val for sublist in fg for val in sublist]
        # import copy
        # flat=copy.deepcopy(flattened)
        dc=[]
        for ig,ih in enumerate(flattened):
            if ih.find(".intracen.") != -1:
                dc.append(ig)
                
        for index in sorted(dc, reverse=True):
            del flattened[index] 
            
        for index in range(len(flattened)):
              
            flattened[index]=flattened[index][17:]
            flattened[index]=flattened[index].split('"')
        
    
        
        fd=pd.DataFrame(flattened)
        fd.to_csv("C:/Users/bluesky/googlemaps/result"+csvi+".csv",mode="a", index=False, header=False)

 
        if j==len(market)-1:
            driver.quit()
    except Exception as e:
        bt=pd.DataFrame([e,surveypage])
        bt.to_csv("C:/Users/bluesky/googlemaps/log.csv",mode="a",index=False,header=False)
        if j==len(market)-1:
            driver.quit()
        pass

