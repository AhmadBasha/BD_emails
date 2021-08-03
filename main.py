############## IMPORTS ##############
import smtplib
import datetime as dtime
import pandas as pd
import random
import time
from email.mime.text import MIMEText
from img_sources.gif_images import gif_images
############## Reading Data and Check Current Day & Month ##############
# read the data
df = pd.read_csv("birthdays.csv")
# current day and month
current_day = dtime.datetime.now().day
current_month = dtime.datetime.now().month

############## LOGIC ##############
# save the rows that has the current day in new variable
new_df = df.loc[df['day'] == current_day]
# check the length of new_df of the current month so if the result is larger than 1
# so there is birthdays on this day
if len(new_df.loc[new_df['month'] == current_month]) > 0:
    # check the length of people having birthday in this day
    for i in range(len(new_df.loc[new_df['month'] == current_month])):
        # open a random html file for the three files that existed
        with open(f"./birthd_letters/letter_{random.randint(1, 3)}.html") as letter_file:
            # reading the file
            letter_contents = letter_file.read()
            # replace [NAME] with actual name on the data
            the_letter = letter_contents.replace("[NAME]", new_df["name"][i])
            # here to replace the GIF from the imported pyhton files
            the_letter = the_letter.replace("[GIF IMAGE]", random.choice(gif_images))
            # here start using smtplib package to send the letter
            # new connection
            with smtplib.SMTP("smtp.gmail.com") as con:
                # secure the mail
                con.starttls()
                # login
                con.login(user="Ahmedbashatest1@gmail.com", password="")
                # create the msg
                msg = MIMEText(the_letter, 'html')
                msg["From"] = "Ahmedbashatest1@gmail.com"
                msg["To"] = new_df["email"][i]
                msg["Subject"] = "Happy Birthday !!!🎊"
                # send the email
                con.send_message(msg)
                # time delay to avoid closing google account
                time.sleep(10)
