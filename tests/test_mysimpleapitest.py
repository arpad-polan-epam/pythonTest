import requests

# this is a simple rest api call to verify the return code and the message
def test_dog():
    response = requests.get("https://api.thedogapi.com/")
    assert response.status_code == 200
    assert "Dog" in response.text
    print(response.text)

# this is the same as befor but with failing assertion on return code
def test_dog2():
    response = requests.get("https://api.thedogapi.com/")
    assert response.status_code == 100
    assert "Dog" in response.text
    print(response.text)
