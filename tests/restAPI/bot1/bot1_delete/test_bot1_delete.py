import requests
import json
from pytest import mark


@mark.delete_bot1
class DeleteBot1Tests:
    # for testing this method need to specify id that exists in DB
    @staticmethod
    def test_bot1_simple_delete_method():
        url = 'http://localhost:4200/api/bot1/61aa30817632f64f53e44e29'

        response = requests.delete(url)
        print(response.status_code)
        date_response = response.json()
        assert (response.status_code == 200), "simple delete method went wrong"

    @staticmethod
    def test_bot1_delete_method_no_id_specified():
        url = "http://localhost:4200/api/bot1"
        response = requests.delete(url)
        print(response.status_code)
        assert (response.status_code == 404), "managed to preform delete bot 1 method without specifying an id"

    @staticmethod
    def test_bot1_delete_method_id_not_exist():
        url = "http://localhost:4200/api/bot1/546642"
        response = requests.delete(url)
        print(response.status_code)
        assert (response.status_code == 422), "managed to preform delete bot 1 method with id that do not exist in DB"

    @staticmethod
    def test_bot1_delete_method_no_bot_spec():
        url = "http://localhost:4200/api"
        response = requests.delete(url)
        print(response.status_code)
        assert (response.status_code == 404), "managed to preform delete without specifying bot"
