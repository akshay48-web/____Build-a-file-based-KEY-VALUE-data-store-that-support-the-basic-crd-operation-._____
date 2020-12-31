import time
import json
import threading

temp={}
#------------------------------------------------------------------------------------------------------------------------------------------
axt=input("import data 'yes'/'no' :-")
    if(axt=='yes'):
       print("wait for load data")
        with open('file.json','r') as fj:
          wait_data=json.load(fj)    
          temp=wait_data
        print('data is loading...')
        print(temp)
    else:
        print("error data not import")
#-------------------------------------------------------------------------------------------------------------------------------------
# create operation 
#-------------------------------------------------------------------------------------------------------------------------------------------

def create(key,value,timeout=0):
    if key in temp:
        print("error found this <><>key already exists<><>") 
    else:
        if(key.isalpha()):
            if len(temp)<(1024*1020*1024)and value<=(16*1024*1024):
                if timeout==0:
                    log=[value,timeout]
                else:
                    log=[value,time.time()+timeout]
                if len(key)<=32: 
                    temp[key]=log
            else:
                print("error found Memory limit exceeded!! ")
        else:
            print("error found not valid key_name, key_name accept only alphabets and no special characters or numbers")
#-----------------------------------------------------------------------------------------------------------------------------------------
#read operation
#------------------------------------------------------------------------------------------------------------------------------------------            
def read(key):
    if key not in temp:
        print("error found given key does not exist in database. Please enter a valid key") 
    else:
        b=temp[key]
        if b[1]!=0:
            if time.time()<b[1]:
                stri=str(key)+":"+str(b[0]) 
                return stri
            else:
                print("error found time-to-live of",key,"has expired") 
        else:
            stri=str(key)+":"+str(b[0])
            return stri
#------------------------------------------------------------------------------------------------------------------------------------
#delete operation
#---------------------------------------------------------------------------------------------------------------------------------------
def delete(key):
    if key not in temp:
        print("error found given key does not exist in database. Please enter a valid key")
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                del temp[key]
                print("key is deleted")
            else:
                print("error found time-to-live of",key,"has expired")
        else:
            del temp[key]
            print("key is deleted")

#---------------------------------------------------------------------------------------------------------------------------------------
#