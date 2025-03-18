import time
import tkinter as tk
from tkinter import *
from typing import Counter
passfound = False
array =['A','B,'C','D','E','F','G','H','I','J','K','L','M','N','O,P','Q',R','S','T','U','V','W','X','Y','Z' '','a','b','c','d','e','f','g'','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z '"1","2","3","4","5","6","7","8","9","0","!","£","$","%","^","&","*","(",")","-","_","=","+","[ ,"]"]","{","}","#","~","@",";",":","<",">","?","/","|  
password = input("please input a 1-4 character password")
time=time.time()
Counter = 0
for a  in array:
  Counter += 1
  guess = a
  print(Trying:  '+guess)=+'
  Attempts: '+str(Counter)')
  if guess == password:
    passfound = True
    print("your password is", password)
    time2 = time.time()
    time = time2 - time 1
    if time>60:
      print('It took:',time/60,'minutes and,int(time%60),'seconds')
            else;
      continue
      break
      else
      continue
      break
      if password == False:
        for a in array:
          for b in array:
            for c in array:
              Counter+=1
              guess = a+b+c
              print(Trying:  '+Guess)=+' Attemts: '+str(Counter))
              if guess == password:
                passfound = True
                print ('The  password is', password)
                time2 = time.time()
                time = time2 - time 1
                if time>60:
                  print('It took:',time/60,'minutes and,int(time%60),'seconds')
                        if time<60:
                          print('It took:',time,'seconds')
              
          
      
        
      
      
      
      
    

  