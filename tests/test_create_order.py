import allure
from allure_commons.types import LabelType
from jsonschema import validate

from tests.helpers import post_request, get_schema, URL


@allure.epic("Petstore")
@allure.feature("Создание заказа")
class TestCreateOrder:
    @allure.story("Создание заказа")
    @allure.label(LabelType.TAG, "smoke")
    @allure.severity("BLOCKER")
    def test_create_order(self):
        with allure.step("Создать заказ"):
            url = URL + "/store/order"
            body = {
                "id": 15,
                "petId": 11,
                "quantity": 10,
                "shipDate": "2025-01-08T13:03:27.063+0000",
                "status": "placed",
                "complete": True
            }
            response = post_request(url=url, body=body)

        with allure.step("Проверить схему ответа"):
            validate(response.json(), get_schema("create_order.json"))
        with allure.step("Проверить код ответа"):
            assert response.status_code == 200
        with allure.step("Проверить тело ответа"):
            assert response.json() == body
