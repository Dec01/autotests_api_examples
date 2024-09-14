import time

import pytest

from src.models.processing_request.processing_request import Requests, AsyncRequests


def pytest_addoption(parser):
    parser.addoption("--domain", action="store", default="https://api-fake.ru")


@pytest.fixture()
def domain(request):
    return request.config.getoption("--domain")

@pytest.fixture(scope="session")
def base_url(domain):
    return domain


@pytest.fixture(autouse=True)
def req():
    return Requests


@pytest.fixture(autouse=True)
def slow_down_tests():
    yield
    time.sleep(0)

@pytest.fixture(autouse=True)
def async_req():
    return AsyncRequests

def pytest_make_parametrize_id(config, val):
    return repr(val)