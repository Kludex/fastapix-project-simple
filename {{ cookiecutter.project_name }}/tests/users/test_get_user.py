from fastapi.testclient import TestClient

USERS_URL = "/api/v1/users"


def test_get_user(client: TestClient) -> None:
    response = client.get(f"{USERS_URL}/1")
    assert response.status_code == 200
    assert response.json() == {"email": "alice@gmail.com", "id": 1}


def test_get_user_not_found(client: TestClient) -> None:
    response = client.get(f"{USERS_URL}/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}
