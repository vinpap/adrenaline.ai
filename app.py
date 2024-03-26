import os

from flask import Flask, session, redirect, render_template, request, flash
import mysql.connector

from utils import hash_new_password


app = Flask(__name__)

@app.route("/")
def index():
    """
    Redirects to the dashboard if the user is logged in, and to
    the sign-in page otherwise.
    """
    if "first_name" in session:
        return redirect("/dashboard")
    return redirect("/sign_in")

@app.route("/sign_in", methods = ['POST', 'GET'])
def sign_in():
    """
    Returns the sign in page.
    """
    if request.method == "POST":
        # On vérifie que l'utilisateur existe et a entré les bonnes infos
        with mysql.connector.connect(
            host=os.environ["MYSQL_HOST"],
            user=os.environ["MYSQL_USER"],
            password=os.environ["MYSQL_PWD"],
            database=os.environ["MYSQL_DB_NAME"],
        ) as db:
            # Regarder le salt qui correspond à l'e-mail entré
            # Calculer le hash du mdp entré + du salt

            # Si tout est ok, on change les variables de session pour log l'utilisateur
            pass
            
    
    return render_template("sign_in.html")

@app.route("/sign_up", methods = ['POST', 'GET'])
def sign_up():
    """
    Returns the sign up page.
    """
    if request.method == "POST":
        with mysql.connector.connect(
            host=os.environ["MYSQL_HOST"],
            user=os.environ["MYSQL_USER"],
            password=os.environ["MYSQL_PWD"],
            database=os.environ["MYSQL_DB_NAME"],
        ) as db:
            # Regarder si l'email est déjà enregistré
            query = f"""SELECT * FROM users WHERE email = '{request.form["username"]}'""" # Attention aux possibles injectins SQL (e.g. si l'e-mail entré contient des guillemets)

            # Stocker le mdp dans la BDD
            hash, salt = hash_new_password(request.form["password"])
    msg = "Test des messages Flash"        
    return render_template("sign_up.html", msg=msg)

@app.route("/logout")
def logout():
    """
    Logs out the user.
    """
    # Effacer les valeurs de la session ici
    return redirect("/sign_in")

@app.route("/privacy")
def privacy():
    """
    Returns the privacy page.
    """
    return render_template("privacy.html")

@app.route("/contact")
def contact():
    """
    Returns the contact page.
    """
    return render_template("contact.html")

@app.route("/dashboard")
def dashboard():
    """
    Returns the dashboard.
    """
    return render_template("dashboard.html")

@app.route("/recommended_workout")
def recommended_workout():
    """
    Returns page displaying the recommended workout for the user.
    """
    return render_template("recommended_workout.html")