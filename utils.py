import os
import hashlib
import binascii
from datetime import date, timedelta

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

def retrieve_data(username: str):
    """
    Retrieves and returns distance and calories data for 'username' in the database.
    """

    # ATTENTION : CODE À MODIFIER POUR NE RÉCUPÉRER QUE LES DONNÉES QUI CORRESPONDENT À L'UTILISATEUR

    with mysql.connector.connect(
            host=os.environ["MYSQL_HOST"],
            user=os.environ["MYSQL_USER"],
            password=os.environ["MYSQL_PWD"],
            database=os.environ["MYSQL_DB_NAME"],
        ) as db:
            with db.cursor() as c:
                # Faire une liste de dates qui couvre les 28 derniers jours
                # Pour chaque jour, faire une requête dans calories_burnt et une autre dans distance
                # Si on trouve une valeur, on la stocke pour la renvoyer
                # Sinon, on stocke un zéro
                days_to_consider = 28
                dates = []
                distances = []
                calories = []

                current_date = date.today()
                for day_count in range(days_to_consider):
                    dates.append(current_date.strftime("%Y-%m-%d"))
                    distance_query = f"""SELECT distance FROM distance WHERE record_date = '{current_date}';"""
                    c.execute(distance_query)
                    results = c.fetchall()
                    if results:
                        distances.append(results[0][0])
                    else:
                        distances.append(0)

                    calories_query = f"""SELECT calories_burnt FROM calories_burnt WHERE record_date = '{current_date}';"""
                    c.execute(calories_query)
                    results = c.fetchall()
                    if results:
                        calories.append(results[0][0])
                    else:
                        calories.append(0)

                    current_date = current_date - timedelta(days=1)

    
                return {
                    "dates": dates,
                    "distance": distances,
                    "calories": calories
                }