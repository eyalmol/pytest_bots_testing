import requests
from pytest import mark
import json


@mark.bot2
@mark.post
@mark.post_bot2
class PostBot2Tests:
    @staticmethod
    def test_bot2_simple_post_method():
        url = 'http://localhost:4200/api/bot2'
        data = {"name": "bot2 post test", "id": "2500"}

        response = requests.post(url, json=data)
        print(response.status_code)
        date_response = response.json()
        assert (response.status_code == 200), "could not manage post bot2 task"

    @staticmethod
    def test_bot2_post_no_name():
        url = 'http://localhost:4200/api/bot2'
        data = {"id": "2600"}

        response = requests.post(url, json=data)
        print(response.status_code)
        data_response = response.json()
        assert (response.status_code == 422), "managed to post bot2 without name"

    @staticmethod
    def test_bo2_post_no_id():
        url = 'http://localhost:4200/api/bot2'
        data = {"name": "try to post no id"}

        response = requests.post(url, json=data)
        print(response.status_code)
        data_response = response.json()
        assert (response.status_code == 422), "managed to post bot2 without id"

    @staticmethod
    def test_bot2_post_id_as_string():
        url = 'http://localhost:4200/api/bot2'
        data = {"name": "try id as string", "id": "thhk"}

        response = requests.post(url, json=data)
        print(response.status_code)
        data_response = response.json()
        assert (response.status_code == 422), "managed to post bot2 with id as a string"
