import os

import hashlib

def hash_new_password(pwd: str):
    hasher = hashlib.sha256()
    salt = os.urandom(32)
    # Adding salt at the end of the password
    pwd = pwd.encode()
    hasher.update(pwd + salt)
    hashed_pwd = hasher.digest()
    return hashed_pwd, salt