import requests
import json
from pytest import mark


@mark.put_bot1
class PutBot1Tests:
    @staticmethod
    def test_bot1_simple_put_method():
        url = 'http://localhost:4200/api/bot1/61ab5cc48ec3dbad1ff95152'
        data = {"intent": "[play_sound]", "permissionList": "[play_sound_permission]"}

        response = requests.put(url, json=data)
        print(response.status_code)
        date_response = response.json()
        assert (response.status_code == 200), "simple put method is not OK"

    @staticmethod
    def test_bot1_put_id_not_exist():
        url = 'http://localhost:4200/api/bot1/f95967'
        data = {"intent": "[jhejhjksahkjh]", "permissionList": "[play_sound_permission]"}
        response = requests.put(url, json=data)
        print(response.status_code)
        assert (response.status_code == 422), "manged to execute put method with no exist id"

    @staticmethod
    def test_bot1_put_no_id_provided():
        url = 'http://localhost:4200/api/bot1'
        data = {"intent": "[some intent]", "permissionList": "[play_sound_permission]"}
        response = requests.put(url, json=data)
        print(response.status_code)
        assert (response.status_code == 404), "manged to execute put method without providing id"

    @staticmethod
    def test_bot1_put_attribute_dont_exist():
        url = 'http://localhost:4200/api/bot1/61ab5cc48ec3dbad1ff95152'
        data = {"dont exist": "some change", "permissionList": "[play_sound_permission]"}

        response = requests.put(url, json=data)
        print(response.status_code)
        date_response = response.json()
        assert (response.status_code == 404), "was able to get into the put method although supplying false attribute "

    @staticmethod
    def test_bot1_put_no_data():
        url = 'http://localhost:4200/api/bot1/61a8134acf9ab3953a5df930'
        response = requests.put(url)
        print(response.status_code)
        assert (response.status_code == 404), "was able to get into the put method although supplying no data"
