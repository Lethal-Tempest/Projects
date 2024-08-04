#Daksh
import csv
import pickle
import mysql.connector as con
x=con.connect(host="localhost",user="root",password="Daksh@2705",database="abd")
mycur=x.cursor()

def cya():                                #cya--> Create Your Account
   nam=input("Enter your name: ")         #python mysql connectivity
   us=input("Enter your username: ")
   pd=input("Enter your password: ")
   mycur.execute('insert into login values("'+nam+'","'+us+'","'+pd+'");')
   x.commit()
   print("Account Created Succesfully!")
   menu()

def bill():                               #bill--> Sends details of the bill to be generated to bill.csv         
   a=input("Enter your name: ")           #csv file handling
   b=input("Enter customer's name: ")
   c=int(input("Enter the amount of payment to be recieved: "))
   d=int(input("Enter number of channels to be added "))
   with open ("bill.csv","a",newline='') as f:
      z=[a,b,c,d]
      csv_w=csv.writer(f,delimiter=',')
      csv_w.writerow(z)
   print("Bill details have been succesfully updated")
   menu2()

def tr():                                 #tr--> Taking Review (binary file handling)
   with open ("review.dat","ab") as f:
      print("Please tell how much you liked our service ")
      y=input("Enter Customer's name: ")
      z=int(input("Please rate out of 10 "))
      q=[y,z]
      pickle.dump(q,f)
      print("Thank you so much for giving your precious time to us.")
   menu2()

def rr():                                 #rr--> Reading Review (binary file handling)                      
   with open ("review.dat","rb") as f:
      string="{0:<15}{1:<5}"
      print(string.format("Customer","Rating"))
      while True:
         try:
            data=pickle.load(f)
            print(string.format(data[0],data[1]))
         except EOFError:
            break
   menu2()

def retry():                                #part of update
   ans=input("The given name is not in the database, do you want to retry (y/n):")
   if ans=='y':
      update()
   elif ans=='n':
      print("Ok")
   else:
      print("Please enter a valid option")
      retry()
   
def update():                             #update--> Updates name of the person
   nam=input("Enter name which needs to be editted ")
   mycur.execute("select * from login;")
   data=mycur.fetchall()
   s=0
   for row in data:
      if nam==row[0]:
         s+=1
         newnam=input("Enter the name which will be added ")
         mycur.execute('update login set Name="'+newnam+'" where Name="'+nam+'";')
         x.commit()
         print("Changes made successfully!")
   if s==0:
      retry()
      
   menu2()

def menu2():                              #menu2--> menu shown after you login
   print(" ")
   print("Press")
   print("1 to see the details of the workers")
   print("2 to update details of the workers")
   print("3 to generate bill")
   print("4 to take review from the user")
   print("5 to see the reviews from all the users")
   print("0 to logout")

   com=int(input("Enter your command "))
   if com==1:                                      #calling all the funtions defined above
      mycur.execute("select * from login;")
      r=mycur.fetchall()
      for i in r:
         print(i)
      menu2()
   elif com==2:
      update()
   elif com==3:
      bill()
   elif com==4:
      tr()
   elif com==5:
      rr()
   elif com==0:
      menu()

def login():                                       #the option which checks for login
   mycur.execute("select * from login;")           #python mysql connectivity
   r=mycur.fetchall()
   nam=input("Enter your name ")
   us=input("Enter your username ")
   pd=input("Enter your password ")
   for i in r:
      if i[0]==nam and i[1]==us and i[2]==pd:
         print("********************************WELCOME TO DAKSH CABLE MANAGEMENT SYSTEM**********************")
         print("What do you want to do today? ")
         menu2()
         break
   else:
      print("Your credentials dont match the data in our database")
      menu()
            

def menu():                               #menu for the person to enter his credentials to gain access
   print(" ")
   print("Press")
   print("1 to Log in")
   print("2 to create your account")
   print("3 to exit")
   print(" ")
   ans=int(input("enter your choice: "))
   if ans==1:
      login()
   elif ans==2:
      cya()
   elif ans==3:
      print("Thank you")
   else:
      print("Please enter valid option ")
      menu()

menu()

