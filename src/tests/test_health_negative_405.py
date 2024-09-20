import json
import pytest

from src.models.paths.user_paths import PathsServices, MethodsList

service = PathsServices.services_paths.get('health_check')
method = MethodsList.methods.keys()

@pytest.mark.dev
@pytest.mark.asyncio
class TestHealth405:

    @pytest.mark.parametrize('method', method)
    async def test_get_health_check(self, domain, async_req, method):
        endpoint = service.get('service_endpoints_path').get('general_path').get('url')
        try:
            if method == 'GET':
                response = await async_req.definition_method_request(method, domain, endpoint, {}, {}, {}, {})
                assert response is not None
                assert response.status_code not in [400, 405, 500, 502]
            else:
                response = await async_req.definition_method_request(method, domain, endpoint, {}, {}, {}, {})
                assert response is not None
                assert response.status_code == 405
        except json.decoder.JSONDecodeError as e:
            assert False, print("Error decoding JSON response:", e)
        except Exception as e:
            assert False, print("Request Exception:", e)