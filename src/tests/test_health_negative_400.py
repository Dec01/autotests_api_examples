import pytest
import json

from src.models.paths.user_paths import PathsServices
from src.models.payloads.model_post_health_negative import PayloadPostHealth, ValidatePostHealth

service = PathsServices.services_paths.get('health_check')

@pytest.mark.dev
@pytest.mark.asyncio
class TestHealth400:

    data_post_user_student_cache = None
    data_get_user_student_cache = None

    async def test_post_user_student_cache_more_element(self, domain, async_req):
        payload = PayloadPostHealth.definition_payload('custom', 'more_element')
        try:
            response = await async_req.post_request(domain, service, {}, payload,
                                                    {})

            assert response is not None
            assert response.status_code == 400

            data = response.json()
            self.__class__.data_post_user_student_cache = data

        except json.decoder.JSONDecodeError as e:
            assert False, print("Error decoding JSON response:", e)
        except Exception as e:
            assert False, print("Request Exception:", e)

    async def test_post_user_student_cache_more_element_validate_response(self):
        assert self.__class__.data_post_user_student_cache is not None, "Данные не должны быть None"
        assert ValidatePostHealth.response_error_more_element(self.__class__.data_post_user_student_cache), \
            "Ответ не валиден"


    async def test_post_user_student_cache_no_element(self, domain, async_req):
        payload = PayloadPostHealth.definition_payload('custom', 'no_element')
        try:
            response = await async_req.post_request(domain, service, {}, payload,
                                                    {})

            assert response is not None
            assert response.status_code == 400

            data = response.json()
            self.__class__.data_post_user_student_cache = data

        except json.decoder.JSONDecodeError as e:
            assert False, print("Error decoding JSON response:", e)
        except Exception as e:
            assert False, print("Request Exception:", e)

    async def test_post_user_student_cache_no_element_validate_response(self):
        assert self.__class__.data_post_user_student_cache is not None, "Данные не должны быть None"
        assert ValidatePostHealth.response_error_no_element(self.__class__.data_post_user_student_cache), \
            "Ответ не валиден"

    @pytest.mark.parametrize('value', ['ages', 'themes'])
    async def test_post_user_student_cache_fake_value_element(self, domain, async_req, value):
        payload = PayloadPostHealth.definition_payload('custom', 'fake_value_element', value)
        try:
            response = await async_req.post_request(domain, service, {}, payload,
                                                    {})

            assert response is not None
            assert response.status_code == 400

            data = response.json()
            self.__class__.data_post_user_student_cache = data

        except json.decoder.JSONDecodeError as e:
            assert False, print("Error decoding JSON response:", e)
        except Exception as e:
            assert False, print("Request Exception:", e)

    async def test_post_user_student_cache_fake_value_element_validate_response(self):
        assert self.__class__.data_post_user_student_cache is not None, "Данные не должны быть None"
        assert ValidatePostHealth.response_error_fake_value_element(self.__class__.data_post_user_student_cache), \
            "Ответ не валиден"