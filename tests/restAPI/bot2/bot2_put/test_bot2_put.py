import requests
import json
from pytest import mark


@mark.put_bot2
class PutBot2Tests:
    @staticmethod
    def test_bot2_simple_put_method():
        url = 'http://localhost:4200/api/bot2/61ab6d608ec3dbad1ff95171'
        data = {"welcomeMsg": "hello friend"}

        response = requests.put(url, json=data)
        print(response.status_code)
        date_response = response.json()
        assert (response.status_code == 200), "simple put method is not OK"

    @staticmethod
    def test_bot2_put_id_not_exist():
        url = 'http://localhost:4200/api/bot2/f95967'
        data = {"intent": "[jhejhjksahkjh]"}
        response = requests.put(url, json=data)
        print(response.status_code)
        assert (response.status_code == 422), "manged to execute put method with no exist id"

    @staticmethod
    def test_bot2_put_no_id_provided():
        url = 'http://localhost:4200/api/bot2'
        data = {"intent": "[some intent]"}
        response = requests.put(url, json=data)
        print(response.status_code)
        assert (response.status_code == 404), "manged to execute put method without providing id"

    @staticmethod
    def test_bot2_put_attribute_dont_exist():
        url = 'http://localhost:4200/api/bot2/61ab6d608ec3dbad1ff95171'
        data = {"dont exist": "some change"}

        response = requests.put(url, json=data)
        print(response.status_code)
        date_response = response.json()
        assert (response.status_code == 404), "was able to get into the put method although supplying false attribute "

    @staticmethod
    def test_bot2_put_no_data():
        url = 'http://localhost:4200/api/bot2/61ab6d608ec3dbad1ff95171'
        response = requests.put(url)
        print(response.status_code)
        assert (response.status_code == 404), "was able to get into the put method although supplying no data"

    @staticmethod
    def test_bot2_put_method_generate_intent_and_welcome_msg():
        url = 'http://localhost:4200/api/bot2/61ab6d608ec3dbad1ff95178'
        data = {"intent": "bot2 put gen welcome msg", "welcomeMsg": "this is my new welcome msg"}

        response = requests.put(url, json=data)
        print(response.status_code)
        date_response = response.json()
        assert (response.status_code == 200 and response.text.__contains__("this is my new welcome msg")), "wasn't able to generate a welcome message replacing the default one"

    @staticmethod
    def test_bot2_put_method_generate_intent_not_changing_welcome_msg():
        url = 'http://localhost:4200/api/bot2/61ab6d9d8ec3dbad1ff9517a'
        data = {"intent": "welcome_msg_intent"}

        response = requests.put(url, json=data)
        print(response.status_code)
        date_response = response.json()
        assert (response.status_code == 200 and response.text.__contains__("welcome")), "wasn't able to generate a welcome message intent"



