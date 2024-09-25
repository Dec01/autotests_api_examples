from faker import Faker

fake = Faker(locale="ru_RU")


class Payload2XX:
    @staticmethod
    def new_form_contact_sales():
        return {
            "firstname": fake.first_name(),
            "lastname": fake.last_name(),
            "surname": fake.last_name(),
            "email": fake.email(),
            "phoneNumber": f'+7{fake.msisdn()[3:]}',
            "message": fake.text(),
            "formType": "sales"
        }

    @staticmethod
    def new_form_contact_sales_phone8():
        return {
            "firstname": fake.first_name(),
            "lastname": fake.last_name(),
            "surname": fake.last_name(),
            "email": fake.email(),
            "phoneNumber": f'8{fake.msisdn()[3:]}',
            "message": fake.text(),
            "formType": "sales"
        }

    @staticmethod
    def new_form_contact_sales_file():
        return {
            "firstname": fake.first_name(),
            "lastname": fake.last_name(),
            "surname": fake.last_name(),
            "email": fake.email(),
            "phoneNumber": f'+7{fake.msisdn()[3:]}',
            "message": fake.text(),
            "formType": "sales",
            "fileUrls": [
                "https://img.png"
            ],
            "appealPage": "https://dev.dev/dev"
        }

    @staticmethod
    def new_form_contact_methodical_technical_support():
        return {
            "firstname": fake.first_name(),
            "lastname": fake.last_name(),
            "surname": fake.last_name(),
            "email": fake.email(),
            "phoneNumber": f'+7{fake.msisdn()[3:]}',
            "message": fake.text(),
            "formType": "methodicalTechnicalSupport"
        }

    @staticmethod
    def new_form_contact_other_appeals():
        return {
            "firstname": fake.first_name(),
            "lastname": fake.last_name(),
            "surname": fake.last_name(),
            "email": fake.email(),
            "phoneNumber": f'+7{fake.msisdn()[3:]}',
            "message": fake.text(),
            "formType": "otherAppeals"
        }


