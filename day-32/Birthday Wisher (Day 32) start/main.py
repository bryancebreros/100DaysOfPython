import os
import smtplib
import datetime as dt

my_email = os.environ["EMAIL"]
password = os.environ["email_pass"]
now = dt.datetime.now()
if now.weekday() == 5:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="cebrerosbryan@gmail.com", msg="Subject:Frase\n\nMi momento ha llegado.\nOogway, Kung Fu Panda.")

