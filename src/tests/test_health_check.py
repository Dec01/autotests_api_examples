import pytest
from src.models.user_paths import UserPath
from src.models.payloads.payload_health import HealthValidate
path = UserPath.path_health_chek

@pytest.mark.stage
@pytest.mark.dev
class TestHealthCheck:

    def test_default_check200(self, domain, req):
        try:
            response = req.get_request(domain, path, {}, {})
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
