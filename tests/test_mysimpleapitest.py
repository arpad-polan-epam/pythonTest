import requests

# this is a simple rest api call to verify the return code and the message
def test_dog():
    response = requests.get("https://api.thedogapi.com/")
    assert response.status_code == 200
    assert "Dog" in response.text
    print(response.text)


