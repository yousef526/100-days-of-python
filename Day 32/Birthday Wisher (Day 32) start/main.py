##################### Extra Hard Starting Project ######################
import pandas as pd
import random
import datetime as dt
import smtplib as smtp
# 1. TODO Update the birthdays.csv
df = pd.read_csv('birthdays.csv')
now = dt.datetime.now()


# 2. Check if today matches a birthday in the birthdays.csv
if now.month in list( df['month']):
    month_df = df[df['month'] == now.month]
    if now.day in list(month_df['day']):
        birthday_persons = month_df[month_df['day'] == now.day]
        print(birthday_persons)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
letters = []
x = 3
while x > 0:
    with open(f'letter_templates/letter_{x}.txt') as f:
        letters.append(f.read())
        x -= 1

# 4. Send the letter generated in step 3 to that person's email address.


persons = birthday_persons['name'].values
email = "20191700920@cis.asu.edu.eg" 

for person in persons:
    randomQuote = random.choice(letters)
    randomQuote = randomQuote.replace('[NAME]',person)
    with smtp.SMTP('smtp-mail.outlook.com',port=587) as connection: 
        connection.starttls()
        connection.login(email,password='Wtdbe6A92pU7Rm9')
        connection.sendmail(from_addr=email,
                            to_addrs='yousefalaa8190@gmail.com',
                            msg=f'subject:Motivation\n\n{randomQuote}')
