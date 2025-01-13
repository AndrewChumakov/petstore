import allure
from allure_commons.types import LabelType

from data.models import create_order_request_data, test_order
from tests.helpers import check_schema, check_code, check_body, create_order


@allure.epic("Petstore")
@allure.feature("Создание заказа")
class TestCreateOrder:
    @allure.story("Создание заказа")
    @allure.label(LabelType.TAG, "smoke")
    @allure.severity("BLOCKER")
    def test_create_order(self, order_endpoint):
        body = create_order_request_data(test_order)
        response = create_order(url=order_endpoint, body=body)
        check_schema(response, "create_order.json")
        check_code(response, 200)
        check_body(response, body)
