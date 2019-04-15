# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 14:42:44 2019

@author: ROSHAN
"""

d={"IN":["India","Delhi",130000000],"US":["America","Washingtone",32000000],"AU":["Australia","Canebbra",24000000],"CA":["Canada","Ottawa",940000]}

#here view function is defined
def view():
    j=""
    for i in sorted(d):
        j=j+i+" "
    print("Country codes:{}".format(j))
    k=input("Enter country code:")
    k=k.upper()
    if k in d.keys():
        return "country is:{}\nCountry capital is:{}\ncountry population is:{}".format(d[k][0],d[k][1],d[k][2],)
    else:
        return "There is no country code for {}".format(k)
    
#here add function is defined  
def add():
    k=input("Enter country code:")
    k=k.upper()
    a1=input("Enter country name:")
    a1=a1.capitalize()
    a2=input("Enter country capital:")
    a2=a2.capitalize()
    a3=input("Enter country population:")
    d[k]=[a1,a2,a3]
    return "{} is added to list".format(k)

#here Del function is defined
def Del():
    j=""
    for i in sorted(d):
        j=j+i+" "
    print("Country codes: {}".format(j))
    k=input("Enter the country code to delete:")
    k=k.upper()
    if k in d:
        del d[k]
        return "The country code {} is deleted".format(k)
    else:
        return "The country code is not present"



while True:
    k=input("SELECT AN OPTION: \nview: view country names \nadd: Add a country\ndel: Delete a country\nexit- Exit the program\nYour choice:")
    def option():
        if k=="view":
            print(view())
            return ""
        elif k=="add":
            print(add())
            return ""
        elif k=="del":
            print(Del())
            return ""
    if k=="exit":
        break
    #from here program starts
        
    print(option())
