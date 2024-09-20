import random
from typing import List, Optional
from faker import Faker

from pydantic import Field, ValidationError, BaseModel, field_validator
from src.models.processings.processing_validate import PydanticResponseError

fake = Faker(locale="ru_RU")

class RequestPostUserCase(BaseModel):
    age: str = None
    themes: List = None

class ResponsePostUserCasePayloadStudent(BaseModel):
    age: str = Field(...)
    themes: List = Field(...)
    selectionCodes: Optional[List]

class ResponsePostUserCasePayload(BaseModel):
    cacheKey: str = Field(...)
    student: ResponsePostUserCasePayloadStudent = Field(...)

class ResponsePostUserCase(BaseModel):
    code: str = Field(...)
    payload: ResponsePostUserCasePayload = Field(...)
    message: str = Field(...)

    @field_validator('code')
    @classmethod
    def force_x_positive_01(cls, v):
        assert v == "0"
        return v

    @field_validator('message')
    @classmethod
    def force_x_positive_02(cls, v):
        assert v == 'Success'
        return v


class CustomResponsePostUserCasePayloadStudent(BaseModel):
    age: str = Field(...)
    themes: List = Field(...)
    selectionCodes: Optional[List]

    @field_validator('age')
    @classmethod
    def force_x_positive_01(cls, v):
        assert v == test_age
        return v

    @field_validator('themes')
    @classmethod
    def force_x_positive_02(cls, v):
        assert v == test_theme
        return v

class CustomResponsePostUserCasePayload(BaseModel):
    cacheKey: str = Field(...)
    student: CustomResponsePostUserCasePayloadStudent = Field(...)

class CustomResponsePostUserCase(BaseModel):
    code: str = Field(...)
    payload: CustomResponsePostUserCasePayload = Field(...)
    message: str = Field(...)

    @field_validator('code')
    @classmethod
    def force_x_positive_01(cls, v):
        assert v == "0"
        return v

    @field_validator('message')
    @classmethod
    def force_x_positive_02(cls, v):
        assert v == 'Success'
        return v


class PayloadPostUserCase:

    @staticmethod
    def list_elements_values(element):
        ages = ['0-3 года', '3-6 лет', '6-10 лет', '10-14 лет', 'от 14+']
        themes = ['игры и развлечения', 'культура и искусство', 'кино', 'музыка', 'литература', 'архитектура',
                  'живопись', 'экология', 'научные эксперименты', 'школа', 'профориентация', 'ЕГЭ', 'ОГЭ',
                  'волонтерство', 'для всей семьи', 'здоровый образ жизни', 'финансы', 'личная безопасность']
        if element == 'ages':
            return ages
        elif element == 'themes':
            return themes
        else:
            return False

    @staticmethod
    def request_generation_default():
        payload = RequestPostUserCase(
            age=random.choice(list(PayloadPostUserCase.list_elements_values('ages'))),
            themes=[random.choice(list(PayloadPostUserCase.list_elements_values('themes')))]
        )
        return_payload = payload.model_dump(mode='json')
        try:
            return return_payload
        except ValidationError as e:
            PydanticResponseError.print_error(e)

    @staticmethod
    def request_generation_custom(type, age, theme, element=None):
        if type == "parametrize":
            payload = RequestPostUserCase(
                age=age,
                themes=[theme]
            )
            return_payload = payload.model_dump(mode='json')
            try:
                return return_payload
            except ValidationError as e:
                PydanticResponseError.print_error(e)
        elif type == "mre":
            return_payload = PayloadPostUserCase.definition_missing_required_elements(element)
            try:
                return return_payload
            except ValidationError as e:
                PydanticResponseError.print_error(e)
        elif type == "more_theme":
            payload = RequestPostUserCase(
                age=random.choice(list(PayloadPostUserCase.list_elements_values('ages'))),
                themes=[random.choice(list(PayloadPostUserCase.list_elements_values('themes'))),
                        random.choice(list(PayloadPostUserCase.list_elements_values('themes'))),
                        random.choice(list(PayloadPostUserCase.list_elements_values('themes')))]
            )
            return_payload = payload.model_dump(mode='json')
            try:
                return return_payload
            except ValidationError as e:
                PydanticResponseError.print_error(e)

    @staticmethod
    def definition_missing_required_elements(element=None):
        dict_required_elements = {
            'age': random.choice(list(PayloadPostUserCase.list_elements_values('age'))),
            'themes': random.choice(list(PayloadPostUserCase.list_elements_values('themes')))
        }
        dict_copy = dict_required_elements.copy()
        if element:
            dict_copy.pop(element)
        return_dict = dict_copy
        return return_dict

    @staticmethod
    def definition_payload(payload, type=None, age=None, themes=None, element=None):
        if payload == 'default':
            return PayloadPostUserCase.request_generation_default()
        elif payload == 'custom':
            return PayloadPostUserCase.request_generation_custom(type, age, themes, element)

class ValidatePostUserCase:
    @staticmethod
    def response_default(data):
        try:
            return ResponsePostUserCase.model_validate(data)
        except ValidationError as e:
            PydanticResponseError.print_error(e)

    @staticmethod
    def response_custom(data, age, theme):
        global test_age
        global test_theme

        test_age = age
        test_theme = theme

        try:
            return CustomResponsePostUserCase.model_validate(data)
        except ValidationError as e:
            PydanticResponseError.print_error(e)