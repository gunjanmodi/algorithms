import datetime
import http.client
import json

import urllib3


class Vaccination:
    def __init__(self):
        self.FIND_BY_PINCODE = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin'

    def perform(self, pincode):
        result = {}
        today = datetime.datetime.today().strftime('%d-%m-%Y')
        availables_centers = self._fetch_centers(**{'pincode': pincode, 'date': today})
        for center in availables_centers:
            if self._is_available_and_free(center):
                result['name'] = center['name']
                result['execution_date'] = today
                result['district_name'] = center['district_name']
                result['time'] = f"{center['from']} - {center['to']}"
                result['address'] = center['address']
                result['pincode'] = center['pincode']
                print(f"******** {center['name']}, {center['district_name']} ********")
        return result

    def _is_available_and_free(self, center):
        if center.get('fee_type') == 'Paid':
            return False
        for session in center.get('sessions'):
            if session.get('available_capacity') > 0:
                return True
        return False

    def _explore_slots(self, slots):
        for slot in slots:
            available_capacity = slot.get('available_capacity')
            if available_capacity > 0:
                print("CAPACITY: ", available_capacity)
                print()

    def _fetch_centers(self, **data):
        result = []
        http = urllib3.PoolManager()
        response = http.request('GET', self.FIND_BY_PINCODE, fields=data)
        response = json.loads(response.data)
        if response and response.get('centers'):
            result = response.get('centers')
        return result


class DispatchUpdate:
    def __init__(self, message_raw):
        TELEGRAM_API_HOST = "api.telegram.org"
        self.message_raw = message_raw
        self.telegram_connection = http.client.HTTPSConnection(TELEGRAM_API_HOST)
        # self.telegram_token = os.getenv('TELEGRAM_TOKEN', '1866785029:AAFazeWKSos8CB6HFmNZW1qk2ff8MtYS5gY')
        self.telegram_token = '1866785029:AAFazeWKSos8CB6HFmNZW1qk2ff8MtYS5gY'

    def dispatch_message(self):
        if self.telegram_token is not None:
            endpoint = f"/bot{self.telegram_token}/sendMessage"

            payload = {
                'chat_id': -1001565784339,
                'text': self.message_raw,
            }

            headers = {'content-type': "application/json"}

            self.telegram_connection.request("POST", endpoint, json.dumps(payload), headers)
            response = self.telegram_connection.getresponse()

            return {
                'statusCode': response.status,
                'body': json.dumps('Lambda executed.')
            }


def format_message(data):
    return f"Vaccine Slot Available at {data['name']}." \
           f"\nAddress:{data['address']}, {data['district_name']}\nPin Code - {data['pincode']}"


if __name__ == '__main__':
    vaccination = Vaccination()
    # data = vaccination.perform('382421')  # Gandhinagar
    data = vaccination.perform('380016')  # Ahmedabad
    if data:
        message = format_message(data)
        du = DispatchUpdate(message)
        du.dispatch_message()
