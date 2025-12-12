        
class mobilephone:#you creat a clss name as mobile phone
    mobilecount=0
    def __init__(self,phonebrand,phoneprice):#inside class you creat a one constructor and give the paramaetrs ie are phonename and price
        self.phonebrand=phonebrand#then inside constructor you creat a variable to store the data of the constructor
        self.phoneprice=phoneprice
        mobilephone.mobilecount+=1
    def showdetails(self):#then again inside the constructor you creat a one function called show details
        print(f"brand={self.phonebrand} price={self.phoneprice}")#this function will print the deatails which were stored in a variable of the constructor with the help of the self
phone1=mobilephone("vivo 19",10000)#after that you creat a one object ie phone 1 to call the class phone1.showdetails()# after this you called showdwtails function
phone2=mobilephone("apple",100000)
print(mobilephone.mobilecount)
phone1.showdetails()
phone2.showdetails()        