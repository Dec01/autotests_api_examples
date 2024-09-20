import pytest
import json

from src.models.paths.user_paths import PathsServices
from src.models.payloads.model_user_case_post import PayloadPostUserCase, ValidatePostUserCase
from src.models.payloads.model_user_case_get import ValidateGetUserCase

service = PathsServices.services_paths.get('health_check')
@pytest.mark.dev
@pytest.mark.asyncio
class TestBFFUserStudentCacheUserCasesValues:

    payload_create_cache = None
    data_create_cache = None
    data_check_create_cache = None

    async def test_create_data(self, domain, async_req):
        payload = PayloadPostUserCase.definition_payload('default')
        try:
            response = await async_req.post_request(domain, service, {}, payload,
                                                    {})

            assert response is not None
            assert response.status_code == 200

            data = response.json()
            self.__class__.data_create_cache = data
            self.__class__.payload_create_cache = payload

        except json.decoder.JSONDecodeError as e:
            assert False, print("Error decoding JSON response:", e)
        except Exception as e:
            assert False, print("Request Exception:", e)

    async def test_check_data_after_create(self, domain, async_req):
        try:
            response = await async_req.get_request(domain, service, {},
                                                   {})
            assert response.status_code == 200

            data = response.json()
            self.__class__.data_check_create_cache = data

        except json.decoder.JSONDecodeError as e:
            assert False, print("Error decoding JSON response:", e)
        except Exception as e:
            assert False, print("Request Exception:", e)


    async def test_actual_save_data(self):
        assert self.__class__.payload_create_cache is not None
        assert self.__class__.data_create_cache is not None
        assert self.__class__.data_check_create_cache is not None

    async def test_values_date(self):
        data_response_create = self.__class__.data_create_cache
        data_response_check_create = self.__class__.data_check_create_cache
        payload = self.__class__.payload_create_cache

        assert ValidatePostUserCase.response_default(data_response_create), "Ответ не валиден"
        assert ValidateGetUserCase.response_default(data_response_check_create), "Ответ не валиден"

        assert all([data_response_create['payload']['student']['age'] == data_response_check_create['payload']['student']['age'],
                    data_response_create['payload']['student']['age'] == payload['age']])
        assert all([data_response_create['payload']['student']['themes'] == data_response_check_create['payload']['student']['themes'],
                    data_response_create['payload']['student']['themes'] == payload['themes']])


@pytest.mark.dev
@pytest.mark.asyncio
class TestBFFUserStudentCacheUserCasesMoreThemes:

    payload_create_cache = None
    data_create_cache = None
    data_check_create_cache = None

    async def test_create_cache(self, domain, async_req):
        payload = PayloadPostUserCase.definition_payload('custom', 'more_theme')
        try:
            response = await async_req.post_request(domain, service, {}, payload,
                                                    {})

            assert response is not None
            assert response.status_code == 200

            data = response.json()
            self.__class__.data_create_cache = data
            self.__class__.payload_create_cache = payload

        except json.decoder.JSONDecodeError as e:
            assert False, print("Error decoding JSON response:", e)
        except Exception as e:
            assert False, print("Request Exception:", e)

    async def test_check_cache_after_create(self, domain, async_req):
        try:
            response = await async_req.get_request(domain, service, {},
                                                   {})
            assert response.status_code == 200

            data = response.json()
            self.__class__.data_check_create_cache = data

        except json.decoder.JSONDecodeError as e:
            assert False, print("Error decoding JSON response:", e)
        except Exception as e:
            assert False, print("Request Exception:", e)


    async def test_actual_data(self):
        assert self.__class__.payload_create_cache is not None
        assert self.__class__.data_create_cache is not None
        assert self.__class__.data_check_create_cache is not None

    async def test_values(self):
        data_response_create = self.__class__.data_create_cache
        data_response_check_create = self.__class__.data_check_create_cache
        payload = self.__class__.payload_create_cache

        assert ValidatePostUserCase.response_default(data_response_create), "Ответ не валиден"
        assert ValidateGetUserCase.response_default(data_response_check_create), "Ответ не валиден"

        assert all([data_response_create['payload']['student']['age'] == data_response_check_create['payload']['student']['age'],
                    data_response_create['payload']['student']['age'] == payload['age']])
        assert all([data_response_create['payload']['student']['themes'] == data_response_check_create['payload']['student']['themes'],
                    data_response_create['payload']['student']['themes'] == payload['themes']])