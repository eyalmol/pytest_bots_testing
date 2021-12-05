import requests
import json
from pytest import mark


@mark.bot1
@mark.get
@mark.get_bot1
class GetBot1Tests:
    @staticmethod
    def test_bot1_simple_get_method():
        url = 'http://localhost:4200/api/bot1'

        response = requests.get(url)
        print(response.status_code)
        date_response = response.json()
        assert (response.status_code == 200), "something went wrong in the simple get function"

    @staticmethod
    def test_bot1_simple_get_method_not_bot_specified():
        url = 'http://localhost:4200/api'

        response = requests.get(url)
        print(response.status_code)

        assert (response.status_code == 404), "managed to activate get without bot specification"

    @staticmethod
    def test_bot1_get_play_sound_method():
        url = 'http://localhost:4200/api/bot1/61a80faa66b5be9579bd22d1/play_sound'
        response = requests.get(url)
        print(response.status_code)

        assert (response.status_code == 200), "something went wrong in the play sound get function"

    @staticmethod
    def test_bot1_get_play_sound_method_no_id():
        url = 'http://localhost:4200/api/bot1/play_sound'
        response = requests.get(url)
        print(response.status_code)

        assert (response.status_code == 404), "managed to activate the play sound without id"

    @staticmethod
    def test_bot1_get_play_sound_method_no_bot_specification():
        url = 'http://localhost:4200/api/play_sound'
        response = requests.get(url)
        print(response.status_code)

        assert (response.status_code == 404), "managed to activate the play sound without bot specification"

    @staticmethod
    def test_bot1_play_sound_no_permission():
        url = 'http://localhost:4200/api/bot1/61ab7545bec9a5aa9e93cf42/play_sound'
        response = requests.get(url)
        print(response.status_code)
        text = response.text
        assert (response.text == 'False'), "managed to activate the play sound without permission"

    @staticmethod
    def test_bot1_play_sound_no_intent():
        url = 'http://localhost:4200/api/bot1/61ab76aabec9a5aa9e93cf4a/play_sound'
        response = requests.get(url)
        print(response.status_code)
        text = response.text
        assert (response.text == 'False'), "managed to activate the play sound without an intent"
