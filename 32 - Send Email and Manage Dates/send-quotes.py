import smtplib
import datetime as dt
import random

MY_EMAIL = "pyhtontests@gmail.com"
TO_EMAIL = "sidneyshafer01@gmail.com"
PASSWORD = "ogiqegchotblygwa"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 5:
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        # add content to email by placing two line breaks (\n\n) after subject title
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_EMAIL,
            msg=f"Subject: Monday Motivation\n\n{quote}"
        )

