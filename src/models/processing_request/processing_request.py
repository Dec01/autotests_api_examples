import requests
import configparser
import logging


class Requests(object):
    LOGGER = logging.getLogger(__name__)
    parser = configparser.ConfigParser()
    parser.read('pytest.ini')

    @staticmethod
    def get_request(url, method_url, params, headers):
        response = requests.get(url + method_url, params=params, headers=headers, verify=True)
        Requests.LOGGER.info('Request url {}{} with params {}, headers {}'.format(url, method_url, params, headers))
        if response.status_code == 404:
            Requests.LOGGER.info('Response {}'.format(response))
        else:
            Requests.LOGGER.info('Response {}{}'.format(response, response.json()))
        return response

    @staticmethod
    def post_request(url, method_url, data, json, headers):
        response = requests.post(url + method_url, data=data,  json=json, headers=headers, verify=True)
        Requests.LOGGER.info('Request url {}{} with data {} , headers {}, body {}'.format(url, method_url, data,
                                                                                              headers, json))
        if (response.status_code == 204) or (response.status_code == 404):
            Requests.LOGGER.info('Response {}'.format(response))
        else:
            Requests.LOGGER.info('Response {}{}'.format(response, response.json()))
        return response

    @staticmethod
    def patch_request(url, method_url, data, json, headers):
        response = requests.patch(url + method_url, data=data,  json=json, headers=headers, verify=False)
        Requests.LOGGER.info(
                'Request url {}{} with data {} , headers {}, body {}'.format(url, method_url, data, headers, json))
        if (response.status_code == 204) or (response.status_code == 404):
                Requests.LOGGER.info('Response {}'.format(response))
        else:
            Requests.LOGGER.info('Response {}{}'.format(response, response.json()))
        return response

    @staticmethod
    def put_request(url, method_url, data, json, headers):
        response = requests.put(url + method_url, data=data, json=json, headers=headers, verify=False)
        Requests.LOGGER.info('Request url {}{} with data {} , headers {}'.format(url, method_url, data, headers))
        if (response.status_code == 204) or (response.status_code == 404):
            Requests.LOGGER.info('Response {}'.format(response))
        else:
            Requests.LOGGER.info('Response {}{}'.format(response, response.json()))
        return response

    @staticmethod
    def delete_request(url, method_url, headers):
        response = requests.delete(url + method_url, headers=headers, verify=False)
        Requests.LOGGER.info('Request url {}{} with headers {}'.format(url, method_url, headers))
        if (response.status_code == 204) or (response.status_code == 404):
            Requests.LOGGER.info('Response {}'.format(response))
        else:
            Requests.LOGGER.info('Response {}{}'.format(response, response.json()))
        return response


class AsyncRequests(object):
    logging.basicConfig(
        filename='logs/pytest.log',
        level=logging.INFO,
        format='%(asctime)s [%(levelname)8s] %(message)s (%(filename)s:%(lineno)s)',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    LOGGER = logging.getLogger(__name__)
    parser = configparser.ConfigParser()
    parser.read('pytest.ini')

    @staticmethod
    async def get_request(url, method_url, params, headers):
        async with httpx.AsyncClient(follow_redirects=True, verify=False) as client:
            with allure.step("Запрос отправлен, посмотрим код ответа"):
                response = await client.get(url + method_url, params=params, headers=headers)
                AsyncRequests.LOGGER.info(f"Response body: {response.text}")
        if response.status_code != 200 and response.status_code != 403 and response.status_code != 405:
            AsyncRequests.LOGGER.info('Request: {}{} params {}, headers {}'.format(url, method_url, params, headers))
            print('\nResponse status_code: {}\nbody: {}'.format(response.status_code, response.json()))
        return response

    @staticmethod
    async def get_request_nolog(url, method_url, params, headers):
        async with httpx.AsyncClient(follow_redirects=True, verify=False) as client:
            with allure.step("Запрос отправлен, посмотрим код ответа"):
                response = await client.get(url + method_url, params=params, headers=headers)
        if response.status_code != 200 and response.status_code != 403 and response.status_code != 405:
            print('\nResponse status_code: {}\nbody: {}'.format(response.status_code, response.json()))
        return response

    @staticmethod
    async def post_request(url, method_url, data, json, headers):
        async with httpx.AsyncClient(follow_redirects=True, verify=False) as client:
            with allure.step("Запрос отправлен, посмотрим код ответа"):
                response = await client.post(url + method_url, data=data, json=json, headers=headers)
                AsyncRequests.LOGGER.info(f"Response body: {response.text}")
        if response.status_code != 200 and response.status_code != 403 and response.status_code != 405:
            AsyncRequests.LOGGER.info('Request: {}{} data {}, headers {}, body {}'.format(url, method_url, data,
                                                                                              headers, json))
            print('\nResponse StatusCode: {}\n Response body: {}'.format(response.status_code, response.json()))
        return response

    @staticmethod
    async def patch_request(url, method_url, data, json, headers):
        async with httpx.AsyncClient(follow_redirects=True, verify=False) as client:
            with allure.step("Запрос отправлен, посмотрим код ответа"):
                response = await client.patch(url + method_url, data=data, json=json, headers=headers)
                AsyncRequests.LOGGER.info(f"Response body: {response.text}")
        if response.status_code != 200 and response.status_code != 403 and response.status_code != 405:
            AsyncRequests.LOGGER.info(
                'Request: {}{} data: {}, headers: {}, body: {}'.format(url, method_url, data, headers, json))
            print('\nResponse StatusCode: {} \n Response body: {}'.format(response.status_code, response.json()))
        return response

    @staticmethod
    async def put_request(url, method_url, data, json, headers):
        async with httpx.AsyncClient(follow_redirects=True, verify=False) as client:
            with allure.step("Запрос отправлен, посмотрим код ответа"):
                response = await client.put(url + method_url, data=data, json=json, headers=headers)
                AsyncRequests.LOGGER.info(f"Response body: {response.text}")
        if response.status_code != 200 and response.status_code != 403 and response.status_code != 405:
            AsyncRequests.LOGGER.info('Request url {}{} with data {} , headers {}'.format(url, method_url, data, headers))
            print('\nResponse StatusCode: {} \n Response body: {}'.format(response.status_code, response.json()))
        return response

    @staticmethod
    async def delete_request(url, method_url, headers):
        async with httpx.AsyncClient(follow_redirects=True, verify=False) as client:
            with allure.step("Запрос отправлен, посмотрим код ответа"):
                response = await client.delete(url + method_url, headers=headers)
                AsyncRequests.LOGGER.info(f"Response body: {response.text}")
        if response.status_code != 200 and response.status_code != 403 and response.status_code != 405:
            AsyncRequests.LOGGER.info('Request url {}{} with headers {}'.format(url, method_url, headers))
            print('\nResponse StatusCode: {} \n Response body: {}'.format(response.status_code, response.json()))
        return response

    @staticmethod
    def definition_method_request(method_type, url, method_url, params, data, json, headers):
        if method_type == 'GET':
            return AsyncRequests.get_request(url, method_url, params, headers)
        elif method_type == 'POST':
            return AsyncRequests.post_request(url, method_url, data, json, headers)
        elif method_type == 'PATCH':
            return AsyncRequests.patch_request(url, method_url, data, json, headers)
        elif method_type == 'PUT':
            return AsyncRequests.put_request(url, method_url, data, json, headers)
        elif method_type == 'DELETE':
            return AsyncRequests.delete_request(url, method_url, headers)
        else:
            return False