d={"IN":"India","US":"America","AU":"Australia","CA":"Canada"}

#here view function is defined
def view():
    j=""
    for i in d:
        j=j+i+" "
    print("Country codes:{}".format(j))
    k=input("Enter country code:")
    if k in d.keys():
        return "country is {}:".format(d[k])
    else:
        return "There is no country code for {}".format(k)
    
#here add function is defined  
def add():
    k=input("Enter country code:")
    a1=input("Enter country name:")
    d[k]=a1
    return "{} is added to list".format(a1)

#here Del function is defined
def Del():
    j=""
    for i in d:
        j=j+i+" "
    print("Country codes:{}".format(j))
    k=input("Enter the country code to delete:")
    del d[k]
    return "The country code {} is deleted".format(k)



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
