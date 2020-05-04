'''
Credential Manager script to work with credentials.

@author: Harish Karthic
@date: 17/01/2020
'''

import os, random, json


class CredentialManager():

    '''
    Credential Manager to generate random password, encrypt and
    decrypt it. Also, save it in a file for remote authentication.
    By default password of length 10 will be generated if no
    value is passed.

    Credentials.json file will be created if default save credentials
    option is selected.
    '''

    def __init__(self):
        pass

    def getpassword(self, password_length=10):
        '''
        Generate random password. Specify the length of password that
        has to be generated.
        '''

        self.password_length = password_length

        chars = list(map(chr, range(33, 123)))
        password = ""
        i = 0

        while i < self.password_length:
            password += random.choice(chars)
            i += 1

        return password

    def encrypt(self, password):
        '''
        Encrypts the password.
        '''

        self.password = password
        encrypt = ""
        for char in self.password:
            encrypt += "^" + hex(ord(char))

        return encrypt

    def decrypt(self, encrypted_password):
        '''
        Decrypts the password.
        '''

        self.encrypted_password = encrypted_password
        decrypt = ""
        for value in self.encrypted_password.strip("^").split("^"):
            decrypt += chr(int(value, 16))

        return decrypt

    def default_credentials(self):

        user_name = os.getlogin()

        result = {
            "Domain": os.environ['userdomain'],
            "username": f"{os.environ['userdomain']}\{user_name}",
            "password": self.encrypt(self.password)
        }

        return result

    def save_credentials(self, file, credentials):
        '''
        Saves the credentials in a file.
        '''

        self.file = file
        self.credentials = credentials

        file = open(self.file, "w+")
        file.write(json.dumps(self.credentials))
        file.close()

        return f"Credentials are saved in given path {self.file}"

    def save_default_credentials(self):

        self.save_credentials("Credentials.json", self.default_credentials())
        return "Default credentials are saved in Credentials.json"
