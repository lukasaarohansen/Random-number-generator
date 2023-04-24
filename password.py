import secrets
import string

# define the alphabet
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabet = special_chars + digits + letters

pwd_length = 12

#password string
pwd = ''
for i in range(pwd_length):
    pwd += ''.join(secrets.choice(alphabet))

print(pwd)

#create password with constraints
while True:
    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))

    if (any(char in special_chars for char in pwd) and
        sum(char in digits for char in pwd)>=2):
        break
print(pwd)