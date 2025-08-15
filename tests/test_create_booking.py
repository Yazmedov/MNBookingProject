import pytest
import allure
import requests
from requests import HTTPError

from conftest import api_client


@allure.feature("Test create")
@allure.story("Test create_booking")
def test_create_booking(api_client):
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    api_client.create_booking(booking_data=payload)

@allure.feature("Test create")
@allure.story("Test create_booking_invalid_json")
def test_create_booking_invalid(api_client):
    payload = {
        "firstname": 123,
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    with pytest.raises(HTTPError):
         api_client.create_booking(booking_data=payload)














