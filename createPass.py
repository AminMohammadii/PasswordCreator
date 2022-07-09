import string
from random import choices


# create the password (if no argument received, automatically create 8 character contain upper & lower)
def create_password(length=8, upper=False, lower=False, digit=False, pun=False):
    pool = ''

    if upper:
        pool += string.ascii_uppercase

    if lower:
        pool += string.ascii_lowercase

    if digit:
        pool += string.digits

    if pun:
        pool += string.punctuation

    if pool == '':
        pool = string.ascii_letters

    password = ''.join(choices(pool, k=length))

    return password
