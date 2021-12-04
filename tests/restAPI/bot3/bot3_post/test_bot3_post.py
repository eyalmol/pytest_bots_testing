import requests
import json
from pytest import mark


@mark.post_bot3
class PostBot3Tests:

    # @staticmethod
    # def test_bot3_simple_post_method():
    #     url = 'http://localhost:4200/api/bot3'
    #     data = {"name": "adult bot3", "id": "3000", "username": "bot3adult_user", "password": "33333"}
    #
    #     response = requests.post(url, json=data)
    #     print(response.status_code)
    #     date_response = response.json()
    #     assert (response.status_code == 200), "could not manage post bot3 simple task"

    @staticmethod
    def test_bot3_post_no_name():
        url = 'http://localhost:4200/api/bot3'
        data = {"id": "3000", "username": "bot3adult_user", "password": "33333"}

        response = requests.post(url, json=data)
        print(response.status_code)
        date_response = response.json()
        assert (response.status_code == 422), "managed post bot3 no name"

    @staticmethod
    def test_bot3_post_no_id():
        url = 'http://localhost:4200/api/bot3'
        data = {"name": "bot3 not suppose to post", "username": "bot3adult_user", "password": "33333"}

        response = requests.post(url, json=data)
        print(response.status_code)
        date_response = response.json()
        assert (response.status_code == 422), "managed post bot3 without name"

    @staticmethod
    def test_bot3_post_no_usr_name():
        url = 'http://localhost:4200/api/bot3'
        data = {"name": "bot3 not suppose to post", "id": "14364654", "password": "33333"}

        response = requests.post(url, json=data)
        print(response.status_code)
        date_response = response.json()
        assert (response.status_code == 422), "managed post bot3 without providing username"

    @staticmethod
    def test_bot3_post_no_password():
        url = 'http://localhost:4200/api/bot3'
        data = {"name": "bot3 not suppose to post", "id": "14364654", "username": "kdhfko"}

        response = requests.post(url, json=data)
        print(response.status_code)
        date_response = response.json()
        assert (response.status_code == 422), "managed to post bot3 without providing password"

    @staticmethod
    def test_bot3_post_with_no_data():
        url = 'http://localhost:4200/api/bot3'

        response = requests.post(url)
        print(response.status_code)
        date_response = response.json()
        assert (response.status_code == 422), "managed to post bot3 without providing any data"

