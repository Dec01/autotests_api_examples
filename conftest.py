import pytest

from src.models.processing_request.processing_request import Requests


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
