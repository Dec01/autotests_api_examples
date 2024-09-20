import random
from typing import List, Dict
from faker import Faker

from pydantic import Field, ValidationError, BaseModel, field_validator
from src.models.processings.processing_validate import PydanticResponseError

fake = Faker(locale="ru_RU")


class RequestPostHealthNegativeFakeValueElement(BaseModel):
    age: str = Field(...)
    themes: List = Field(...)

class RequestPostHealthNegativeNoElement(BaseModel):
    age: str = Field(...)

class RequestPostHealthNegativeMoreElement(BaseModel):
    age: str = Field(...)
    themes: List = Field(...)
    test: str = Field(...)


class ResponsePostHealthNoElement(BaseModel):
    code: str = Field(...)
    error: list = Field(...)
    message: str = Field(...)

    @field_validator('message')
    @classmethod
    def force_x_positive_02(cls, v):
        assert v == 'Form is not valid'
        return v

class ResponsePostHealthMoreElementError(BaseModel):
    notExpectedFields: list = Field(...)

class ResponsePostHealthMoreElement(BaseModel):
    code: str = Field(...)
    error: ResponsePostHealthMoreElementError = Field(...)
    message: str = Field(...)

    @field_validator('message')
    @classmethod
    def force_x_positive_02(cls, v):
        assert v == 'Form is not valid'
        return v

class ResponsePostHealthFakeValueElementError(BaseModel):
    fields: Dict = Field(...)

class ResponsePostHealthFakeValueElement(BaseModel):
    code: str = Field(...)
    error: ResponsePostHealthFakeValueElementError = Field(...)
    message: str = Field(...)

    @field_validator('message')
    @classmethod
    def force_x_positive_02(cls, v):
        assert v == 'Form is not valid'
        return v



class PayloadPostHealth:

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
    def request_generation_custom(type, element=None):
        if type == "more_element":
            payload = RequestPostHealthNegativeMoreElement(
                age=random.choice(list(PayloadPostHealth.list_elements_values('ages'))),
                themes=[random.choice(list(PayloadPostHealth.list_elements_values('themes')))],
                test=fake.text(max_nb_chars=10)
            )
            return_payload = payload.model_dump(mode='json')
            try:
                return return_payload
            except ValidationError as e:
                PydanticResponseError.print_error(e)
        elif type == "no_element":
            payload = RequestPostHealthNegativeNoElement(
                age=random.choice(list(PayloadPostHealth.list_elements_values('ages')))
            )
            return_payload = payload.model_dump(mode='json')
            try:
                return return_payload
            except ValidationError as e:
                PydanticResponseError.print_error(e)
        elif type == "fake_value_element":
            if element == 'ages':
                ages = 'test'
                themes = random.choice(list(PayloadPostHealth.list_elements_values('themes')))
            else:
                ages = random.choice(list(PayloadPostHealth.list_elements_values('ages')))
                themes = 'test'
            payload = RequestPostHealthNegativeFakeValueElement(
                age=ages,
                themes=[themes],
            )
            return_payload = payload.model_dump(mode='json')
            try:
                return return_payload
            except ValidationError as e:
                PydanticResponseError.print_error(e)


    @staticmethod
    def definition_payload(payload, type=None, element=None):
        if payload == 'custom':
            return PayloadPostHealth.request_generation_custom(type, element)

class ValidatePostHealth:

    @staticmethod
    def response_error_no_element(data):
        try:
            return ResponsePostHealthNoElement.model_validate(data)
        except ValidationError as e:
            PydanticResponseError.print_error(e)

    @staticmethod
    def response_error_more_element(data):
        try:
            return ResponsePostHealthMoreElement.model_validate(data)
        except ValidationError as e:
            PydanticResponseError.print_error(e)

    @staticmethod
    def response_error_fake_value_element(data):
        try:
            return ResponsePostHealthFakeValueElement.model_validate(data)
        except ValidationError as e:
            PydanticResponseError.print_error(e)