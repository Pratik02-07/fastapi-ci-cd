import pytest
from fastapi.testclient import TestClient
from app import app
from app.models import Item
from app.database import get_db
from unittest.mock import MagicMock


@pytest.fixture
def mock_session_local():
    mock_db = MagicMock()
    mock_db.exec.return_value.all.return_value = [
        Item(
            id=1,
            name="Item 1",
            description="Item 1 description"
        ),
        Item(
            id=2,
            name="Item 2"
        )
    ]
    return mock_db


@pytest.fixture
def client(mock_session_local):
    def get_db_override():
        return mock_session_local

    app.dependency_overrides[get_db] = get_db_override

    with TestClient(app) as client:
        yield client

    app.dependency_overrides.clear()


def test_get_items(client, mock_session_local):
    response = client.get("/")

    assert response.status_code == 200

    items = response.json()

    assert len(items) == 2
    assert items[0]["name"] == "Item 1"
    assert items[0]["description"] == "Item 1 description"
    assert items[1]["name"] == "Item 2"

    mock_session_local.exec.assert_called_once()
