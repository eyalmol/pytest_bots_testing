import requests
import json
from pytest import mark


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
    def test_bot2_get_method_intent_welcome_message_change_def_msg():
        url = 'http://localhost:4200/api/bot2/61ab6d608ec3dbad1ff95171/welcomeMsg_intent/welcome_my_friend'

        response = requests.get(url)
        print(response.status_code)
        assert (response.status_code == 200), "something went wrong in the get function with id, intent and welcomeMsg provided"

    @staticmethod
    def test_bot2_get_method_give_intent_no_msg_given():
        # needs to generate the default welcome msg "welcome"
        url = 'http://localhost:4200/api/bot2/61ab6d608ec3dbad1ff95173/welcomeMsg_intent'

        response = requests.get(url)
        print(response.status_code)
        assert (response.status_code == 200), "something went wrong trying to send only the id and the intent without new welcome msg"
