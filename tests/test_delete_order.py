import allure
from allure_commons.types import LabelType

from data.models import create_order_request_data, test_order
from tests.helpers import check_schema, check_code, check_body, create_order, delete_order


@allure.epic("Petstore")
@allure.feature("Удаление заказа")
class TestDeleteOrder:
    @allure.story("Удаление существующего заказа")
    @allure.label(LabelType.TAG, "smoke")
    @allure.severity("BLOCKER")
    def test_delete_existing_order(self, order_endpoint):
        body = create_order_request_data(test_order)
        create_order(url=order_endpoint, body=body)
        expected_json = {
            "code": 200,
            "type": "unknown",
            "message": f"{test_order.id}"
        }
        response = delete_order(url=order_endpoint + f"/{test_order.id}")
        check_schema(response, "delete_order.json")
        check_code(response, 200)
        check_body(response, expected_json)


    @allure.story("Невозможно удаление несуществующего заказа")
    @allure.label(LabelType.TAG, "smoke")
    @allure.severity("BLOCKER")
    def test_cant_delete_non_existing_order(self, order_endpoint):
        body = create_order_request_data(test_order)
        create_order(url=order_endpoint, body=body)
        delete_order(url=order_endpoint + f"/{test_order.id}")
        expected_json = {
            "code": 404,
            "type": "unknown",
            "message": "Order Not Found"
        }
        response = delete_order(url=order_endpoint + f"/{test_order.id}")
        check_schema(response, "delete_order.json")
        check_code(response, 404)
        check_body(response, expected_json)
