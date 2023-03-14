import smtplib

my_email = "pyhtontests@gmail.com"
to_email = "sidneyshafer01@gmail.com"
# password generated from the my_email email
password = "ogiqegchotblygwa"

# --- SMTP INFO : --- #
# Gmail - smtp.gmail.com
# Hotmail - smtp.live.com
# Yahoo - smtp.mail.yahoo.com
with smtplib.SMTP("smtp.gmail.com") as connection:
    # makes connection secure
    connection.starttls()
    # login
    connection.login(user=my_email, password=password)
    # send email
    connection.sendmail(from_addr=my_email, to_addrs=to_email,
                        msg="Subject:Hello There\n\nThis is an email sent using Python :)\n\nBest,\n\nSidney Shafer")


