from pydantic import Field, ValidationError, BaseModel, field_validator
from src.models.processings.processing_validate import PydanticResponseError


class ResponseGetHealthDefault(BaseModel):
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


class ValidateGetHealthDefault:

    @staticmethod
    def response_default(data):
        try:
            return ResponseGetHealthDefault.model_validate(data)
        except ValidationError as e:
            PydanticResponseError.print_error(e)
