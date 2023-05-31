import random
from config import config


def generate_otp():
    otp = ""
    for i in range(6):
        otp += str(random.randint(0, 9))
    return otp


def send_otp():
    try:
        import requests

        url = "https://control.msg91.com/api/v5/flow/"

        payload = {
            "template_id": "62cecf8cd6fc05200c4b66b2",
            "sender": "Ravi",
            "short_url": "1 (On) or 0 (Off)",
            "mobiles": "918460855681",
            "VAR1": "VALUE 1",
            "VAR2": "VALUE 2"
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authkey": "364987AwQwM1V761026ad3P1"
        }

        response = requests.post(url, json=payload, headers=headers)

        print(response.text)
        print("\n\n\n Stage 1 \n\n\n")
        # import requests

        # url = "https://api.msg91.com/api/v5/otp"
        # print("\n\n\n Stage 2 \n\n\n")

        # payload = {
        #     "authkey": "364987AwQwM1V761026ad3P1",
        #     "mobile": "+918460855681",  
        #     "otp": "1234",  
        #     "sender": "Ravi", 
        #     "message": "check message" 
        # }
        # print("\n\n\n Stage 1 \n\n\n")
        # headers = {
        #     "content-type": "application/json"
        # }

        # response = requests.post(url, json=payload, headers=headers)

        # print(f"\n\n\n response of otp {response.text}\n\n\n")
    except Exception as e:
        print(e,"error")
        
    # otp = generate_otp()
    # message = f'Your OTP is {otp}'
    # print(f"\n\n\n message otp {message} \n\n\n")
    # try:
    #     config.client.messages.create(
    #         to='+91'+mobile_number,
    #         from_='+918460855681',
    #         body=message)
    #     return {'success': True, 'message': 'OTP sent successfully'}
    # except Exception as e:
    #     print(f"\n\n\n Error  {e} \n\n\n")
    #     return {'success': False, 'message': 'Error sending OTP'}
    
    
    

