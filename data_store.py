#import packages
import time
import threading 
from threading import*

#create dictionary
dict ={} 

#create operation
def create(key,value,timeout=0):
    if key in dict:
        print("error: key already exists") 
    else:
        if(key.isalpha()):
            if len(dict)<(1024*1024*1024) and value<=(16*1024*1024):
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: 
                    dict[key]=l
            else:
                print("error: Memory limit exceeded!! ")
        else:
            print("error: Invalid key name!! key name must contain only alphabets and no special characters or numbers")

#read operation
def read(key):
    if key not in dict:
        print("error: given key does not exist in database. Please enter a valid key") 
    else:
        b=dict[key]
        if b[1]!=0:
            if time.time()<b[1]:
                stri=str(key)+":"+str(b[0]) 
                return stri
            else:
                print("error: time-to-live of",key,"has expired") 
        else:
            stri=str(key)+":"+str(b[0])
            return stri

#delete operation
def delete(key):
    if key not in dict:
        print("error: given key does not exist in database. Please enter a valid key") 
    else:
        b=dict[key]
        if b[1]!=0:
            if time.time()<b[1]:
                del dict[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired") 
        else:
            del dict[key]
            print("key is successfully deleted")

#modify operation
def modify(key,value):
    b=dict[key]
    if b[1]!=0:
        if time.time()<b[1]:
            if key not in dict:
                print("error: given key does not exist in database. Please enter a valid key") 
            else:
                l=[]
                l.append(value)
                l.append(b[1])
                dict[key]=l
        else:
            print("error: time-to-live of",key,"has expired") 
    else:
        if key not in dict:
            print("error: given key does not exist in database. Please enter a valid key") 
        else:
            l=[]
            l.append(value)
            l.append(b[1])
            dict[key]=l
