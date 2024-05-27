"""
Unit tests for the app itself.
"""
import pytest
from flask import session

from app import app

@pytest.fixture()
def test_app():
    test_app = app
    test_app.config.update({
        "TESTING": True,
    })

    yield test_app

@pytest.fixture()
def client(test_app):
    return test_app.test_client()

def test_index(client):
    """
    Tests the root path by making sure it redirects to the 
    correct page (/dashboard if the user is signed in,
    /sign_in otherwise).
    """

    response = client.get("/", follow_redirects=True)
    assert response.request.path == "/sign_in"


    with client.session_transaction() as session:
        session["username"] = "TEST_USER"
    signed_in_response = client.get("/", follow_redirects=True)
    assert signed_in_response.request.path == "/dashboard"

def test_sign_in(client):
    """
    Unit test for /sign_in.
    """

    # Wrong username and password
    form_data = {
        "username": "user or 1=1",
        "password": "qwertyuiopasdfghjklzxcvbnm"
    }
    response = client.post("/sign_in", follow_redirects=True, data=form_data)
    assert response.request.path == "/sign_in"

    # Right username, wrong password
    form_data = {
        "username": "TEST",
        "password": "qwertyuiopasdfghjklzxcvbnm"
    }
    response = client.post("/sign_in", follow_redirects=True, data=form_data)
    assert response.request.path == "/sign_in"

    # Right username, right password
    form_data = {
        "username": "TEST",
        "password": "TEST"
    }
    response = client.post("/sign_in", follow_redirects=True, data=form_data)
    assert response.request.path == "/dashboard"


def test_sign_up(client):
    """
    Unit test for /sign_up.
    """
    # Using a username that already exists
    form_data = {
        "username": "TEST",
        "first_name": "TEST",
        "surname": "TEST",
        "password": "TEST"
    }
    response = client.post("/sign_up", follow_redirects=True, data=form_data)
    assert response.request.path == "/sign_up"

def test_logout(client):
    """
    Unit test for /logout.
    """
    with client:
        response = client.get("/logout", follow_redirects=True)
        assert response.request.path == "/sign_in"
        assert "username" not in session


def test_dashboard(client):
    """
    Unit test for /dashboard.
    """
    # Trying to access te dashboard without being signed in
    with client.session_transaction() as session:
        if "username" in session:
            session.pop("username")
    response = client.get("/dashboard", follow_redirects=True)
    assert response.request.path == "/sign_in"


def test_recommended_workout(client):
    """
    Unit test for /recommended_workout.
    """

    # Trying to access te dashboard without being signed in
    with client.session_transaction() as session:
        if "username" in session:
            session.pop("username")
    response = client.get("/recommended_workout", follow_redirects=True)
    assert response.request.path == "/sign_in"


