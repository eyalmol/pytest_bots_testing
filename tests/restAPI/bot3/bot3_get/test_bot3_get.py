import requests
import json
from pytest import mark


@mark.bot3
@mark.get
@mark.get_bot3
class GetBot3Tests:
    @staticmethod
    def test_bot3_simple_get_method():
        url = 'http://localhost:4200/api/bot3'

        response = requests.get(url)
        print(response.status_code)
        date_response = response.json()
        assert (response.status_code == 200), "something went wrong in the simple get function"

    @staticmethod
    def test_bot3_get_make_api_call():
        url = 'http://localhost:4200/api/bot3/61abbcf809444d8ebaf8b96a/eyalmolakandov'

        response = requests.get(url)
        print(response.status_code)
        assert (
                response.status_code == 200 and response.text == "make_api_call"), "something went wrong in the bot3 get make api call"

    @staticmethod
    def test_bot3_get_make_api_call_wrong_auth():
        url = 'http://localhost:4200/api/bot3/61abbcf809444d8ebaf8b96a/eyalndov'
        response = requests.get(url)
        print(response.status_code)
        assert (
                response.status_code == 200 and response.text == "Unauthorized"), "was able to make api call although giving wrong username+password "

    @staticmethod
    def test_bot3_get_make_api_call_id_does_not_exist():
        url = 'http://localhost:4200/api/bot3/15454/eyalndov'
        response = requests.get(url)
        print(response.status_code)
        assert (response.status_code == 422), "manged to run bot3 get make api call with id that does not exist in DB"

    @staticmethod
    def test_bot3_get_make_api_call_correct_auth():
        url = 'http://localhost:4200/api/bot3/61abbcf809444d8ebaf8b96a/30377'
        response = requests.get(url)
        print(response.status_code)
        assert (
                response.status_code == 200 and response.text == "make_api_call"), "bot3 get was not able to generate api call although supplying right auth"
