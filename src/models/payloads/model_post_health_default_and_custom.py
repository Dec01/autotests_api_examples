import random

from typing import List, Optional
from faker import Faker
from pydantic import Field, ValidationError, BaseModel, field_validator

from src.models.processings.processing_validate import PydanticResponseError
from src.models.utils.date import DateGeneration2Days

fake = Faker(locale="ru_RU")
start_date = DateGeneration2Days.start_date()
end_date = DateGeneration2Days.end_date()

class RequestPostHealthDefaultInside(BaseModel):
    int: int = None


class RequestPostHealthDefault(BaseModel):
    url: str = None
    bool: bool = None
    text: Optional[str] = None
    dateStart: object = None
    dateEnd: str = None
    randomChoice: object = None
    inside: RequestPostHealthDefaultInside = None
    insideList: List[RequestPostHealthDefaultInside] = None
    draftId: str = None
    uuid: str = None
    listUuid: list = None

class ResponsePostHealthDefault(BaseModel):
    status: str = Field(...)
    warnings: object = Field(...)

    @field_validator('status')
    @classmethod
    def force_x_positive_01(cls, v):
        assert v == 'alive'
        return v

    @field_validator('warnings')
    @classmethod
    def force_x_positive_02(cls, v):
        assert v == []
        return v


class PayloadPostHealthDefault:

    @staticmethod
    def payload_string_length_elements(element=None):
        dict_length_elements = {
            'url': 150,
            'text': 150
        }
        dict_copy = dict_length_elements.copy()
        if element:
            dict_copy[element] += 2
        return_dict = dict_copy
        return return_dict

    @staticmethod
    def request_generation_default(draft_id):
        payload = RequestPostHealthDefault(
            url=fake.domain_word() + fake.msisdn()[5:],
            bool=fake.pybool(),
            text=fake.text(max_nb_chars=10),
            dateStart=start_date.strftime("%Y-%m-%dT%H:%M:00+03:00"),
            dateEnd=end_date.strftime("%Y-%m-%dT%H:%M:00+03:00"),
            randomChoice=random.choice(['compact', 'full']),
            inside=RequestPostHealthDefaultInside(
                int=random.randint(1000, 9999)
            ),
            insideList=[RequestPostHealthDefaultInside(
                int=random.randint(1000, 9999)
            )],
            draftId=draft_id,
            uuid=fake.uuid4(),
            listUuid=[fake.uuid4(), fake.uuid4(), fake.uuid4()]
        )
        return_payload = payload.model_dump(mode='json')
        try:
            return return_payload
        except ValidationError as e:
            PydanticResponseError.print_error(e)

    @staticmethod
    def request_generation_custom(draft_id, type, element):
        if type == "ore":
            payload_ore = RequestPostHealthDefault(
                url=fake.domain_word() + fake.msisdn()[5:],
                bool=fake.pybool(),
                text=fake.text(max_nb_chars=10),
                draftId=draft_id
            )
            return_payload = payload_ore.model_dump(mode='json')
            try:
                return return_payload
            except ValidationError as e:
                PydanticResponseError.print_error(e)
        elif type == "mre":
            return_payload = PayloadPostHealthDefault.definition_missing_required_elements(draft_id, element)
            try:
                return return_payload
            except ValidationError as e:
                PydanticResponseError.print_error(e)
        elif type == "sle":
            length_elements = PayloadPostHealthDefault.payload_string_length_elements(element)
            length_url = length_elements.get('url')
            length_text = length_elements.get('text')
            payload = RequestPostHealthDefault(
                url=fake.pystr(min_chars=length_url, max_chars=length_url),
                bool=fake.pybool(),
                text=fake.pystr(min_chars=length_text, max_chars=length_text),
                draftId=draft_id
            )
            return_payload = payload.model_dump(mode='json')
            try:
                return return_payload
            except ValidationError as e:
                PydanticResponseError.print_error(e)

    @staticmethod
    def definition_missing_required_elements(draft_id=None, element=None):
        dict_required_elements = {
            'url': fake.domain_word() + fake.msisdn()[5:],
            'bool': fake.pybool(),
            'text': fake.text(max_nb_chars=10),
            'draftId': draft_id
        }
        dict_copy = dict_required_elements.copy()
        if element:
            dict_copy.pop(element)
        return_dict = dict_copy
        return return_dict

    @staticmethod
    def definition_payload(draft_id, payload, type=None, element=None):
        if payload == 'default':
            return PayloadPostHealthDefault.request_generation_default(draft_id)
        elif payload == 'custom':
            return PayloadPostHealthDefault.request_generation_custom(draft_id, type, element)


class ValidatePostHealthDefault:
    @staticmethod
    def response_default(data):
        try:
            return ResponsePostHealthDefault.model_validate(data)
        except ValidationError as e:
            PydanticResponseError.print_error(e)
