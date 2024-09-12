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
