 # Simple Mail Transfer Protcol library (smtplib)





# steps 1- make a connection
# 2- secure connection
# 3- login
# 4- send the msg by putting email provider and reciver

"""
email = "20191700920@cis.asu.edu.eg" 
connection = smtp.SMTP('smtp-mail.outlook.com',port=587)# used to setup which mail company info will be used


connection.starttls()
connection.login(user=email,password='')
connection.sendmail(from_addr=email,
                    to_addrs='yousefalaa8190@gmail.com',
                    msg='subject:Testing\n\nThis is body of mail',)
connection.quit() 

# also can treat as with open close way

with smtp.SMTP('smtp-mail.outlook.com',port=587) as connection:
    connection.starttls()
    connection.login(user=email,password='')
    connection.sendmail(from_addr=email,
                        to_addrs='yousefalaa8190@gmail.com',
                        msg='subject:Testing\n\nThis is body of mail',)"""
    

##############################################
#work with datetime module



"""now = dt.datetime.now()
 print(now.year)
print(now.month)
print(now.weekday()) 

date_of_birth = dt.datetime(year=2001,day=1,month=1,hour=23,minute=59,second=59)
print(date_of_birth)"""
############################################
# Exercise 1
import smtplib as smtp
from email.message import EmailMessage
import datetime as dt
import random


with open('Birthday Wisher (Day 32) start/quotes.txt','r') as f:
    contents = f.read().split('\n')
    randomQuote = random.choice(contents)


email = "20191700920@cis.asu.edu.eg" 

with smtp.SMTP('smtp-mail.outlook.com',port=587) as connection: 
    connection.starttls()
    connection.login(email,password='Wtdbe6A92pU7Rm9')
    now = dt.datetime.now()
    if now.weekday() == 4:
        connection.sendmail(from_addr=email,
                            to_addrs='yousefalaa8190@gmail.com',
                            msg=f'subject:Motivation\n\n{randomQuote}')
    print()# friday is 4