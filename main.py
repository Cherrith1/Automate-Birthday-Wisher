##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import random
import smtplib

data = pandas.read_csv("birthdays.csv")
today = (dt.datetime.now().month, dt.datetime.now().day)

new_dict = {(index, data_row["month"], data_row["day"]):data_row for (index,data_row) in data.iterrows()}
print(new_dict)

for row in new_dict:
    if today == (row[1], row[2]):
        line = new_dict[row]
        num = random.randint(1,3)
        with open(f"letter_templates/letter_{num}.txt") as letter:
            text = letter.read()
            new_text = text.replace("[NAME]", f"{line['name']}")

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user="tesingtester02@gmail.com", password="ponnu@123")
            connection.sendmail(from_addr="tesingtester02@gmail.com", to_addrs="ponnulings@gmail.com",
                                msg=f"Subject:Happy Birthday\n\n{new_text}".encode("UTF-8"))




