from fastapi.testclient import TestClient

from api.main import app


client = TestClient(app)


VALID_PAYLOAD = {
    "pclass": 1,
    "age": 25,
    "sibsp": 0,
    "parch": 0,
    "fare": 80.0,
    "sex": "female",
    "embarked": "C",
    "class_name": "First",
    "who": "woman",
    "adult_male": False,
    "deck": "C",
    "embark_town": "Cherbourg",
    "alive": "yes",
    "alone": True
}


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert "message" in response.json()


def test_health():
    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "healthy"
    assert data["model_loaded"] is True


def test_predict_success():
    response = client.post(
        "/predict",
        json=VALID_PAYLOAD
    )

    assert response.status_code == 200

    data = response.json()

    assert "prediction" in data
    assert "prediction_label" in data
    assert "probability_negative" in data
    assert "probability_positive" in data

    assert data["prediction"] in [0, 1]

    assert 0 <= data["probability_negative"] <= 1
    assert 0 <= data["probability_positive"] <= 1


def test_predict_invalid_payload():
    invalid_payload = {
        "pclass": 99,
        "age": 25,
        "sibsp": 0,
        "parch": 0,
        "fare": 80.0,
        "sex": "female",
        "embarked": "C",
        "class_name": "First",
        "who": "woman",
        "adult_male": False,
        "deck": "C",
        "embark_town": "Cherbourg",
        "alive": "yes",
        "alone": True
    }

    response = client.post(
        "/predict",
        json=invalid_payload
    )

    assert response.status_code == 422