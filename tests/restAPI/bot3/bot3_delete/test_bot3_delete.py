import requests
import json
from pytest import mark


@mark.bot3
@mark.delete
@mark.delete_bot3
class DeleteBot3Tests:
    # for testing this method need to specify id that exists in DB
    # @staticmethod
    # def test_bot3_simple_delete_method():
    #     url = 'http://localhost:4200/api/bot3/61abbcd209444d8ebaf8b968'
    #
    #     response = requests.delete(url)
    #     print(response.status_code)
    #     assert (response.status_code == 200), "simple bot3 delete method went wrong"

    @staticmethod
    def test_bot3_delete_method_no_id_specified():
        url = "http://localhost:4200/api/bot3"
        response = requests.delete(url)
        print(response.status_code)
        assert (response.status_code == 404), "managed to preform delete bot3 method without specifying an id"

    @staticmethod
    def test_bot3_delete_method_id_not_exist():
        url = "http://localhost:4200/api/bot3/546642"
        response = requests.delete(url)
        print(response.status_code)
        assert (response.status_code == 422), "managed to preform delete bot3 method with id that do not exist in DB"

    @staticmethod
    def test_bot3_delete_method_no_bot_spec():
        url = "http://localhost:4200/api"
        response = requests.delete(url)
        print(response.status_code)
        assert (response.status_code == 404), "managed to preform delete without specifying bot"
