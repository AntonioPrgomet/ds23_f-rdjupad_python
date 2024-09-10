from api import API

api = API()

def test_api():
    assert isinstance(api.fetch_data(), list)