class Payload4XX:
    @staticmethod
    def new_form_contact_error_formtype():
        return {
            "firstname": fake.first_name(),
            "lastname": fake.last_name(),
            "surname": fake.last_name(),
            "email": fake.email(),
            "phoneNumber": f'+7{fake.msisdn()[3:]}',
            "message": fake.text(),
            "formType": "check"
        }

    @staticmethod
    def new_form_contact_nofirstname():
        return {
            "lastname": fake.last_name(),
            "surname": fake.last_name(),
            "email": fake.email(),
            "phoneNumber": f'+7{fake.msisdn()[3:]}',
            "message": fake.text(),
            "formType": "sales"
        }

    @staticmethod
    def new_form_contact_nolastname():
        return {
            "firstname": fake.first_name(),
            "surname": fake.last_name(),
            "email": fake.email(),
            "phoneNumber": f'+7{fake.msisdn()[3:]}',
            "message": fake.text(),
            "formType": "sales"
        }

    @staticmethod
    def new_form_contact_nosurname():
        return {
            "firstname": fake.first_name(),
            "lastname": fake.last_name(),
            "email": fake.email(),
            "phoneNumber": f'+7{fake.msisdn()[3:]}',
            "message": fake.text(),
            "formType": "sales"
        }

    @staticmethod
    def new_form_contact_noemail():
        return {
            "firstname": fake.first_name(),
            "lastname": fake.last_name(),
            "surname": fake.last_name(),
            "phoneNumber": f'+7{fake.msisdn()[3:]}',
            "message": fake.text(),
            "formType": "sales"
        }

    @staticmethod
    def new_form_contact_nophone():
        return {
            "firstname": fake.first_name(),
            "lastname": fake.last_name(),
            "surname": fake.last_name(),
            "email": fake.email(),
            "message": fake.text(),
            "formType": "sales"
        }

    @staticmethod
    def new_form_contact_nomessage():
        return {
            "firstname": fake.first_name(),
            "lastname": fake.last_name(),
            "surname": fake.last_name(),
            "email": fake.email(),
            "phoneNumber": f'+7{fake.msisdn()[3:]}',
            "formType": "sales"
        }

    @staticmethod
    def new_form_contact_noformtype():
        return {
            "firstname": fake.first_name(),
            "lastname": fake.last_name(),
            "surname": fake.last_name(),
            "email": fake.email(),
            "phoneNumber": f'+7{fake.msisdn()[3:]}',
            "message": fake.text(),
        }

    @staticmethod
    def new_form_contact_email_errortype():
        return {
            "firstname": fake.first_name(),
            "lastname": fake.last_name(),
            "surname": fake.last_name(),
            "email": "email.ru",
            "phoneNumber": f'+7{fake.msisdn()[3:]}',
            "message": fake.text(),
            "formType": "sales"
        }

    @staticmethod
    def new_form_contact_phone_errortype():
        return {
            "firstname": fake.first_name(),
            "lastname": fake.last_name(),
            "surname": fake.last_name(),
            "email": fake.email(),
            "phoneNumber": f'7{fake.msisdn()[3:]}',
            "message": fake.text(),
            "formType": "sales"
        }

    @staticmethod
    def new_form_contact_nobody():
        return {
        }

    @staticmethod
    def new_form_contact_firstname_length():
        return {
            "firstname": fake.pystr(min_chars=None, max_chars=70),
            "lastname": fake.last_name(),
            "surname": fake.last_name(),
            "email": fake.email(),
            "phoneNumber": f'+7{fake.msisdn()[3:]}',
            "message": fake.text(),
            "formType": "sales"
        }

    @staticmethod
    def new_form_contact_lastname_length():
        return {
            "firstname": fake.first_name(),
            "lastname": fake.pystr(min_chars=None, max_chars=70),
            "surname": fake.last_name(),
            "email": fake.email(),
            "phoneNumber": f'+7{fake.msisdn()[3:]}',
            "message": fake.text(),
            "formType": "sales"
        }

    @staticmethod
    def new_form_contact_surname_length():
        return {
            "firstname": fake.first_name(),
            "lastname": fake.last_name(),
            "surname": fake.pystr(min_chars=None, max_chars=70),
            "email": fake.email(),
            "phoneNumber": f'+7{fake.msisdn()[3:]}',
            "message": fake.text(),
            "formType": "sales"
        }

    @staticmethod
    def new_form_contact_email_length():
        return {
            "firstname": fake.first_name(),
            "lastname": fake.last_name(),
            "surname": fake.last_name(),
            "email": f'{fake.pystr(min_chars=None, max_chars=320) + fake.email()}',
            "phoneNumber": f'+7{fake.msisdn()[3:]}',
            "message": fake.text(),
            "formType": "sales"
        }

    @staticmethod
    def new_form_contact_phone_lenght():
        return {
            "firstname": fake.first_name(),
            "lastname": fake.last_name(),
            "surname": fake.last_name(),
            "email": fake.email(),
            "phoneNumber": f'+7{fake.msisdn()[3:] + fake.bothify(text="#######")}',
            "message": fake.text(),
            "formType": "sales"
        }

    @staticmethod
    def new_form_contact_emty_firstname():
        return {
            "firstname": "",
            "lastname": fake.last_name(),
            "surname": fake.last_name(),
            "email": fake.email(),
            "phoneNumber": f'+7{fake.msisdn()[3:]}',
            "message": fake.text(),
            "formType": "sales"
        }

    @staticmethod
    def new_form_contact_emty_lastname():
        return {
            "firstname": fake.first_name(),
            "lastname": "",
            "surname": fake.last_name(),
            "email": fake.email(),
            "phoneNumber": f'+7{fake.msisdn()[3:]}',
            "message": fake.text(),
            "formType": "sales"
        }

    @staticmethod
    def new_form_contact_emty_surname():
        return {
            "firstname": fake.first_name(),
            "lastname": fake.last_name(),
            "surname": "",
            "email": fake.email(),
            "phoneNumber": f'+7{fake.msisdn()[3:]}',
            "message": fake.text(),
            "formType": "sales"
        }

    @staticmethod
    def new_form_contact_emty_email():
        return {
            "firstname": fake.first_name(),
            "lastname": fake.last_name(),
            "surname": fake.last_name(),
            "email": "",
            "phoneNumber": f'+7{fake.msisdn()[3:]}',
            "message": fake.text(),
            "formType": "sales"
        }

    @staticmethod
    def new_form_contact_emty_phone():
        return {
            "firstname": fake.first_name(),
            "lastname": fake.last_name(),
            "surname": fake.last_name(),
            "email": fake.email(),
            "phoneNumber": "",
            "message": fake.text(),
            "formType": "sales"
        }

    @staticmethod
    def new_form_contact_emty_message():
        return {
            "firstname": fake.first_name(),
            "lastname": fake.last_name(),
            "surname": fake.last_name(),
            "email": fake.email(),
            "phoneNumber": f'+7{fake.msisdn()[3:]}',
            "message": "",
            "formType": "sales"
        }

    @staticmethod
    def new_form_contact_emty_formType():
        return {
            "firstname": fake.first_name(),
            "lastname": fake.last_name(),
            "surname": fake.last_name(),
            "email": fake.email(),
            "phoneNumber": f'+7{fake.msisdn()[3:]}',
            "message": fake.text(),
            "formType": ""
        }

    @staticmethod
    def new_form_contact_extra_element():
        return {
            "firstname": fake.first_name(),
            "lastname": fake.last_name(),
            "surname": fake.last_name(),
            "email": fake.email(),
            "phoneNumber": f'+7{fake.msisdn()[3:]}',
            "message": fake.text(),
            "formType": "sales",
            "test": "test"
        }

