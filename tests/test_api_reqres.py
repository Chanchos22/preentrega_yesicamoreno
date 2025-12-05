import requests
from utils.logger import logger

# GET
def test_get_echo():
    url = "https://postman-echo.com/get?foo=bar"
    logger.info(f"GET → {url}")
    response = requests.get(url)

    assert response.status_code == 200
    data = response.json()
    assert data["args"]["foo"] == "bar"


# POST
def test_post_echo():
    url = "https://postman-echo.com/post"
    payload = {"name": "Yesica", "role": "QA"}

    logger.info(f"POST → {url}")
    response = requests.post(url, json=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["json"]["name"] == "Yesica"
    assert data["json"]["role"] == "QA"


# DELETE
def test_delete_echo():
    url = "https://postman-echo.com/delete"
    logger.info(f"DELETE → {url}")
    response = requests.delete(url)

    assert response.status_code == 200



