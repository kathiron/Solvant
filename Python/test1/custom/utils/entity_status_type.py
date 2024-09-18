import enum

from custom.utils.common import Common

class EntityStatusType(enum.Enum):
    Deleted = 0
    Active = 1
    Suspended = 2
    Inactive = 3
    Recovered = 4
    Quarantined = 5

    def get_response_type(self, is_sentence_case:bool = True):
        return Common.split_camel_case(self.name, is_sentence_case) 