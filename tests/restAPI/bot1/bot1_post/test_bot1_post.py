import requests
import json
from pytest import mark


@mark.bot1
@mark.post
@mark.post_bot1
class PostBot1Tests:

    @staticmethod
    def test_bot1_simple_post_method():
        url = 'http://localhost:4200/api/bot1'
        data = {"name": "someBot1", "id": "1500"}

        response = requests.post(url, json=data)
        print(response.status_code)
        date_response = response.json()
        assert (response.status_code == 200), "could not manage post bot1 task"

    @staticmethod
    def test_bot1_post_no_name():
        url = 'http://localhost:4200/api/bot1'
        data = {"id": "1600"}

        response = requests.post(url, json=data)
        print(response.status_code)
        data_response = response.json()
        assert (response.status_code == 422), "manage to post bot1 without name"

    @staticmethod
    def test_bo1_post_no_id():
        url = 'http://localhost:4200/api/bot1'
        data = {"name": "try to post no id"}

        response = requests.post(url, json=data)
        print(response.status_code)
        data_response = response.json()
        assert (response.status_code == 422), "manage to post bot1 without id"

    @staticmethod
    def test_bot1_post_id_as_string():
        url = 'http://localhost:4200/api/bot1'
        data = {"name": "try id as string", "id": "thhk"}

        response = requests.post(url, json=data)
        print(response.status_code)
        data_response = response.json()
        assert (response.status_code == 422), "manage to post bot1 with id as a string"

    @staticmethod
    def test_bot1_post_name_as_number():
        url = 'http://localhost:4200/api/bot1'
        data = {"name": "777", "id": "5615"}
        response = requests.post(url, json=data)
        print(response.status_code)
        data_response = response.json()
        assert (response.status_code == 422), "manage to post bot1 with name as a number"
