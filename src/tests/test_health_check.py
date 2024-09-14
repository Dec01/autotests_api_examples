import pytest

from src.models.user_paths import PathsServices
from src.models.payloads.payload_health import HealthValidate

service = PathsServices.services_paths.get('health_check')

@pytest.mark.dev
class TestHealthCheck:

    def test_default_check200(self, domain, req):
        endpoint = service.get('service_endpoints_path').get('general_path').get('url')
        try:
            response = req.get_request(domain, endpoint, {}, {})
            data = response.json()
            assert response.status_code == 200
            assert HealthValidate.response_health_check(data)

        except req.exceptions.HTTPError as errh:
            print("Http Error:", errh)
        except req.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
        except req.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
        except req.exceptions.RequestException as err:
            print("OOps: Something Else", err)
