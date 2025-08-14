import pytest
import allure
import requests


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
    status_code = api_client.create_booking()
    assert status_code == 200, f"Expected status 200 but got {status_code}"











