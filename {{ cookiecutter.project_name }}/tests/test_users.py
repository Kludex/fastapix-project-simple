from fastapi.testclient import TestClient

USERS_URL = "/api/v1/users"


def test_get_users(client: TestClient) -> None:
    response = client.get(USERS_URL)
    assert response.status_code == 200
    assert response.json() == [{"name": "Alice"}, {"name": "Bob"}]


def test_get_user(client: TestClient) -> None:
    response = client.get(f"{USERS_URL}/1")
    assert response.status_code == 200
    assert response.json() == {"name": "Alice"}


def test_create_user(client: TestClient) -> None:
    response = client.post(USERS_URL)
    assert response.status_code == 200
    assert response.json() == {"name": "Alice"}


def test_update_user(client: TestClient) -> None:
    response = client.put(f"{USERS_URL}/1")
    assert response.status_code == 200
    assert response.json() == {"name": "Alice"}
