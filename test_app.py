# test_app.py
import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test that home page loads correctly"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"ACEest Fitness and Gym" in response.data

def test_add_workout_requires_fields(client):
    """Test that missing fields returns error"""
    response = client.post("/add_workout_form", data={})
    assert response.status_code == 400

def test_add_and_view_workout(client):
    """Test adding and viewing workouts by Gym ID"""
    # Add a workout
    response = client.post("/add_workout_form", data={
        "gym_id": "101",
        "workout": "running",
        "duration": "30"
    })
    assert response.status_code == 302  # redirect to home

    # View workouts for Gym ID
    response = client.post("/view_workouts", data={"gym_id": "101"})
    assert response.status_code == 200
    assert b"running" in response.data
    assert b"30 minutes" in response.data

