from pydantic import ValidationError

import pytest
import allure
import requests
from requests import HTTPError

from conftest import api_client
from core.models.booking import BookingResponse


@allure.feature("Test create")
@allure.story("Positive: creating booking with custom data")
def test_create_booking(api_client):
    booking_data = {
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
    response = api_client.create_booking(booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f"Response validation failed: {e}")
    assert response ["booking"]["firstname"] == booking_data ["firstname"]
    assert response["booking"]["lastname"] == booking_data["lastname"]
    assert response["booking"]["totalprice"] == booking_data["totalprice"]
    assert response["booking"]["depositpaid"] == booking_data["depositpaid"]
    assert response["booking"]["bookingdates"]["checkin"] == booking_data["bookingdates"]["checkin"]
    assert response["booking"]["bookingdates"]["checkout"] == booking_data["bookingdates"]["checkout"]
    assert response["booking"]["additionalneeds"] == booking_data["additionalneeds"]

@allure.feature("Test create")
@allure.story("Negative: create booking invalid name")
def test_create_booking_invalid_name(api_client):
    booking_data = {
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
         api_client.create_booking(booking_data)

@allure.feature("Test create")
@allure.story("Positive: creating booking with random data")
def test_create_booking(api_client,generate_random_booking_data):
    booking_data = generate_random_booking_data
    response = api_client.create_booking(booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
         raise ValidationError(f"Response validation failed: {e}")

@allure.feature("Test create")
@allure.story("Negative: create booking invalid lastname")
def test_create_booking_invalid_lastname(api_client):
    booking_data = {
        "firstname": "Jim",
        "lastname": 2423154,
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    with pytest.raises(HTTPError):
         api_client.create_booking(booking_data)














