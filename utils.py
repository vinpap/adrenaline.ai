import os
import hashlib
import binascii
from datetime import date

import mysql.connector

def hash_new_password(pwd: str):
    hasher = hashlib.sha256()
    salt = os.urandom(32).hex()
    encoded_salt = salt.encode()
    pwd = pwd.encode()
    hasher.update(pwd + encoded_salt)
    hashed_pwd = hasher.hexdigest()
    return hashed_pwd, salt

def check_password(email: str, pwd: str):
    """
    Returns True if the password entered by an user is valid, False otherwise.
    """
    with mysql.connector.connect(
        host=os.environ["MYSQL_HOST"],
        user=os.environ["MYSQL_USER"],
        password=os.environ["MYSQL_PWD"],
        database=os.environ["MYSQL_DB_NAME"],
    ) as db:
        with db.cursor() as c:
            query = f"""SELECT * FROM users WHERE email = '{email}'""" # Attention aux possibles injectinos SQL (e.g. si l'e-mail entré contient des guillemets)
            c.execute(query)
            results = c.fetchall()
            if not results:
                 raise ValueError(f"Email {email} does not match any recorded user")
            stored_hash = results[0][5]
            stored_salt = results[0][6].encode()
            
            entered_pwd_hasher = hashlib.sha256()
            pwd = pwd.encode()
            
            entered_pwd_hasher.update(pwd + stored_salt)
            entered_pwd = entered_pwd_hasher.hexdigest()
            if entered_pwd == stored_hash.decode():
                 return True
            return False






def user_exists(email: str):
    """
    Returns True if the user already exists in the database, False otherwise.
    """

    with mysql.connector.connect(
            host=os.environ["MYSQL_HOST"],
            user=os.environ["MYSQL_USER"],
            password=os.environ["MYSQL_PWD"],
            database=os.environ["MYSQL_DB_NAME"],
        ) as db:
            with db.cursor() as c:
                query = f"""SELECT * FROM users WHERE email = '{email}'""" # Attention aux possibles injectinos SQL (e.g. si l'e-mail entré contient des guillemets)
                c.execute(query)
                results = c.fetchall()

                if results: 
                     return True
                
                return False

def save_user(first_name: str, last_name: str, email: str, hash: str, salt: str):
    """
    Inserts user information in the database.
    """
    with mysql.connector.connect(
            host=os.environ["MYSQL_HOST"],
            user=os.environ["MYSQL_USER"],
            password=os.environ["MYSQL_PWD"],
            database=os.environ["MYSQL_DB_NAME"],
        ) as db:
            with db.cursor() as c:
                current_date = date.today().strftime("%Y-%m-%d")

                query = f"""INSERT INTO users (email, last_name, first_name, password_hash, signup_date, salt) VALUES ('{email}', '{last_name}', '{first_name}', '{hash}', '{current_date}', '{salt}');"""
                c.execute(query)
                db.commit()