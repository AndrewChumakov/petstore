import allure
from allure_commons.types import LabelType
from jsonschema import validate

from tests.helpers import post_request, get_schema, delete_request, get_request, URL


@allure.epic("Petstore")
@allure.feature("Получение заказа")
class TestGetOrder:
    @allure.story("Получение существующего заказа")
    @allure.label(LabelType.TAG, "smoke")
    @allure.severity("BLOCKER")
    def test_get_existing_order(self):
        order_id = 7
        with allure.step("Создать заказ"):
            body = {
                "id": order_id,
                "petId": 11,
                "quantity": 10,
                "shipDate": "2025-01-08T13:03:27.063+0000",
                "status": "placed",
                "complete": True
            }
            post_request(url=URL + "/store/order", body=body)

        with allure.step("Получить созданный заказ"):
            response = get_request(url=URL + f"/store/order/{order_id}")

        with allure.step("Проверить схему ответа"):
            validate(response.json(), get_schema("success_get_order.json"))

        with allure.step("Проверить код ответа"):
            assert response.status_code == 200

        with allure.step("Проверить тело ответа"):
            assert response.json() == body

    @allure.story("Невозможно получение несуществующего заказа")
    @allure.label(LabelType.TAG, "smoke")
    @allure.severity("BLOCKER")
    def test_cant_get_non_existing_order(self):
        order_id = 8
        with allure.step("Создать заказ"):
            body = {
                "id": order_id,
                "petId": 11,
                "quantity": 10,
                "shipDate": "2025-01-08T13:03:27.063+0000",
                "status": "placed",
                "complete": True
            }
            post_request(url=URL + "/store/order", body=body)

        with allure.step("Удалить заказ"):
            delete_request(url=URL + f"/store/order/{order_id}")

        expected_json = {
            "code": 1,
            "type": "error",
            "message": "Order not found"
        }
        with allure.step("Получить удаленный заказ"):
            response = get_request(url=URL + f"/store/order/{order_id}")

        with allure.step("Проверить схему ответа"):
            validate(response.json(), get_schema("failure_get_order.json"))

        with allure.step("Проверить код ответа"):
            assert response.status_code == 404

        with allure.step("Проверить тело ответа"):
            assert response.json() == expected_json
