import os

from flask import Flask, session, redirect, render_template, request, session, abort
import requests
import mysql.connector

from utils import hash_new_password, user_exists, save_user, check_password, retrieve_data


app = Flask(__name__)
print(os.environ)
app.secret_key = os.environ["FLASK_SESSION_KEY"]


@app.route("/")
def index():
    """
    Redirects to the dashboard if the user is logged in, and to
    the sign-in page otherwise.
    """
    if "username" in session:
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
            if not user_exists(request.form["username"]):
                msg = "Cet utilisateur n'existe pas" 
                return render_template("sign_up.html", msg=msg)
            if not check_password(request.form["username"], request.form["password"]):
                msg = "Wrong password, try again"
                return render_template("sign_in.html", msg=msg)
            session["username"] = request.form["username"]
            return redirect("/dashboard")  
    
    return render_template("sign_in.html")

@app.route("/sign_up", methods = ['POST', 'GET'])
def sign_up():
    """
    Returns the sign up page.
    """
    if "username" in session:
        return redirect("/dashboard")  
    if request.method == "POST":

        if user_exists(request.form["username"]):
            msg = "Cet utilisateur existe déjà dans la base de données" 
            return render_template("sign_up.html", msg=msg)
        
        # Stocker le mdp dans la BDD
        hash, salt = hash_new_password(request.form["password"])
        save_user(request.form["first_name"], request.form["surname"], request.form["username"], hash, salt)
        session["username"] = request.form["username"]
        return redirect("/dashboard")
      
    return render_template("sign_up.html")

@app.route("/logout")
def logout():
    """
    Logs out the user.
    """
    if "username" in session:
        session.pop("username")
    return redirect("/sign_in")

@app.route("/privacy")
def privacy():
    """
    Returns the privacy page.
    """
    if "username" in session:
        return render_template("privacy.html", user=session["username"])
    return render_template("privacy.html")

@app.route("/contact")
def contact():
    """
    Returns the contact page.
    """
    if "username" in session:
        return render_template("contact.html", user=session["username"])
    return render_template("contact.html")

@app.route("/dashboard")
def dashboard():
    """
    Returns the dashboard.
    """
    if "username" not in session:
        return redirect("/sign_in")
    
    # Récupérer les métriques de l'utilisateur dans la BDD
    # Les stocker dans une variable à passer au template
    user_data = retrieve_data(session['username'])
    return render_template("dashboard.html", user=session["username"], user_data=user_data)

@app.route("/recommended_workout")
def recommended_workout():
    """
    Returns page displaying the recommended workout for the user.
    """
    if "username" not in session:
        return redirect("/sign_in")
    
    # dummy workout, must be replaced with a call to the API that exposes the AI
    dummy_training = """
    Entraînement en fractionné\n
    Durée : 55 minutes\n
    Étapes :\n
    <ul>
    <li>15 min à 145 BPM - échauffement\n</li>
    <li>alterner 10 min à 170 BPM et 3 min à 145 BPM (répéter 3X)\n</li>
    <li>10 min à 145 BPM - récupération\n</li>
    </ul>
    Cet entraînement vous permettra de soutenir un effort intense sur de plus longues distances.
    """
    return render_template("recommended_workout.html", user=session["username"])

