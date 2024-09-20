import json
import pytest

from src.models.paths.user_paths import PathsServices
from src.models.processings.processing_request import RequestToken
from src.models.payloads.model_get_health_default import ValidateGetHealthDefault

service = PathsServices.services_paths.get('health_check')
roles = RequestToken.token_role.keys()
token_admin = RequestToken.response_token_role('ROLE_SUPER_ADMIN')
permissions_health = ['ROLE_MANAGER', 'ROLE_EDITOR', 'ROLE_SUPER_ADMIN']



@pytest.mark.dev
@pytest.mark.asyncio
class TestHealthPermissions:

    @pytest.mark.parametrize('roles', roles)
    async def test_get_health_check(self, domain, async_req, roles):
        token_header = RequestToken.response_token_role(roles)
        endpoint = service.get('service_endpoints_path').get('general_path').get('url')
        try:
            if roles not in permissions_health:
                response = await async_req.get_request(domain, endpoint, {}, token_header)
                assert response is not None
                assert response.status_code == 403
            else:
                response = await async_req.get_request(domain, endpoint, {}, token_header)
                assert response is not None
                assert response.status_code == 200
                data = response.json()
                assert ValidateGetHealthDefault.response_default(data)
        except json.decoder.JSONDecodeError as e:
            assert False, print("Error decoding JSON response:", e)
        except Exception as e:
            assert False, print("Request Exception:", e)
