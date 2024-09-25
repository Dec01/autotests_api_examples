import unittest
import pytest
import requests

from src.models.payloads.model_json_payload import Payload2XX, Payload4XX
from src.models.paths.user_paths import PathsServices
from src.models.processings.processing_request import RequestLanguage
from src.models.processings.processing_validate import ResponseErrorRU

path = PathsServices.services_paths.get('health_check')

@pytest.mark.stage
@pytest.mark.dev
class TestFormContact(unittest.TestCase):
    session = requests.Session()
    session.verify = False

    @pytest.fixture(autouse=True)
    def prepare_fixture(self, domain):
        self.domain = domain

    def test_create_form_contact_sales_checkStatus200(self):
        payload = Payload2XX.new_form_contact_sales()
        response = requests.post(self.domain + path, json=payload)
        data = response.json()
        elements = response.content.decode('unicode-escape')
        assert response.status_code == 200, 'Check code status endpoint'
        assert data['code'] == "0", "Check code"
        assert data['payload']['type'] == "contactForm", "Check type"
        assert type(data['payload']['id']) is str, 'Check type id'
        self.assertIn(payload['email'], elements)
        self.assertIn(payload['phoneNumber'], elements)
        self.assertIn(payload['message'], elements)
        self.assertIn(payload['formType'], elements)
        assert data['payload']['language'] == "ru", "Check message"
        assert data['message'] == "Success", "Check message"

    def test_create_form_contact_sales_phone8_checkStatus200(self):
        payload = Payload2XX.new_form_contact_sales_phone8()
        response = requests.post(self.domain + path, json=payload)
        data = response.json()
        elements = response.content.decode('unicode-escape')
        assert response.status_code == 200, 'Check code status endpoint'
        assert data['code'] == "0", "Check code"
        assert data['payload']['type'] == "contactForm", "Check type"
        assert type(data['payload']['id']) is str, 'Check type id'
        self.assertIn(payload['email'], elements)
        self.assertIn(payload['phoneNumber'], elements)
        self.assertIn(payload['message'], elements)
        self.assertIn(payload['formType'], elements)
        assert data['payload']['language'] == "ru", "Check message"
        assert data['message'] == "Success", "Check message"

    def test_create_form_contact_sales_file_checkStatus200(self):
        payload = Payload2XX.new_form_contact_sales_file()
        response = requests.post(self.domain + path, json=payload)
        data = response.json()
        elements = response.content.decode('unicode-escape')
        assert response.status_code == 200, 'Check code status endpoint'
        assert data['code'] == "0", "Check code"
        assert data['payload']['type'] == "contactForm", "Check type"
        assert type(data['payload']['id']) is str, 'Check type id'
        self.assertIn(payload['email'], elements)
        self.assertIn(payload['phoneNumber'], elements)
        self.assertIn(payload['message'], elements)
        self.assertIn(payload['formType'], elements)
        self.assertIn(payload['appealPage'], elements)
        self.assertIn(payload['fileUrls'][0], elements)
        assert data['payload']['language'] == "ru", "Check message"
        assert data['message'] == "Success", "Check message"

    def test_create_form_contact_en_sales_checkStatus200(self):
        payload = Payload2XX.new_form_contact_sales()
        response = requests.post(self.domain + path, headers=RequestLanguage.header_preference_en, json=payload)
        data = response.json()
        elements = response.content.decode('unicode-escape')
        assert response.status_code == 200, 'Check code status endpoint'
        assert data['code'] == "0", "Check code"
        assert data['payload']['type'] == "contactForm", "Check type"
        assert type(data['payload']['id']) is str, 'Check type id'
        self.assertIn(payload['email'], elements)
        self.assertIn(payload['phoneNumber'], elements)
        self.assertIn(payload['message'], elements)
        self.assertIn(payload['formType'], elements)
        assert data['payload']['language'] == "en", "Check message"
        assert data['message'] == "Success", "Check message"

    @pytest.mark.repeat(3)
    def test_create_form_contact_sales_recheckStatus200(self):
        payload = Payload2XX.new_form_contact_sales()
        response = requests.post(self.domain + path, json=payload)
        data = response.json()
        elements = response.content.decode('unicode-escape')
        assert response.status_code == 200, 'Check code status endpoint'
        assert data['code'] == "0", "Check code"
        assert data['payload']['type'] == "contactForm", "Check type"
        assert type(data['payload']['id']) is str, 'Check type id'
        self.assertIn(payload['email'], elements)
        self.assertIn(payload['phoneNumber'], elements)
        self.assertIn(payload['message'], elements)
        self.assertIn(payload['formType'], elements)
        assert data['payload']['language'] == "ru", "Check message"
        assert data['message'] == "Success", "Check message"

    def test_create_form_contact_other_appeals_checkStatus200(self):
        payload = Payload2XX.new_form_contact_other_appeals()
        response = requests.post(self.domain + path, json=payload)
        data = response.json()
        elements = response.content.decode('unicode-escape')
        assert response.status_code == 200, 'Check code status endpoint'
        assert data['code'] == "0", "Check code"
        assert data['payload']['type'] == "contactForm", "Check type"
        assert type(data['payload']['id']) is str, 'Check type id'
        self.assertIn(payload['email'], elements)
        self.assertIn(payload['phoneNumber'], elements)
        self.assertIn(payload['message'], elements)
        self.assertIn(payload['formType'], elements)
        assert data['payload']['language'] == "ru", "Check message"
        assert data['message'] == "Success", "Check message"

    @pytest.mark.repeat(3)
    def test_create_form_contact_other_appeals_recheckStatus200(self):
        payload = Payload2XX.new_form_contact_other_appeals()
        response = requests.post(self.domain + path, json=payload)
        data = response.json()
        elements = response.content.decode('unicode-escape')
        assert response.status_code == 200, 'Check code status endpoint'
        assert data['code'] == "0", "Check code"
        assert data['payload']['type'] == "contactForm", "Check type"
        assert type(data['payload']['id']) is str, 'Check type id'
        self.assertIn(payload['email'], elements)
        self.assertIn(payload['phoneNumber'], elements)
        self.assertIn(payload['message'], elements)
        self.assertIn(payload['formType'], elements)
        assert data['payload']['language'] == "ru", "Check message"
        assert data['message'] == "Success", "Check message"

    def test_create_form_contact_methodical_technical_support_checkStatus200(self):
        payload = Payload2XX.new_form_contact_methodical_technical_support()
        response = requests.post(self.domain + path, json=payload)
        data = response.json()
        elements = response.content.decode('unicode-escape')
        assert response.status_code == 200, 'Check code status endpoint'
        assert data['code'] == "0", "Check code"
        assert data['payload']['type'] == "contactForm", "Check type"
        assert type(data['payload']['id']) is str, 'Check type id'
        self.assertIn(payload['email'], elements)
        self.assertIn(payload['phoneNumber'], elements)
        self.assertIn(payload['message'], elements)
        self.assertIn(payload['formType'], elements)
        assert data['payload']['language'] == "ru", "Check message"
        assert data['message'] == "Success", "Check message"

    @pytest.mark.repeat(3)
    def test_create_form_contact_methodical_technical_support_recheckStatus200(self):
        payload = Payload2XX.new_form_contact_methodical_technical_support()
        response = requests.post(self.domain + path, json=payload)
        data = response.json()
        elements = response.content.decode('unicode-escape')
        assert response.status_code == 200, 'Check code status endpoint'
        assert data['code'] == "0", "Check code"
        assert data['payload']['type'] == "contactForm", "Check type"
        assert type(data['payload']['id']) is str, 'Check type id'
        self.assertIn(payload['email'], elements)
        self.assertIn(payload['phoneNumber'], elements)
        self.assertIn(payload['message'], elements)
        self.assertIn(payload['formType'], elements)
        assert data['payload']['language'] == "ru", "Check message"
        assert data['message'] == "Success", "Check message"

    def test_create_form_contact_emty_phone_checkStatus200(self):
        payload = Payload4XX.new_form_contact_emty_phone()
        response = requests.post(self.domain + path, json=payload)
        data = response.json()
        assert response.status_code == 200, 'Check code status endpoint'
        assert data['code'] == "0", "Check code"
        assert data['payload']['type'] == "contactForm", "Check type"
        assert data['payload']['language'] == "ru", "Check message"
        assert data['message'] == "Success", "Check message"

    def test_create_form_contact_nophone_checkStatus200(self):
        payload = Payload4XX.new_form_contact_nophone()
        response = requests.post(self.domain + path, json=payload)
        data = response.json()
        assert response.status_code == 200, 'Check code status endpoint'
        assert data['code'] == "0", "Check code"
        assert data['payload']['type'] == "contactForm", "Check type"
        assert data['payload']['language'] == "ru", "Check message"
        assert data['message'] == "Success", "Check message"

    def test_create_form_contact_get_checkStatus405(self):
        payload = Payload2XX.new_form_contact_sales()
        response = requests.get(self.domain + path, json=payload)
        data = response.json()
        assert response.status_code == 405, 'Check code status endpoint'
        assert type(data['code']) is str, 'Check code'
        assert data['error']['allowed'] == ['POST'], 'Check error'
        assert data['message'] == "Method not allowed", 'Check message'

    def test_create_form_contact_patch_checkStatus405(self):
        payload = Payload2XX.new_form_contact_sales()
        response = requests.patch(self.domain + path, json=payload)
        data = response.json()
        assert response.status_code == 405, 'Check code status endpoint'
        assert type(data['code']) is str, 'Check code'
        assert data['error']['allowed'] == ['POST'], 'Check error'
        assert data['message'] == "Method not allowed", 'Check message'

    def test_create_form_contact_delete_checkStatus405(self):
        payload = Payload2XX.new_form_contact_sales()
        response = requests.delete(self.domain + path, json=payload)
        data = response.json()
        assert response.status_code == 405, 'Check code status endpoint'
        assert type(data['code']) is str, 'Check code'
        assert data['error']['allowed'] == ['POST'], 'Check error'
        assert data['message'] == "Method not allowed", 'Check message'

    def test_create_form_contact_put_checkStatus405(self):
        payload = Payload2XX.new_form_contact_sales()
        response = requests.put(self.domain + path, json=payload)
        data = response.json()
        assert response.status_code == 405, 'Check code status endpoint'
        assert type(data['code']) is str, 'Check code'
        assert data['error']['allowed'] == ['POST'], 'Check error'
        assert data['message'] == "Method not allowed", 'Check message'

    def test_create_form_contact_error_formtype_checkStatus400(self):
        payload = Payload4XX.new_form_contact_error_formtype()
        response = requests.post(self.domain + path, json=payload)
        data = response.json()
        assert response.status_code == 400, 'Check code status endpoint'
        assert type(data['code']) is str, 'Check code'
        assert data['error']['fields']['formType'] == ResponseErrorRU.choice_invalid, 'Check error'
        assert data['message'] == "Form is not valid", 'Check message'

    def test_create_form_contact_nofirstname_checkStatus400(self):
        payload = Payload4XX.new_form_contact_nofirstname()
        response = requests.post(self.domain + path, json=payload)
        data = response.json()
        assert response.status_code == 400, 'Check code status endpoint'
        assert type(data['code']) is str, 'Check code'
        assert data['error']['fields']['firstname'] == ResponseErrorRU.blank, 'Check error'
        assert data['message'] == "Form is not valid", 'Check message'

    def test_create_form_contact_nolastname_checkStatus400(self):
        payload = Payload4XX.new_form_contact_nolastname()
        response = requests.post(self.domain + path, json=payload)
        data = response.json()
        assert response.status_code == 400, 'Check code status endpoint'
        assert type(data['code']) is str, 'Check code'
        assert data['error']['fields']['lastname'] == ResponseErrorRU.blank, 'Check error'
        assert data['message'] == "Form is not valid", 'Check message'

    def test_create_form_contact_nosurname_checkStatus400(self):
        payload = Payload4XX.new_form_contact_nosurname()
        response = requests.post(self.domain + path, json=payload)
        data = response.json()
        assert response.status_code == 400, 'Check code status endpoint'
        assert type(data['code']) is str, 'Check code'
        assert data['error']['fields']['surname'] == ResponseErrorRU.blank, 'Check error'
        assert data['message'] == "Form is not valid", 'Check message'

    def test_create_form_contact_noemail_checkStatus400(self):
        payload = Payload4XX.new_form_contact_noemail()
        response = requests.post(self.domain + path, json=payload)
        data = response.json()
        assert response.status_code == 400, 'Check code status endpoint'
        assert type(data['code']) is str, 'Check code'
        assert data['error']['fields']['email'] == ResponseErrorRU.blank, 'Check error'
        assert data['message'] == "Form is not valid", 'Check message'

    def test_create_form_contact_nomessage_checkStatus400(self):
        payload = Payload4XX.new_form_contact_nomessage()
        response = requests.post(self.domain + path, json=payload)
        data = response.json()
        assert response.status_code == 400, 'Check code status endpoint'
        assert type(data['code']) is str, 'Check code'
        assert data['error']['fields']['message'] == ResponseErrorRU.blank, 'Check error'
        assert data['message'] == "Form is not valid", 'Check message'

    def test_create_form_contact_noformtype_checkStatus400(self):
        payload = Payload4XX.new_form_contact_noformtype()
        response = requests.post(self.domain + path, json=payload)
        data = response.json()
        assert response.status_code == 400, 'Check code status endpoint'
        assert type(data['code']) is str, 'Check code'
        assert data['error']['fields']['formType'] == ResponseErrorRU.blank, 'Check error'
        assert data['message'] == "Form is not valid", 'Check message'

    def test_create_form_contact_nobody_checkStatus400(self):
        payload = Payload4XX.new_form_contact_nobody()
        response = requests.post(self.domain + path, json=payload)
        data = response.json()
        assert response.status_code == 400, 'Check code status endpoint'
        assert type(data['code']) is str, 'Check code'
        assert data['error'] == [], 'Check error'
        assert data['message'] == "form is not submitted", 'Check message'

    def test_create_form_contact_email_errortype_checkStatus400(self):
        payload = Payload4XX.new_form_contact_email_errortype()
        response = requests.post(self.domain + path, json=payload)
        data = response.json()
        assert response.status_code == 400, 'Check code status endpoint'
        assert type(data['code']) is str, 'Check code'
        assert data['error']['fields']['email'] == ResponseErrorRU.not_valid_email, 'Check error'
        assert data['message'] == "Form is not valid", 'Check message'

    def test_create_form_contact_phone_errortype_checkStatus400(self):
        payload = Payload4XX.new_form_contact_phone_errortype()
        response = requests.post(self.domain + path, json=payload)
        data = response.json()
        assert response.status_code == 400, 'Check code status endpoint'
        assert type(data['code']) is str, 'Check code'
        assert data['error']['fields']['phoneNumber'] == ResponseErrorRU.not_valid, 'Check error'
        assert data['message'] == "Form is not valid", 'Check message'

    def test_create_form_contact_email_length_checkStatus400(self):
        payload = Payload4XX.new_form_contact_email_length()
        response = requests.post(self.domain + path, json=payload)
        data = response.json()
        assert response.status_code == 400, 'Check code status endpoint'
        assert type(data['code']) is str, 'Check code'
        assert data['error']['fields']['email'] == ResponseErrorRU.long_email, 'Check error'
        assert data['message'] == "Form is not valid", 'Check message'

    def test_create_form_contact_firstname_length_checkStatus400(self):
        payload = Payload4XX.new_form_contact_firstname_length()
        response = requests.post(self.domain + path, json=payload)
        data = response.json()
        assert response.status_code == 400, 'Check code status endpoint'
        assert type(data['code']) is str, 'Check code'
        assert data['error']['fields']['firstname'] == ResponseErrorRU.long_name, 'Check error'
        assert data['message'] == "Form is not valid", 'Check message'

    def test_create_form_contact_lastname_length_checkStatus400(self):
        payload = Payload4XX.new_form_contact_lastname_length()
        response = requests.post(self.domain + path, json=payload)
        data = response.json()
        assert response.status_code == 400, 'Check code status endpoint'
        assert type(data['code']) is str, 'Check code'
        assert data['error']['fields']['lastname'] == ResponseErrorRU.long_name, 'Check error'
        assert data['message'] == "Form is not valid", 'Check message'

    def test_create_form_contact_surname_length_checkStatus400(self):
        payload = Payload4XX.new_form_contact_surname_length()
        response = requests.post(self.domain + path, json=payload)
        data = response.json()
        assert response.status_code == 400, 'Check code status endpoint'
        assert type(data['code']) is str, 'Check code'
        assert data['error']['fields']['surname'] == ResponseErrorRU.long_name, 'Check error'
        assert data['message'] == "Form is not valid", 'Check message'

    def test_create_form_contact_phone_length_checkStatus400(self):
        payload = Payload4XX.new_form_contact_phone_lenght()
        response = requests.post(self.domain + path, json=payload)
        data = response.json()
        assert response.status_code == 400, 'Check code status endpoint'
        assert type(data['code']) is str, 'Check code'
        assert data['error']['fields']['phoneNumber'] == ResponseErrorRU.not_valid, 'Check error'
        assert data['message'] == "Form is not valid", 'Check message'

    def test_create_form_contact_extra_element_checkStatus400(self):
        payload = Payload4XX.new_form_contact_extra_element()
        response = requests.post(self.domain + path, json=payload)
        data = response.json()
        assert response.status_code == 400, 'Check code status endpoint'
        assert type(data['code']) is str, 'Check code'
        assert data['error']['notExpectedFields'] == ['test'], 'Check error'
        assert data['message'] == "Form is not valid", 'Check message'

    def test_create_form_contact_emty_firstname_checkStatus400(self):
        payload = Payload4XX.new_form_contact_emty_firstname()
        response = requests.post(self.domain + path, json=payload)
        data = response.json()
        assert response.status_code == 400, 'Check code status endpoint'
        assert type(data['code']) is str, 'Check code'
        assert data['error']['fields']['firstname'] == ResponseErrorRU.blank, 'Check error'
        assert data['message'] == "Form is not valid", 'Check message'

    def test_create_form_contact_emty_lastname_checkStatus400(self):
        payload = Payload4XX.new_form_contact_emty_lastname()
        response = requests.post(self.domain + path, json=payload)
        data = response.json()
        assert response.status_code == 400, 'Check code status endpoint'
        assert type(data['code']) is str, 'Check code'
        assert data['error']['fields']['lastname'] == ResponseErrorRU.blank, 'Check error'
        assert data['message'] == "Form is not valid", 'Check message'

    def test_create_form_contact_emty_surname_checkStatus400(self):
        payload = Payload4XX.new_form_contact_emty_surname()
        response = requests.post(self.domain + path, json=payload)
        data = response.json()
        assert response.status_code == 400, 'Check code status endpoint'
        assert type(data['code']) is str, 'Check code'
        assert data['error']['fields']['surname'] == ResponseErrorRU.blank, 'Check error'
        assert data['message'] == "Form is not valid", 'Check message'

    def test_create_form_contact_emty_email_checkStatus400(self):
        payload = Payload4XX.new_form_contact_emty_email()
        response = requests.post(self.domain + path, json=payload)
        data = response.json()
        assert response.status_code == 400, 'Check code status endpoint'
        assert type(data['code']) is str, 'Check code'
        assert data['error']['fields']['email'] == ResponseErrorRU.blank, 'Check error'
        assert data['message'] == "Form is not valid", 'Check message'

    def test_create_form_contact_emty_message_checkStatus400(self):
        payload = Payload4XX.new_form_contact_emty_message()
        response = requests.post(self.domain + path, json=payload)
        data = response.json()
        assert response.status_code == 400, 'Check code status endpoint'
        assert type(data['code']) is str, 'Check code'
        assert data['error']['fields']['message'] == ResponseErrorRU.blank, 'Check error'
        assert data['message'] == "Form is not valid", 'Check message'

    def test_create_form_contact_emty_formType_checkStatus400(self):
        payload = Payload4XX.new_form_contact_emty_formType()
        response = requests.post(self.domain + path, json=payload)
        data = response.json()
        assert response.status_code == 400, 'Check code status endpoint'
        assert type(data['code']) is str, 'Check code'
        assert data['error']['fields']['formType'] == ResponseErrorRU.blank, 'Check error'
        assert data['message'] == "Form is not valid", 'Check message'