from custom.utils.api_response_type import ApiResponseType
from custom.utils.common import Common
from custom.utils.common_response import CommonResponse
from flask import request

class ApiCommon:

    @staticmethod
    def to_data_format_response(data):
        data = data if isinstance(data, bool) else Common.to_data_format(data)
        cr = CommonResponse()
        
        # Return the serialized data as a JSON response
        if isinstance(data, bool):
            cr.get_response(ApiResponseType.Success if data == True else ApiResponseType.BadRequest, data)
        elif isinstance(data, str):
            cr.get_response(ApiResponseType.Success if str(data).lower().index('error') >= 0 else ApiResponseType.BadRequest, data)
        elif data is None or not data:
            cr.get_response(ApiResponseType.DataNotFound)
        else:
            cr.get_response(ApiResponseType.Success, data = data)
            
        print(cr.to_json())
        return cr.to_json(), cr.successvalue 
    
    @staticmethod
    def get_request_data():
        data = request.get_json()
        if not data:
            raise ValueError("No JSON data provided")
        return data