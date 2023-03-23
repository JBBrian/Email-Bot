import smtplib
import os
import random

SENDER = "pythonburnermail@yahoo.com"
AUTH = os.environ.get("ETOKEN")
TARGET = "theemailaddress70@gmail.com"

with open("insults.txt") as source:
    lines = source.readlines()

body = f"Dear Brian,\n\n{random.choice(lines)}\nSincerely, \nYour Arch Nemesis"
message = f"Subject: I hope this message finds you well\n\n{body}"

print(f"--- SENDING.... ---\n\n{message}")

carrier = smtplib.SMTP("smtp.mail.yahoo.com", 587)
carrier.starttls()
carrier.login(SENDER, AUTH)
carrier.sendmail(SENDER, TARGET, message)
carrier.quit()

print("\n\n--- MESSAGE SENT SUCCESSFULLY ---")


