from pydantic import Field, ValidationError, BaseModel, ConfigDict, field_validator
from src.models.utils.ascii import BColors
from src.models.processing_request.response_processing import PydanticResponseError


class HealthValidateSchema(BaseModel):
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


class HealthValidate:

    @staticmethod
    def response_health_check(data):
        try:
            return HealthValidateSchema.model_validate(data)
        except ValidationError as e:
            PydanticResponseError.print_error(e)
