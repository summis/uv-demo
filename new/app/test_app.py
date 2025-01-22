import pytest

from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        app.testing = True
        yield client


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Optimize" in response.data


def test_button_click(client):
    response = client.post("/optimize")
    assert response.status_code == 302
