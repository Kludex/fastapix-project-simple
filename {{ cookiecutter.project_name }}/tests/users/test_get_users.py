from fastapi.testclient import TestClient

USERS_URL = "/api/v1/users"


def test_get_users(client: TestClient) -> None:
    response = client.get(f"{USERS_URL}/")
    assert response.status_code == 200
    assert response.json() == [
        {"email": "alice@gmail.com", "id": 1},
        {"email": "robin@gmail.com", "id": 2},
    ]
