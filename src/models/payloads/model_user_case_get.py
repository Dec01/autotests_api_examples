from faker import Faker

from pydantic import Field, ValidationError, BaseModel, field_validator
from src.models.processings.processing_validate import PydanticResponseError
from typing import List, Optional

fake = Faker(locale="ru_RU")

class ResponseGetUserCasePayloadStudent(BaseModel):
    age: str = Field(...)
    themes: List = Field(...)
    selectionCodes: Optional[List]

class ResponseGetUserCasePayload(BaseModel):
    cacheKey: str = Field(...)
    student: ResponseGetUserCasePayloadStudent = Field(...)
class ResponseGetUserCase(BaseModel):
    code: str = Field(...)
    payload: ResponseGetUserCasePayload = Field(...)
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


class ValidateGetUserCase:

    @staticmethod
    def response_default(data):
        try:
            return ResponseGetUserCase.model_validate(data)
        except ValidationError as e:
            PydanticResponseError.print_error(e)