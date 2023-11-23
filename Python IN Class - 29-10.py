# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 10:11:30 2023

@author: MadCorpSlave
"""

'''
DICTIONARY - UNDERSTANDING
CANN HAE PRIMITIVE DATA TYPE 
can have list, 
'''

## Single line dictionary - single line but multiple data 
dPhone = {
        "brand": "OnePlus",
        "model": "QR",
        "year": 2021,
        "ram": "12 GB"
}

## defining multiple elements in dictionary
dPhones = {
        "brand": ["OnePlus", "Samsung"],
        "model": ["QR","M12"],
        "year": [2021, 2022],
        "ram": ["12 GB","8gb"]
}

print(dPhones["brand"])

## Dictionary can have multiple data all types 
type(dPhone)
type(dPhones) 

## getting or fetching data from dictionary
dPhones["model"]

## Using GET Method 
dPhones.get("model")


## Gettig Keys that store data in the dictionary - Keys are like heading of columnn
dPhones.keys()  ## Which are data keys


dPhones.keys()  ## shows which data iis stored 

## ITEMS method shhows all keys and data in it as a slist
dPhones.items()

"""editing dictionary     """
dPhones["refresh_rate"]="120 hz"   ## Adds key names refresh_rate in dPhones dictionary
dPhones["model"]="S23"
dPhones.update({"brand":["Apple, Nothing"]})

if "brand" in dPhones:
    print ("Brand Key is present in dictionary")
else:
    print ("Brand Key is NOT present in dictionary")


## editing the  dictionary - CANT change key name but can be copied to new key name and old one deleted
dPhones["brand_new"]=dPhones["brand"]
del dPhones["brand"]

## POP fuction  retuns the items popped - can be assigned to dictionary 
dPhones["brand"] = dPhones.pop("brand_new")

## deleting the dictionary key
del dPhones["year"]   ## deles all data and key Year

## emptying the dictionar y
dPhones.clear()  ## using clear method - empties the dictionary 

del dPhone["model"][0]  ## deletes QR from phones = on 0th index 


## Looping through the dictionary 
""" Redefining the dPhones """
dPhones = {
        "brand": ["OnePlus", "Samsung"],
        "model": ["QR","M12"],
        "year": [2021, 2022],
        "ram": ["12 GB","8gb"]
}

## Checking with looping
for ele in dPhones:   ## ele returs all keys of dictionary
    print(ele)      ## prints all keys of dict

## printing values with looping
for ele in dPhones:   ## ele returs all keys of dictionary
    print(dPhones[ele])      ## prints all keys of dict

## Printing all values of dict 
for eleKey,eleValues in dPhones.items():  ## items returns keys and values 
    print(eleKey,eleValues)   ## Prints keys and values 
  
duplicate_dPhones=dPhones.copy()

