import smtplib
import os
import random

# CREATING CONSTANTS
SENDER = BOT_EMAIL
AUTH = os.environ.get("ETOKEN")
TARGET = TARGET_EMAIL

# CONVERTING DATA IN .TXT TO LIST OF LINES
with open("insults.txt") as source:
    lines = source.readlines()

# CREATING MESSAGE
body = f"Dear Jeff,\n\n{random.choice(lines)}\nSincerely, \nYour Arch Nemesis"
message = f"Subject: I hope this message finds you well\n\n{body}"

print(f"--- SENDING.... ---\n\n{message}")

# SENDING MESSAGE
carrier = smtplib.SMTP("smtp.mail.yahoo.com", 587)
carrier.starttls()
carrier.login(SENDER, AUTH)
carrier.sendmail(SENDER, TARGET, message)
carrier.quit()

print("\n\n--- MESSAGE SENT SUCCESSFULLY ---")


