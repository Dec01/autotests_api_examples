import json
import re

import pytest

from src.models.paths.user_paths import PathsServices
from src.models.payloads.model_get_health_params import ParamsGetHealthParams, ValidateGetHealthParams
from src.models.payloads.model_post_health_default_and_custom import PayloadPostHealthDefault, ValidatePostHealthDefault

service = PathsServices.services_paths.get('health_check')
get_filters_keys = ParamsGetHealthParams.request_filter(None).keys()
get_sorts_keys = ParamsGetHealthParams.request_sorts('queue', None, None)
@pytest.mark.dev
class TestHealthCheckV1Req:

    uuid_list = []

    @pytest.mark.dependency(name="test_main")
    @pytest.mark.parametrize('generation', range(10))
    async def test_post_payload_generation(self, domain, async_req, generation):
        payload = PayloadPostHealthDefault.definition_payload('12345', 'default')
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

    @pytest.mark.dependency(depends=["test_main"], force=True)
    @pytest.mark.parametrize('filter', get_filters_keys)
    async def test_get_health_check_filters(self, domain, async_req, filter):
        endpoint = service.get('service_endpoints_path').get('general_path').get('url')
        params = ParamsGetHealthParams.request_filter(filter)

        try:
            response = await async_req.get_request(domain, endpoint, ''.join(params), {})
            assert response is not None
            assert response.status_code == 200
            data = response.json()

            for item in data['items']:
                if params[2] == 'false':
                    assert not item[filter]
                elif params[2] == 'true':
                    assert item[filter]
                else:
                    assert item[filter] == params[2]

            assert ValidateGetHealthParams.response_default(data)
        except json.decoder.JSONDecodeError as e:
            assert False, print("Error decoding JSON response:", e)
        except Exception as e:
            assert False, print("Request Exception:", e)


    @pytest.mark.dependency(depends=["test_main"], force=True)
    @pytest.mark.parametrize('sort', get_sorts_keys)
    async def test_get_health_check_sort_active(self, domain, async_req, sort):
        endpoint = service.get('service_endpoints_path').get('general_path').get('url')
        params = ParamsGetHealthParams.request_sorts(None, 'active', sort)
        try:
            response = await async_req.get_request(domain, endpoint, ''.join(params), {})
            assert response is not None
            assert response.status_code == 200
            data = response.json()

            items = data['items']

            if sort == 'asc':
                for index, item in enumerate(items):
                    if item['active']:
                        assert item['active'], f"Ошибка: ожидается True после первого True на индексе {index}"

            elif sort == 'desc':
                for index, item in enumerate(items):
                    if not item['active']:
                        assert not item['active'], f"Ошибка: ожидается False после первого False на индексе {index}"

            assert ValidateGetHealthParams.response_default(data)
        except json.decoder.JSONDecodeError as e:
            assert False, print("Error decoding JSON response:", e)
        except Exception as e:
            assert False, print("Request Exception:", e)

    @pytest.mark.dependency(depends=["test_main"], force=True)
    @pytest.mark.parametrize('sort', get_sorts_keys)
    async def test_get_health_check_sort_title(self, domain, async_req, sort):
        endpoint = service.get('service_endpoints_path').get('general_path').get('url')
        params = ParamsGetHealthParams.request_sorts(None, 'title', sort)
        try:
            response = await async_req.get_request(domain, endpoint, ''.join(params), {})
            assert response is not None
            assert response.status_code == 200
            data = response.json()

            items = data['items']

            titles = [item['title'] for item in items]

            def custom_sort_key(title):
                title_cleaned = title.replace(' ', '').lower()
                numeric_part = re.match(r'(\d+)', title_cleaned)
                if numeric_part:
                    return (0, title_cleaned)
                elif re.match(r'[a-z]', title_cleaned):
                    return (1, title_cleaned)
                elif re.match(r'[а-яё]', title_cleaned):
                    return (2, title_cleaned)
                return (3, title_cleaned)

            if sort == 'asc':
                sorted_titles = sorted(titles, key=custom_sort_key)
                for index in range(len(titles)):
                    assert titles[index] == sorted_titles[
                        index], f"Ошибка: {titles[index]} не соответствует ожидаемому порядку на индексе {index}"

            elif sort == 'desc':
                sorted_titles = sorted(titles, key=custom_sort_key, reverse=True)
                for index in range(len(titles)):
                    assert titles[index] == sorted_titles[
                        index], f"Ошибка: {titles[index]} не соответствует ожидаемому порядку на индексе {index}"

            assert ValidateGetHealthParams.response_default(data)
        except json.decoder.JSONDecodeError as e:
            assert False, print("Error decoding JSON response:", e)
        except Exception as e:
            assert False, print("Request Exception:", e)