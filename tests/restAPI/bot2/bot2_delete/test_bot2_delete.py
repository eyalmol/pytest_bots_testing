import requests
import json
from pytest import mark


@mark.delete_bot2
class DeleteBot1Tests:
    # # for testing this method need so specify id that exists in DB
    # @staticmethod
    # def test_bot2_simple_delete_method():
    #     url = 'http://localhost:4200/api/bot2/61ab6f1ba915e800ab09261d'
    #
    #     response = requests.delete(url)
    #     print(response.status_code)
    #     date_response = response.json()
    #     assert (response.status_code == 200), "simple bot2 delete method went wrong"

    @staticmethod
    def test_bot2_delete_method_no_id_specified():
        url = "http://localhost:4200/api/bot2"
        response = requests.delete(url)
        print(response.status_code)
        assert (response.status_code == 404), "managed to preform delete bot2 method without specifying an id"

    @staticmethod
    def test_bot2_delete_method_id_not_exist():
        url = "http://localhost:4200/api/bot2/655"
        response = requests.delete(url)
        print(response.status_code)
        assert (response.status_code == 422), "managed to preform delete bot2 method with id that do not exist in DB"

    @staticmethod
    def test_bot2_delete_method_no_bot_spec():
        url = "http://localhost:4200/api"
        response = requests.delete(url)
        print(response.status_code)
        assert (response.status_code == 404), "managed to preform delete without specifying bot"
