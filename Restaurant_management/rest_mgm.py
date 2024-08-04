import time
import csv
import random
from win32com.client import Dispatch
import pandas as pd
pd.set_option('display.max_columns',None)
def speak(str):
    speak=Dispatch(("SAPI.SpVoice"))
    speak.Speak(str)

line="                 ----------------------------------------------------------"
line2="---------------------------------------------------"
print(line) 
headline="                 |                  Food Wars Cafe                        |"
headline1="                 |               Food Ordering System                     |"
headline2="                 |                By Priyanshu kumar                      |"
headline3=line

print(headline)
print(headline1)
print(headline2)
print(headline3)
time.sleep(1) #for pausing the progrm for two seconds.Imported from time module


print("")
print("")
print("")
print("")
print("")
print("                         ______________________________________")
print("                        |    ::  : : :  ::       :::::::::     |")
print("                        |    ::  : : :  ::       :::::::::     |")
print("                        |    ::  : : :  ::       :::::::::     |")
print("                        |    ::  : : :  ::       :::::::::     |")
print("                        |    ::         ::       :::::::::     |")
print("                        |      :::::::::         :::::::::     |")
print("                        |        ::::            :::::::::     |")  
print("                        |        ::::            :::::::::     |")
print("                        |        ::::            :::::::::     |")
print("                        |        ::::                 ::::     |")
print("                        |        ::::   WELCOME  TO   ::::     |")
print("                        |        ::::    FOOD WARS    ::::     |")
print("                        |        ::::      CAFE       ::::     |")
print("                        |        ::::                 ::::     |")
print("                        |        ::::                 ::::     |")
print("                        |______________________________________|")
if __name__ == '__main__':
    speak("welcome to food wars cafe")
print("")
print("")
print("") 
print("")
print("")
if __name__ == '__main__':
    speak("are you a customer or staff")
    speak("please select")
print("-------------------------")
print("1. Customer")
print("2. Staff")
print("Press 0 to exit")
print("-------------------------")

    
def error():
    print("")
    print("")
    print("WRONG INPUT!")
    print("")
    print("")
    print("Reloading Back in 5 Seconds")
    time.sleep(5)
    print("")
    print("")
    print("")
    print("")
    print("")
    print(line)
    print(headline)
    print(headline1)
    print(headline2)
    print(headline3)
    time.sleep(2)
    
def close():
    response=0
    while response==0:
            t=input("Do you want to order more (Y/N): ")
            if t=="Y" or t=="YES" or t=="yes" or t=="y" :
                print("Reloading in 5 seconds")
                time.sleep(5)
                print()
                print()
                print()
                print()
                print()
                starting()
                                
            else:
                if t=="n" or t=="NO" or t=="N" or t=="no" :
                    time.sleep(1) #for pausing the program for 1 second.Imported from time module
                    print("")
                    print("")
                    print("-------------------------------------------------------")
                    print("OK, No Problem")
                    time.sleep(1) #for pausing the program for 1 second.Imported from time module
                    print("BYE, thanks for choosing us")
                    print("-----------------------------------------------------")
                    break
                

