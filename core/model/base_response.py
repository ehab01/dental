
import json


class BaseResponse():

    def create_success_response(self, result):
        ret = {
            'valid': True,
            'result': result,
            'error': None
        }
        return ret

    def create_failure_response(self, error_message):
        ret = {
            'valid': False,
            'result': None,
            'error': {
                'message' : error_message
            }
        }
        return ret
