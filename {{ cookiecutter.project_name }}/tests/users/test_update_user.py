from fastapi.testclient import TestClient

USERS_URL = "/api/v1/users"


def test_update_user(client: TestClient) -> None:
    payload = {"email": "potato@gmail.com"}
    response = client.put(f"{USERS_URL}/1", json=payload)
    assert response.status_code == 200
    assert response.json() == {"email": payload["email"], "id": 1}


def test_update_user_already_exists(client: TestClient) -> None:
    payload = {"email": "robin@gmail.com"}
    response = client.put(f"{USERS_URL}/1", json=payload)
    assert response.status_code == 409
    assert response.json() == {"detail": "Email already exists."}


def test_update_user_not_found(client: TestClient) -> None:
    payload = {"email": "potato@gmail.com"}
    response = client.put(f"{USERS_URL}/999", json=payload)
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found."}
