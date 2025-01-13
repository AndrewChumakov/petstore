import os

import pytest
from dotenv import load_dotenv


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()

def base_url():
    return os.getenv("URL")

@pytest.fixture(scope="function")
def order_endpoint():
    url = base_url() + "/store/order"
    yield url

