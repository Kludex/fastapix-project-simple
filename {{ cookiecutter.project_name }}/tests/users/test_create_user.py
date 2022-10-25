from fastapi.testclient import TestClient

USERS_URL = "/api/v1/users"


def test_create_user(client: TestClient) -> None:
    payload = {"email": "potato@gmail.com", "password": "password"}
    response = client.post(f"{USERS_URL}/", json=payload)
    assert response.status_code == 200
    assert "potato@gmail.com" == response.json().get("email")


def test_create_user_already_exists(client: TestClient) -> None:
    payload = {"email": "alice@gmail.com", "password": "password"}
    response = client.post(f"{USERS_URL}/", json=payload)
    assert response.status_code == 409
    assert response.json() == {"detail": "Email already exists."}
