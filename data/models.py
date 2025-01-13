from dataclasses import dataclass


@dataclass
class Order:
    id: int
    pet_id: int
    quantity: int
    ship_date: str
    status: str
    complete: bool

test_order = Order(id=7, pet_id=11, quantity= 10, ship_date= "2025-01-08T13:03:27.063+0000", status="placed", complete=True)


def create_order_request_data(order) -> dict:
    body = {
        "id": order.id,
        "petId": order.pet_id,
        "quantity": order.quantity,
        "shipDate": order.ship_date,
        "status": order.status,
        "complete": order.complete
    }
    return body
