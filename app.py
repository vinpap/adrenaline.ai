from flask import Flask, session, redirect, render_template
from werkzeug.security import check_password_hash, generate_password_hash

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

@app.route("/sign_in")
def sign_in():
    """
    Returns the sign in page.
    """
    return render_template("sign_in.html")

@app.route("/sign_up")
def sign_up():
    """
    Returns the sign up page.
    """
    return render_template("sign_up.html")

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