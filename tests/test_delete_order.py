import allure
from allure_commons.types import LabelType
from jsonschema import validate

from tests.helpers import post_request, get_schema, delete_request, URL


@allure.epic("Petstore")
@allure.feature("Удаление заказа")
class TestDeleteOrder:
    @allure.story("Удаление существующего заказа")
    @allure.label(LabelType.TAG, "smoke")
    @allure.severity("BLOCKER")
    def test_delete_existing_order(self):
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

        expected_json = {
            "code": 200,
            "type": "unknown",
            "message": f"{order_id}"
        }

        with allure.step("Удалить созданный заказ"):
            response = delete_request(url=URL + f"/store/order/{order_id}")

        with allure.step("Проверить схему ответа"):
            validate(response.json(), get_schema("delete_order.json"))

        with allure.step("Проверить код ответа"):
            assert response.status_code == 200

        with allure.step("Проверить тело ответа"):
            assert response.json() == expected_json

    @allure.story("Невозможно удаление несуществующего заказа")
    @allure.label(LabelType.TAG, "smoke")
    @allure.severity("BLOCKER")
    def test_cant_delete_non_existing_order(self):
        order_id = 11
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

        with allure.step("Удалить созданный заказ"):
            delete_request(url=URL + f"/store/order/{order_id}")

        expected_json = {
            "code": 404,
            "type": "unknown",
            "message": "Order Not Found"
        }
        with allure.step("Удалить удаленный заказ"):
            response = delete_request(url=URL + f"/store/order/{order_id}")

        with allure.step("Проверить схему ответа"):
            validate(response.json(), get_schema("delete_order.json"))
        with allure.step("Проверить код ответа"):
            assert response.status_code == 404
        with allure.step("Проверить тело ответа"):
            assert response.json() == expected_json
