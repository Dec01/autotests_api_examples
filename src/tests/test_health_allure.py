import json
import pytest
import allure

from src.models.paths.user_paths import PathsServices
from src.models.payloads.model_get_health_default import ValidateGetHealthDefault
from src.models.payloads.model_post_health_default_and_custom import PayloadPostHealthDefault

service = PathsServices.services_paths.get('health_check')


@allure.epic('Микросервис "Allure"')
@allure.feature('Установка меток')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.dev
@pytest.mark.asyncio
class TestHealthAllure:

    async def test_get_health_check(self, domain, async_req):
        endpoint = service.get('service_endpoints_path').get('general_path').get('url')
        payload = PayloadPostHealthDefault.definition_payload('1234', 'custom', "ore", None)
        try:
            with allure.step("Формирование данных и запрос на эндпоинт"):
                response = await async_req.post_request(domain, endpoint, {}, payload, {})
            with allure.step("Проверка корретности ответа"):
                with allure.step("Статус код"):
                    assert response is not None
                    assert response.status_code == 200
                with allure.step("Валидация тела ответа"):
                    data = response.json()
                    assert ValidateGetHealthDefault.response_default(data)
        except json.decoder.JSONDecodeError as e:
            assert False, print("Error decoding JSON response:", e)
        except Exception as e:
            assert False, print("Request Exception:", e)
