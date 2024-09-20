import allure
import httpx
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


class RequestLanguage:
    header_en_one = {'Accept-Language': 'en'}
    header_en = {'Accept-Language': 'en-US'}
    header_ru_one = {'Accept-Language': 'ru'}
    header_ru = {'Accept-Language': 'ru-Ru'}
    header_default = {}
    header_error = {'Accept-Language': 'zu-Ze'}
    header_preference_ru = {'Accept-Language': 'ru-RU,ru;q=0.9,en-GB;q=0.8,en;q=0.7,be-BY;q=0.6,be;q=0.5,en-US;q=0.4'}
    header_preference_en = {'Accept-Language': 'ru-RU,ru;q=0.7,en-GB;q=0.8,en;q=0.9,be-BY;q=0.6,be;q=0.5,en-US;q=0.4'}

class RequestToken:

    token_role = {
        'ROLE_SUPER_ADMIN': '123123123-213123123-213123123',
        'ROLE_ADMIN': '2332323-23232323-23232323-232323',
        'ROLE_MANAGER': '232323232-453-43-4345-535-34343434',
        'ROLE_EDITOR': '33432423-4324234343-43434343434-4343434',
        'ROLE_MODERATOR': '43434342321352-213523523523-235235235'
    }

    @staticmethod
    def response_token_role(role):
        for i in RequestToken.token_role:
            if i == role:
                return_token_role = {'Authorization': f'Bearer {RequestToken.token_role.get(role)}'}
                return return_token_role
