from urllib.parse import urlencode
from urllib.request import urlopen
from hashlib import sha256
from hmac import HMAC
from datetime import datetime
import json

class DarazRequest:

    def __init__(self, user_id, api_key) -> None:
        self.api_key = bytes(api_key.encode("utf-8"))
        self.BASE_URL = "https://api.sellercenter.daraz.pk"
        self.user_id = user_id

    def validate_api(self):
        action = "GetProducts"
        resp = self.call_api(action=action, custom_parameters={})
        check_resp = resp.read()
        
        if "ErrorMessage" in str(check_resp):
           return False
        else:
            return True


    def call_api(self, action='GetOrders', custom_parameters:dict={}):
        parameters = {
            'UserID': self.user_id,
            'Version': '1.0',
            'Action': action,
            'Format': 'json',
            'Timestamp': datetime.utcnow().replace(microsecond=0).isoformat()
        }

        parameters = {**parameters, **custom_parameters}


        concatenated = urlencode(sorted(parameters.items())).encode("utf-8")
        parameters['Signature'] = HMAC(self.api_key, concatenated, sha256).hexdigest()
        final_parameters = urlencode(sorted(parameters.items()))

        resp = urlopen(f"{self.BASE_URL}?{final_parameters}")

        return resp

    def json_to_python(self, resp):

        data = json.loads(resp.read())
        return data



if __name__ == "__main__":

    ins = DarazRequest(user_id='info@techdukaan.pk',api_key ='WDWsBGgZgdj-_MFaT7uuxiXhbsYATLW3mYbOE-O9bSW-gTx8W05V_2Q3')

    ins.validate_api()

    # action = "GetProducts"
    # data = ins.call_api(action=action, custom_parameters={})


    # with open(f"{action}.json", "w") as file:
    #     file.write(json.dumps(data))