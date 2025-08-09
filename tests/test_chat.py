import os
import sys
import pytest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from app import app


def test_chat_missing_message():
    with app.test_client() as client:
        response = client.post("/chat", json={})
        assert response.status_code == 400
        data = response.get_json()
        assert "message" in data["error"]


def test_chat_non_json_request():
    with app.test_client() as client:
        response = client.post("/chat", data="plain text", content_type="text/plain")
        assert response.status_code == 400
