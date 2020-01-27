"""Hacked Passwords checker
   This script helps to identify the passwords that are hacked
   and returns a dictionary with number of times the passwords
   are hacked. 
   Suggests a strong password which is unhacked.
"""

import requests
import hashlib
import sys
import random


def get_response(query_password):

    url = "https://api.pwnedpasswords.com/range/" + query_password
    response = requests.get(url)
    return response.text


def encode_password(password):

    password_encode = hashlib.sha1(
        password.encode('utf-8')).hexdigest().upper()
    return password_encode


def trim_password(encoded_string):

    start, tail = encoded_string[:5], encoded_string[5:]
    return start, tail


def hacked_counts(hashed_passwords, hashes_check):
    hashed_counts = (passwords.split(":")
                     for passwords in hashed_passwords.splitlines())
    for hash_pass, count in hashed_counts:
        if hash_pass == hashes_check:
            return count
    return 0


def get_password(password_length=10):
    '''Generate random password. Specify the length of password that
        has to be generated.
    '''
    chars = list(map(chr, range(33, 123)))
    password = ""
    i = 0

    while i < password_length:
        password += random.choice(chars)
        i += 1

    return password


def suggest_password(random_password):

    encoded = encode_password(random_password)
    sec_pass = trim_password(encoded)
    hacked_pass_count = hacked_counts(get_response(sec_pass[0]), sec_pass[1])

    if hacked_pass_count == 0:
        return random_password
    else:
        return suggest_password(random_password)


def main(args):

    hacked_dict = {"UnhackedPassword": suggest_password(get_password())}
    for secure_string in args:

        encode = encode_password(secure_string)
        secure_pass = trim_password(encode)
        hack_counts = hacked_counts(
            get_response(secure_pass[0]), secure_pass[1])

        if hack_counts != 0:
            hacked_dict.update({secure_string: hack_counts})

        else:
            hacked_dict.update({secure_string: hack_counts})

    return hacked_dict


if __name__ == '__main__':
    print(main(sys.argv[1:]))
