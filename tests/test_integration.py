from sqlalchemy import text

from app import app, db


def test_database_connection():
    with app.app_context():
        result = db.session.execute(text("SELECT 1")).scalar()
        assert result == 1


def test_home_page():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"Celsius to Fahrenheit" in response.data
    assert b"TempConverter" in response.data
    assert b"Luka Badzek" in response.data
    assert b"Algebra Bernays University" in response.data