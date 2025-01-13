import allure
from allure_commons.types import LabelType

from data.models import create_order_request_data, test_order
from tests.helpers import check_schema, check_code, \
    check_body, create_order, get_order, delete_order


@allure.epic("Petstore")
@allure.feature("Получение заказа")
class TestGetOrder:
    @allure.story("Получение существующего заказа")
    @allure.label(LabelType.TAG, "smoke")
    @allure.severity("BLOCKER")
    def test_get_existing_order(self, order_endpoint):
        body = create_order_request_data(test_order)
        create_order(url=order_endpoint, body=body)
        response = get_order(url=order_endpoint + f"/{test_order.id}")
        check_schema(response, "success_get_order.json")
        check_code(response, 200)
        check_body(response, body)

    @allure.story("Невозможно получение несуществующего заказа")
    @allure.label(LabelType.TAG, "smoke")
    @allure.severity("BLOCKER")
    def test_cant_get_non_existing_order(self, order_endpoint):
        body = create_order_request_data(test_order)
        create_order(url=order_endpoint, body=body)
        delete_order(url=order_endpoint + f"/{test_order.id}")
        expected_json = {
            "code": 1,
            "type": "error",
            "message": "Order not found"
        }
        response = get_order(url=order_endpoint + f"/{test_order.id}")
        check_schema(response, "failure_get_order.json")
        check_code(response, 404)
        check_body(response, expected_json)
