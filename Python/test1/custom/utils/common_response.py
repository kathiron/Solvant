from custom.utils.api_response_type import ApiResponseType
from custom.utils.common import Common

class CommonResponse:
    def __init__(self, data = None, message = '', success = False, tag = None):
        self.data = data
        if message == '':
            if success:
                message = 'Success'
            else:
                message = 'Failed'

        # if data is not None and (message == '' and success == False):
        #     message = 'Success'

        self.message = message
        self.time = Common.get_current_datetime_formatted()
        self.success = success
        self.successvalue = 200 if self.success else 404
        self.tag = tag
        self.records = Common.get_data_length(data)

    def reset_time(self):
        self.time = Common.get_current_datetime_formatted()

    def get_response(self, responsetype: ApiResponseType, data = None, message = '', tag = None):
        self.success = True if responsetype == ApiResponseType.Success else False
        self.successvalue = responsetype.value
        self.data = data
        self.message = Common.get_response_type(responsetype) + (' : ' + message if message != '' else '')
        self.reset_time()
        self.tag = tag
        self.records = Common.get_data_length(data)

        ## similar to switch case 
        # match responsetype:
        #     case ApiResponseType.Success:
        #         self.success = True

    def to_json(self):
        return {
            "data": self.data,
            "message": self.message,
            "time": self.time,
            "success": self.success,
            "tag": self.tag,
            "records": self.records
        }