#Daksh

import csv
import mysql.connector as con
x=con.connect(host="localhost",user="root",password="Daksh@2705")
mycur=x.cursor()
mycur.execute("create database abd;")
mycur.execute("use abd;")
mycur.execute("create table login(Name varchar(20), usr varchar(20), pwd varchar(20))");
mycur.execute("create table cust(Name varchar(20), custname varchar(20), cash int(6), noc int(3));")
x.commit()
x.close()

with open ("review.dat","w") as f:
   pass

with open ("bill.csv","w",newline='') as f:
   a=['NAME','CUST_NAME','AMOUNT','NO_OF_CHANNELS']
   csv_w=csv.writer(f)
   csv_w.writerow(a)