def starting() :
        response=3
        while response==3:
            print(line2)
            print("1. Order New Food Item")
            speak("1. Order New Food Item")
            print("2. Track Order Status")
            speak("2. Track Order Status")
            print(line2)
            response=int(input("Enter(1 or 2):")) #asking the customer
            if response==3:
                response=4
        
        while response==1:
            response=3
            time.sleep(1) #for pausing the program for 1 second.Imported from time module
            print("-----------------------------------------------------") #menu of canteen
            print("           Menu (St. Xavier's Canteen)               ")
            print("   Name                               Price          ")
            print("")
            print(" 1. Patties                            10Rs          ")
            print(" 2. Pizza                              40Rs          ")
            print(" 3. Chowmein                           30Rs          ")
            print(" 4. Samosa                             10RS          ")
            print(" 5. Lemonade                           10RS          ")
            print(" 6. Momos                              30Rs(6 pcs)   ")
            print(" 7. Pastry                             20Rs          ")
            print("-----------------------------------------------------")
            print("")
        
            t1=1 
            choice=input("Enter Serial Number or Food Name you Would like to Order:")
            while t1==1:
                if choice=="1" or choice=="Patties" or choice=="PATTIES" or choice=="patties": #for choice 1
                    time.sleep(1) #for pausing the program for 1 second.Imported from time module
                    sub=10 #price of item
                    speak("You have Picked Patties")
                    print("\U0001f600","You have Picked Patties","\U0001f600")
                    od="Patties"
                    multi=int(input("How many Patties you would like to Order:")) #number or items
                    if multi<=15:
                        biln=sub*multi
                        gst=(sub*multi)*18/100
                        bil=biln+gst
                        time.sleep(2) #for pausing the program for 2 seconds.Imported from time module
                        print("\U0001F447","\U0001F447","\U0001F447","\U0001F447","\U0001F447","\U0001F447","\U0001F447")
                        print("Sub-Total:",biln)
                        print("GST 18%:",gst)
                        print("Total:",bil)
                        print("\U0001F446","\U0001F446","\U0001F446","\U0001F446","\U0001F446","\U0001F446","\U0001F446")
                        t1=0
                    else:
                        time.sleep(1)
                        print("")
                        print("You cannot order More than 15 in One Order")
                        print("")
                        time.sleep(1)
                        t1=1
        
                elif choice=="2" or choice=="Pizza" or choice=="PIZZA" or choice=="pizza": #for choice 2
                    time.sleep(1) #for pausing the program for 1 second.Imported from time module
                    sub=40 #price of item 
                    print("\U0001F60E","You have Picked Pizza","\U0001F60E")
                    od="Pizza"
                    multi=int(input("How many Pizzas you would like to Order:")) #number or items
                    if multi<=15:
                        biln=sub*multi
                        gst=(sub*multi)*18/100
                        bil=biln+gst
                        time.sleep(2) #for pausing the program for 2 seconds.Imported from time module
                        print("\U0001F447","\U0001F447","\U0001F447","\U0001F447","\U0001F447","\U0001F447","\U0001F447")
                        print("Sub-Total:",biln)
                        print("GST 18%:",gst)
                        print("Total:",bil)
                        print("\U0001F446","\U0001F446","\U0001F446","\U0001F446","\U0001F446","\U0001F446","\U0001F446")
                        t1=0
                    else:
                        time.sleep(1)
                        print("")
                        print("You cannot order More than 15 in One Order")
                        print("")
                        time.sleep(1)
                        t1=1
        
                elif choice=="3" or choice=="Chowmein" or choice=="CHOWMEIN" or choice=="chowmein": #for choice 3
                    time.sleep(1) #for pausing the program for 1 second.Imported from time module
                    sub=30 #price of item
                    print("\U0001F4A5","You have Picked Chowmein","\U0001F4A5")
                    od="Chowmein"
                    multi=int(input("How many Chowmein Plates you would like to Order:")) #number or items
                    if multi<=15:
                        biln=sub*multi
                        gst=(sub*multi)*18/100
                        bil=biln+gst
                        time.sleep(2)
                        print("\U0001F447","\U0001F447","\U0001F447","\U0001F447","\U0001F447","\U0001F447","\U0001F447")
                        print("Sub-Total:",biln)
                        print("GST 18%:",gst)
                        print("Total:",bil)
                        print("\U0001F446","\U0001F446","\U0001F446","\U0001F446","\U0001F446","\U0001F446","\U0001F446")
                        t1=0
                    else:
                        time.sleep(1)
                        print("")
                        print("You cannot order More than 15 in One Order")
                        print("")
                        time.sleep(1)
                        t1=1
            
                elif choice=="4" or choice=="Samosa" or choice=="SAMOSA" or choice=="samosa": #for choice 4
                    time.sleep(1) #for pausing the program for 1 second.Imported from time module
                    sub=10 #price of item
                    print("\U0001F60F","You have Picked Samosa","\U0001F60F")
                    od="Samosa"
                    multi=int(input("How many Samosas you would like to Order:")) #number or items
                    if multi<=15:
                        biln=sub*multi
                        gst=(sub*multi)*18/100
                        bil=biln+gst
                        time.sleep(2) #for pausing the program for 2 seconds.Imported from time module
                        print("\U0001F447","\U0001F447","\U0001F447","\U0001F447","\U0001F447","\U0001F447","\U0001F447")
                        print("Sub-Total:",biln)
                        print("GST 18%:",gst)
                        print("Total:",bil)
                        print("\U0001F446","\U0001F446","\U0001F446","\U0001F446","\U0001F446","\U0001F446","\U0001F446")
                        t1=0
                    else:
                        time.sleep(1)
                        print("")
                        print("You cannot order More than 15 in One Order")
                        print("")
                        time.sleep(1)
                        t1=1
        
                elif choice=="5"or choice=="Lemonade" or choice=="LEMONADE" or choice=="lemonade": #for choice 5
                    time.sleep(1) #for pausing the program for 1 second.imported from time module
                    sub=10 #price of item
                    print("\U0001F61C","You have Picked Lemonade","\U0001F61C")
                    od="Lemonade"
                    multi=int(input("How many Lemonade you would like to Order:")) #number or items
                    if multi<=15:
                        biln=sub*multi
                        gst=(sub*multi)*18/100
                        bil=biln+gst
                        time.sleep(2) #for pausing the program for 2 seconds.Imported from time module
                        print("\U0001F447","\U0001F447","\U0001F447","\U0001F447","\U0001F447","\U0001F447","\U0001F447")
                        print("Sub-Total:",biln)
                        print("GST 18%:",gst)
                        print("Total:",bil)
                        print("\U0001F446","\U0001F446","\U0001F446","\U0001F446","\U0001F446","\U0001F446","\U0001F446")
                        t1=0
                    else:
                        time.sleep(1)
                        print("")
                        print("You cannot order More than 15 in One Order")
                        print("")
                        time.sleep(1)
                        t1=1
        
                elif choice=="6" or choice=="Momos" or choice=="MOMOS" or choice=="momos": #for choice 6
                    time.sleep(1) #for pausing the program for 1 second.Imported from time module 
                    sub=30 #price of item
                    print("\U0001f60D","You have Picked Momos","\U0001f60D")
                    od="Momos"
                    multi=int(input("How many Momo Plates you would like to Order:")) #number or items
                    if multi<=15:
                        biln=sub*multi
                        gst=(sub*multi)*18/100
                        bil=biln+gst
                        time.sleep(2) #for pausing the program for 2 seconds.Imported from time module
                        print("\U0001F447","\U0001F447","\U0001F447","\U0001F447","\U0001F447","\U0001F447","\U0001F447")
                        print("Sub-Total:",biln)
                        print("GST 18%:",gst)
                        print("Total:",bil)
                        print("\U0001F446","\U0001F446","\U0001F446","\U0001F446","\U0001F446","\U0001F446","\U0001F446")
                        t1=0
                    else:
                        time.sleep(1)
                        print("")
                        print("You cannot order More than 15 in One Order")
                        print("")
                        time.sleep(1)
                        t1=1
        
                elif choice=="7" or choice=="Pastry" or choice=="PASTRY" or choice=="pastry": #for choice 7
                    time.sleep(1) #for pausing the program for 1 second.Imported from time module
                    sub=20 #price of item
                    print("\U0001f929","You have Picked Pastry","\U0001f929")
                    od="Pastry"
                    multi=int(input("How many Pastries you would like to Order:")) #number or items
                    if multi<=15:
                        biln=sub*multi
                        gst=(sub*multi)*18/100
                        bil=biln+gst
                        time.sleep(2) #for pausing the program for 2 seconds.Imported from time module
                        print("\U0001F447","\U0001F447","\U0001F447","\U0001F447","\U0001F447","\U0001F447","\U0001F447")
                        print("Sub-Total:",biln)
                        print("GST 18%:",gst)
                        print("Total:",bil)
                        print("\U0001F446","\U0001F446","\U0001F446","\U0001F446","\U0001F446","\U0001F446","\U0001F446")
                        t1=0
                    else:
                        time.sleep(1)
                        print("")
                        print("You cannot order More than 15 in One Order")
                        print("")
                        time.sleep(1)
                        t1=1
                
                else:
                    time.sleep(2)
                    print("")
                    print("")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Sorry ! We do not have this item in menu ! ")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("")
                    print("")
                    time.sleep(1)
                    choice=input("Enter Serial Number or Food Name you Would like to Order:")
                    t1=1
        
            print("")
            print("")
        
            final=input("Are You Sure you Want to Place the Order(Y/N):")
        
            bil=bil
        
            if final=="Y" or final=="Yes" or final=="yes" or final=="YES" or final=="y":
                vr1=input("Enter Any other Specifications: ")
                if vr1=="":
                    vr1="no"
                print("")
                print("")
                call=input("Please Enter your Phone Number: ")
                time.sleep(1)
                csv_file = csv.reader(open('starting.csv', "r+"))
                temp9=0
                for row in csv_file:
                        if call == row[1].strip():
                            resp1=input("Are you "+row[2]+"(Y/N)"+":")
                            time.sleep(1)
                            if resp1=="y" or resp1=="Y":
                                print("-------------------------------------------------------")
                                print("WELCOME BACK",row[2])
                                print("-------------------------------------------------------")
                                nme=row[2]
                                addr=row[3]
                                pinc=row[4]
                                temp9=1
                                break
                            else:
                                print("")
                                print("ENTER YOUR DETAILS:")
                                print("")
                                temp9=0
                            
                if temp9 == 0:
                    nme=input("Please Enter your Name: ")
                    time.sleep(1)
                    addr=input("Please Enter Delivery Address(Without PINCODE): ")
                    time.sleep(1)
                    pinc=input("Please Enter your Delivery PINCODE: ")
                    time.sleep(2) #for pausing the program for 2 seconds.Imported from time module
                orderno=random.randint(1589678,9896865212) #for generating a random order number.Imported from time module
                for row in csv_file:
                    if orderno == row[5]:
                        orderno=orderno+1
                dict={'phone' : call, 'name' : nme, 'address' : addr, 'pincode' : pinc, 
                      'orderno' : orderno,'quantity' : multi,'Particulars': od, "Specifications": vr1,
                      "Sub-Total":biln,"GST 18%:":gst,"Total":bil,"Status": "In Process"}
                print("Specifications:",vr1)
                df=pd.DataFrame(dict , index=[0])
                df.to_csv('starting.csv', header=False,mode='a')
                print("")
                print("")
                print("-------------------------------------------------------")
                print("\U0001F449","Your Order Number is:",orderno,"\U0001F448")
                print("You order is On the Way")
                print("Total Bill:",bil,"Rs")
                print("")
                print("")
                print("Customer Details:")
                print("Name:",nme)
                print("Address:",addr)
                print("PINCODE:",pinc)
                print("")
                print("")
                print("Order Details:")
                print("Particulars:",od," X ",multi)
                print("Specifications:",vr1)
                print("-------------------------------------------------------")
                time.sleep(1) #for pausing the program for 1 second.Imported from time module
                print("")
                print("")
                print("Thank you for Choosing Us")
                break
                
            else:
                time.sleep(1) #for pausing the program for 1 second.Imported from time module
                print("")
                print("")
                print("-------------------------------------------------------")
                print("OK, No Problem")
                time.sleep(1) #for pausing the program for 1 second.Imported from time module
                print("BYE, Reloading Back in 5 Seconds")
                print("-----------------------------------------------------")
                time.sleep(5)
                print("")
                print("")
                print("")
                print("")
                print("")
                break
            
                
                
        while response==2:
            print("")
            print("")
            track=input("Enter the Order Number:")
            time.sleep(1)
            print("")
            print("")
            tk=0
            csv_file = csv.reader(open('starting.csv', "r"))
            for row in csv_file:
                        if track == row[5].strip():
                            print("-------------------------------------------------------")
                            print("ORDER STATUS")
                            print("")
                            print("Name: ",row[2])
                            print("Status: ",row[12])
                            print("-------------------------------------------------------")
                            tk=1
                            print("")
                            time.sleep(2)
                            print("Reloading Back in 5 Seconds")
                            time.sleep(5)
                            print("")
                            print("")
                            print("")
                            print("")
                            print("")
                            print(headline)
                            print(headline1)
                            print(headline2)
                            print(headline3)
                            time.sleep(2)
                            starting()
            if tk==0:
                print("")
                print("ORDER NUMBER DOES NOT EXIST")
                print("")
                time.sleep(2)
                print("Reloading Back in 5 Seconds")
                time.sleep(5)
                print("")
                print("")
                print("")
                print("")
                print("")
                print(headline)
                print(headline1)
                print(headline2)
                print(headline3)
                time.sleep(2)
                close()
                            
            while response != 3 and response != 1 and response !=2 and response !=0 :
                response=3
                error()
                

