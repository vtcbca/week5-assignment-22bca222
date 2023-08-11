#Write a python program create csv file student.csv(sid,sname,city,contact) using 10 records 
#(in which 5 records input directly and 5 records take input from user) write records into this file.
#Read this file using csv module and print it. 
#NOTE: Reading and writting must be perform using python script.

#ADDING FIELDS(HEADING) AND 5 RECORDS DIRECTLY IN CSV FILE:
import csv
with open('E:\\ANAMIKA\\ps github\\student.csv','w',newline='') as i :
    w=csv.writer(i)
    fields=['SID','SNAME','CITY','CONTACT']
    w.writerow(fields)
    rows=[[1,'om','surat',5675765766],[2,'sai','delhi',3365475365],[3,'radha','mumbai',73642364766],[4,'ram','ahemdabad',1233423434],[5,'kishan','vadodara',9786787687]]
    w.writerows(rows)

#TAKING INPUT OF 5 RECORDS THROUGH USER:    
from csv import writer
with open('E:\\ANAMIKA\\ps github\\student.csv','a',newline='') as i :
    w=csv.writer(i)
    l=[]
    for i in range(5):
        s_id=int(input("ENTER STUDENT ID:"))
        s_name=input("ENTER STUENT NAME:")
        city=input("ENTER CITY:")
        contact=input("ENTER STUDENT CONTACT NUMBER:")
        t=(s_id, s_name,city,contact)
        l.append(t)
    w.writerows(l)
    
#READING THIS FILE USING CSV MODULE AND PRINTING IT:
from csv import reader
with open('E:\\ANAMIKA\\ps github\\student.csv','r',newline='') as i :
    w=reader(i)
    for row in w:
        print(row)
