import smtplib
import datetime as dt
import random

now = dt.datetime.now()
current_day = now.weekday()

if current_day == 2:
    with open("day_32/quotes.txt", "r") as file:
        quotes = file.readlines()
        today_quote = random.choice(quotes)
        
    my_email = "**************"
    password = "**************"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="******************", msg=f"Subject:Yours today quote:\n\n{today_quote}")
