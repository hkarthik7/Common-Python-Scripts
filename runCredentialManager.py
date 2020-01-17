from credential_manager import CredentialManager

cred_man = CredentialManager()

# random password
new_password = cred_man.getpassword()

# print random password
print(new_password)

# encrypt password
enc_password = cred_man.encrypt(new_password)

# print encrypted password
print(enc_password)

# decrypt password
dec_password = cred_man.decrypt(enc_password)

# print decrypted password
print(dec_password)

# print default credentials
print(cred_man.default_credentials())

def_cred = cred_man.default_credentials()

print(cred_man.decrypt(def_cred['password']))

# save password
print(cred_man.save_credentials("password.xml", new_password))

# save default credentials
print(cred_man.save_default_credentials())
