import random

from faker import Faker
from pydantic import Field, ValidationError, BaseModel, field_validator
from src.models.processings.processing_validate import PydanticResponseError

fake = Faker(locale="ru_RU")

class ResponseGetHealthParams(BaseModel):
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


class ParamsGetHealthParams:

    @staticmethod
    def request_filter(element=None):
        dict_params = {
            'material': random.choice(list(["true", "false"])),
            'video': random.choice(list(["true", "false"]))
        }
        if element:
            param = dict_params[element]
            return list([element, '=', param])
        else:
            return dict_params


    @staticmethod
    def request_sorts(select=None, field=None, value=None):
        sort_selection = ["asc", "desc"]

        if select == 'queue':
            return sort_selection

        elif value == 'asc':
            if field == 'Active':
                return ['field', '=', 'active', '&', 'direction', '=', 'asc']
            elif field == 'title':
                return ['field', '=', 'title', '&', 'direction', '=', 'asc']
        elif value == 'desc':
            if field == 'Active':
                return ['field', '=', 'active', '&', 'direction', '=', 'desc']
            elif field == 'title':
                return ['field', '=', 'title', '&', 'direction', '=', 'desc']
        else:
            return False

class ValidateGetHealthParams:
    @staticmethod
    def response_default(data):
        try:
            return ResponseGetHealthParams.model_validate(data)
        except ValidationError as e:
            PydanticResponseError.print_error(e)
