import json
import logging
import os

import allure
import requests
from allure_commons.types import AttachmentType
from requests import Response

CURRENT_FILE = os.path.abspath(__file__)
DIRECTORY = os.path.dirname(CURRENT_FILE)
SCHEMA_DIR = os.path.join(os.path.dirname(DIRECTORY), "schemas")
URL = "https://petstore.swagger.io/v2"


def response_logging(response: Response):
    logging.info("Request: " + response.request.url)
    if response.request.body:
        logging.info("Request body: " + response.request.body.decode('utf-8'))
    logging.info("Request headers: " + str(response.request.headers))
    logging.info("Response code " + str(response.status_code))
    logging.info("Response: " + response.text)


def response_attaching(response: Response):
    allure.attach(
        body=response.request.url,
        name="Request url",
        attachment_type=AttachmentType.TEXT,
    )

    if response.request.body:
        allure.attach(
            body=json.dumps(json.loads(response.request.body.decode('utf-8')), indent=4, ensure_ascii=True),
            name="Request body",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )
    allure.attach(
        body=json.dumps(response.json(), indent=4, ensure_ascii=True),
        name="Response",
        attachment_type=AttachmentType.JSON,
        extension="json",
    )


def post_request(url, body, **kwargs):
    response = requests.post(url=url, json=body, **kwargs)
    response_logging(response)
    response_attaching(response)
    return response


def get_request(url, **kwargs):
    response = requests.get(url, **kwargs)
    response_logging(response)
    response_attaching(response)
    return response


def delete_request(url, **kwargs):
    response = requests.delete(url, **kwargs)
    response_logging(response)
    response_attaching(response)
    return response


def get_schema(file_name):
    with open(os.path.join(SCHEMA_DIR, file_name)) as file:
        return json.loads(file.read())
