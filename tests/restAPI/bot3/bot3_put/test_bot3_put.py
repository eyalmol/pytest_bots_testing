import requests
import json
from pytest import mark


@mark.bot3
@mark.put
@mark.put_bot3
class PutBot3Tests:
    @staticmethod
    def test_bot3_simple_put_method():
        url = 'http://localhost:4200/api/bot3/61a9548b6cff190c4b06047f'
        data = {"intent": "[play_sound]", "permissionList": "[play_sound_permission]"}

        response = requests.put(url, json=data)
        print(response.status_code)
        date_response = response.json()
        assert (response.status_code == 200), "simple put bot3 method is not OK"

    @staticmethod
    def test_bot3_put_method_giving_false_id():
        url = 'http://localhost:4200/api/bot3/4852'
        data = {"intent": "[play_sound]", "permissionList": "[play_sound_permission]"}

        response = requests.put(url, json=data)
        print(response.status_code)
        date_response = response.json()
        assert (response.status_code == 422), "was able to generate bot3 put with id that does not exist in DB"

    @staticmethod
    def test_bot3_put_method_giving_no_data():
        url = 'http://localhost:4200/api/bot3/61a9548b6cff190c4b06047f'

        response = requests.put(url)
        print(response.status_code)
        date_response = response.json()
        assert (response.status_code == 422), "was able to generate bot3 put with no data supplied"

    @staticmethod
    def test_bot3_put_method_id_dont_supplied():
        url = 'http://localhost:4200/api/bot3'
        data = {"intent": "[play_sound]", "permissionList": "[play_sound_permission]"}
        response = requests.put(url)
        print(response.status_code)

        assert (response.status_code == 404), "was able to generate bot3 put with no id supplied"

    @staticmethod
    def test_bot3_put_attribute_dont_exist():
        url = 'http://localhost:4200/api/bot3/61a9548b6cff190c4b06047f'
        data = {"dont exist": "some change", "permissionList": "[play_sound_permission]"}

        response = requests.put(url, json=data)
        print(response.status_code)
        date_response = response.json()
        assert (response.status_code == 404), "was able to get into the put method although supplying false attribute "
