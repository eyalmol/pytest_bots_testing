import requests
import json
from pytest import mark


@mark.bot2
@mark.get
@mark.get_bot2
class GetBot2Tests:
    @staticmethod
    def test_bot2_simple_get_method():
        url = 'http://localhost:4200/api/bot2'

        response = requests.get(url)
        print(response.status_code)
        date_response = response.json()
        assert (response.status_code == 200), "something went wrong in the simple get function"

    @staticmethod
    def test_bot2_get_method_commit_default_msg():
        url = 'http://localhost:4200/api/bot2/61ab6d9d8ec3dbad1ff95181/default_welcome_message'
        response = requests.get(url)
        print(response.status_code)
        assert (
                response.status_code == 200 and response.text == "welcome"), "something went wrong in the get method activate the bot2 function no new message"

    @staticmethod
    def test_bot2_get_method_sending_false_intent():
        url = 'http://localhost:4200/api/bot2/61ab6d9d8ec3dbad1ff95181/message'
        response = requests.get(url)
        print(response.status_code)
        assert (
                response.status_code == 200 and response.text == "False intent"), "didn't return an alarm while trying to give false intent"

    @staticmethod
    def test_bot2_get_commit_fun_and_supply_new_msg():
        url = 'http://localhost:4200/api/bot2/61ab6d9d8ec3dbad1ff95181/default_welcome_message/hello_my_friend'
        response = requests.get(url)
        print(response.status_code)
        assert (
                response.status_code == 200 and response.text == "hello_my_friend"), "was not able to generate new msg in the get bot2 functionality"

    @staticmethod
    def test_bot2_get_default_msg_supply_not_exist_id_with_new_msg():
        url = 'http://localhost:4200/api/bot2/5324/default_welcome_message/hello_my_friend'
        response = requests.get(url)
        print(response.status_code)
        assert (response.status_code == 422), "was able to commit bot2 get new default msg with wrong id"

    @staticmethod
    def test_bot2_get_default_msg_supply_not_exist_id_withot_new_msg():
        url = 'http://localhost:4200/api/bot2/5324/default_welcome_message'
        response = requests.get(url)
        print(response.status_code)
        assert (
                response.status_code == 422), "was able to commit bot2 get default msg with wrong id and without a new msg"