def admin():
    username=input("Enter Admin Username:")
    l=[]
    csv_file1 = csv.reader(open('admin.csv', "r"))
    for row in csv_file1:
        l.append(row)
        for i in l:
            for j in i:
                if username==j:
                    passwd=input("Enter the Password(Only Numbers Allowed):")
                    time.sleep(1)
                    for password in l:
                        for check in password:
                            if passwd==check:
                                time.sleep(1)
                                print("")
                                print("")
                                print("")
                                print("")
                                print("")
                                print("")
                                print("")
                                print("Welcome ",username)
                                print("")
                                print("")
                                print(line2)
                                print("1. View All Orders")#starting.csv
                                print("2. Track Order Status")
                                print(line2)
                                resp69=3
                                while resp69==3:
                                    resp69=int(input("Select 1 Or 2:"))
                                while resp69==1:
                                    resp69=3
                                    print("All Orders:")
                                    print("")
                                    df2= pd.read_csv("starting.csv", delimiter=",")
                                    print(df2)
                                while resp69==2:
                                    resp69=3
                                    print("")
                                    print("")
                                    track=input("Enter the Order Number:")
                                    time.sleep(1)
                                    print("")
                                    print("")
                                    tk=0
                                    csv_file = csv.reader(open('starting.csv', "r"))
                                    for row in csv_file:
                                                if track == row[5].strip():
                                                    print("-------------------------------------------------------")
                                                    print("ORDER STATUS")
                                                    print("")
                                                    print("Name: ",row[2])
                                                    print("Status: ",row[13])
                                                    print("-------------------------------------------------------")
                                                    tk=1
                                                    print("")
                                                    time.sleep(2)
                                                    print("Reloading Back in 5 Seconds")
                                                    time.sleep(5)
                                                    print("")
                                                    print("")
                                                    print("")
                                                    print("")
                                                    print("")
                                                    print(headline)
                                                    print(headline1)
                                                    print(headline2)
                                                    print(headline3)
                                                    time.sleep(2)
                                                    close()
                                                    break
                                    if tk==0:
                                        print("")
                                        print("ORDER NUMBER DOES NOT EXIST")
                                        print("")
                                        time.sleep(2)
                                        print("Reloading Back in 5 Seconds")
                                        time.sleep(5)
                                        print("")
                                        print("")
                                        print("")
                                        print("")
                                        print("")
                                    else:
                                        print("wrong password")
                            
                        else:
                            print("Try Again")
                            username=0
    

user=int(input("Are You a Customer or Staff(Enter 1 or 2):"))

while user != 1 and user != 2 and user !=0:
    error()
    user=int(input("Are You a Customer or Staff(Enter 1 or 2):"))
    
while user==1:
    starting()
while user==2: 
    admin()
while user==0:
    close()
