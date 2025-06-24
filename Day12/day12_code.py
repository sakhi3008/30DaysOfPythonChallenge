# Challenge - Validate gmail addresses using regex

import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._]+@gmail\.com$'

    if re.match(pattern,email):
        return True
    else:
        return False

emails = ['example@gmail.com','invalid@yahoo.com','ab_c@gmail.com','username123@gmail.com']

for email in emails:
    if is_valid_email(email):
        print(f"{email} is a valid Gmail address.")
    else:
        print(f"{email} is not a valid Gmail address.")

