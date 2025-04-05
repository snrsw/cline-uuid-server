import uuid
import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_get_uuid():
    """Test that the /uuid endpoint returns a valid UUID4 string"""
    response = client.get("/uuid")
    assert response.status_code == 200
    # Verify the response is a valid UUID4
    uuid_value = response.text.strip('"')  # Remove any quotes
    assert uuid.UUID(uuid_value, version=4)


def test_get_uuid_json():
    """Test that the /uuid/json endpoint returns a valid UUID4 in JSON format"""
    response = client.get("/uuid/json")
    assert response.status_code == 200
    data = response.json()
    assert "uuid" in data
    # Verify the UUID is valid
    assert uuid.UUID(data["uuid"], version=4)


def test_get_batch_uuids_default():
    """Test that the /uuid/batch endpoint returns a single UUID by default"""
    response = client.get("/uuid/batch")
    assert response.status_code == 200
    data = response.json()
    assert "uuids" in data
    assert len(data["uuids"]) == 1
    # Verify the UUID is valid
    assert uuid.UUID(data["uuids"][0], version=4)


def test_get_batch_uuids_custom_count():
    """Test that the /uuid/batch endpoint returns the requested number of UUIDs"""
    count = 5
    response = client.get(f"/uuid/batch?count={count}")
    assert response.status_code == 200
    data = response.json()
    assert "uuids" in data
    assert len(data["uuids"]) == count
    # Verify all UUIDs are valid
    for uuid_str in data["uuids"]:
        assert uuid.UUID(uuid_str, version=4)


def test_get_batch_uuids_max_count():
    """Test that the /uuid/batch endpoint handles the maximum count correctly"""
    count = 100
    response = client.get(f"/uuid/batch?count={count}")
    assert response.status_code == 200
    data = response.json()
    assert len(data["uuids"]) == count


def test_get_batch_uuids_invalid_count():
    """Test that the /uuid/batch endpoint validates the count parameter"""
    # Test with count > 100
    response = client.get("/uuid/batch?count=101")
    assert response.status_code == 422  # Validation error

    # Test with count < 1
    response = client.get("/uuid/batch?count=0")
    assert response.status_code == 422  # Validation error
