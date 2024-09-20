import json
import pytest

from src.models.paths.user_paths import PathsServices
from src.models.payloads.model_post_health_default_and_custom import PayloadPostHealthDefault, ValidatePostHealthDefault

service = PathsServices.services_paths.get('health_check')
post_required_elements = PayloadPostHealthDefault.definition_missing_required_elements(None).keys()
post_string_length_elements = PayloadPostHealthDefault.payload_string_length_elements().keys()
@pytest.mark.dev
@pytest.mark.asyncio
class TestHealthElemnts:

    uuid_list = []

    @pytest.mark.dependency(name="test_main")
    async def test_post_health__only_required_elements(self, domain, async_req):
        payload = PayloadPostHealthDefault.definition_payload('1234', 'custom', "ore", None)
        endpoint = service.get('service_endpoints_path').get('general_path').get('url')
        try:
            response = await async_req.post_request(domain, endpoint, {}, payload, {})
            assert response.status_code == 200

            data = response.json()
            uuid = data['payload']['uuid']
            self.__class__.uuid_list.append(uuid)

            assert ValidatePostHealthDefault.response_default(data)
        except json.decoder.JSONDecodeError as e:
            assert False, print("Error decoding JSON response:", e)
        except Exception as e:
            assert False, print("Request Exception:", e)


    @pytest.mark.parametrize('required_element', post_required_elements)
    async def test_post_health__missing_required_elements(self, domain, async_req, required_element):
        payload = PayloadPostHealthDefault.definition_payload('1234', 'custom', "mre", required_element)
        endpoint = service.get('service_endpoints_path').get('general_path').get('url')
        try:
            response = await async_req.post_request(domain, endpoint, {}, payload, {})

            if response.status_code == 200:
                data = response.json()
                uuid = data['payload']['uuid']
                self.__class__.uuid_list.append(uuid)
                assert False
            else:
                assert response.status_code == 400

        except json.decoder.JSONDecodeError as e:
            assert False, print("Error decoding JSON response:", e)
        except Exception as e:
            assert False, print("Request Exception:", e)


    @pytest.mark.parametrize('length_elements', post_string_length_elements)
    async def test_post_health__string_length_elements(self, domain, async_req, length_elements):
        payload = PayloadPostHealthDefault.definition_payload('1234', 'custom', "sle", length_elements)
        endpoint = service.get('service_endpoints_path').get('general_path').get('url')
        try:
            response = await async_req.post_request(domain, endpoint, {}, payload, {})

            if response.status_code == 200:
                data = response.json()
                uuid = data['payload']['uuid']
                self.__class__.uuid_list.append(uuid)
                assert False
            else:
                assert response.status_code == 400

        except json.decoder.JSONDecodeError as e:
            assert False, print("Error decoding JSON response:", e)
        except Exception as e:
            assert False, print("Request Exception:", e)


    @pytest.mark.dependency(depends=["test_main"], force=True)
    async def test_delete_health(self, domain, async_req):
        endpoint = service.get('service_endpoints_path').get('general_path').get('url')
        try:
            for uuid in self.__class__.uuid_list:
                response = await async_req.delete_request(domain, endpoint + f'/{uuid}', {})
                assert response.status_code == 200
        except json.decoder.JSONDecodeError as e:
            assert False, print("Error decoding JSON response:", e)
        except Exception as e:
            assert False, print("Request Exception:", e)