##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
import smtplib
import random

# 1. Update the birthdays.csv
df  = pd.read_csv("day_32/birthdays.csv")

new_info = {
    "name": {0: "Somebody"},
    "email": {0: "*************"},
    "year": {0: 1961},
    "month": {0: 1},
    "day": {0: 12}
}

data = pd.DataFrame(new_info)
data.to_csv("day_32/birthdays.csv")
new_data = data.to_dict()
name = new_data["name"][0]

# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
now = dt.datetime.now()
current_day = now.weekday()

if current_day == 3:
    letters_list = []
    for i in range(1, 4):
        with open(f"day_32/letter_templates/letter_{i}.txt", "r") as file:
            letter = file.read()
        letters_list.append(letter)

    random_letter = random.choice(letters_list)
    letter_to_send = random_letter.replace("[NAME]", name)

# 4. Send the letter generated in step 3 to that person's email address.
    my_email = "*******************"
    password = "*******************"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="*********************", msg=f"Subject:Happy Birthday!\n\n{letter_to_send}")
