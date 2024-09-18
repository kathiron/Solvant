import enum

from custom.utils.common import Common

class ApiResponseType(enum.Enum):
    Success = 200
    DataNotFound = 404
    BadRequest = 400
    UnAuthorized = 401
    InternalServerError = 500