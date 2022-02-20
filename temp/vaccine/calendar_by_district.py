import datetime
import http.client
import json

import urllib3


class Vaccination:
    def __init__(self):
        self.CALENDAR_BY_DIST_URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict'

    def perform(self, district, preferred_vaccine='COVISHIELD', min_age=18):
        result = []
        today = datetime.datetime.today().strftime('%d-%m-%Y')
        availables_centers = self._fetch_centers(**{'district_id': district, 'date': today})
        for center in availables_centers:
            slot = dict()
            if self._is_available_free_and_covishield(center):
                print(f"******** {center['name']}, {center['district_name']} ********")
                slot['name'] = center['name']
                slot['execution_date'] = today
                slot['district_name'] = center['district_name']
                slot['time'] = f"{center['from']} - {center['to']}"
                slot['address'] = center['address']
                slot['pincode'] = center['pincode']
                result.append(slot)
        return result

    def _is_available_free_and_covishield(self, center):
        if center.get('fee_type') == 'Paid':
            return False
        for session in center.get('sessions'):
            if session.get('vaccine') == 'COVAXIN':
                continue
            if session.get('available_capacity') > 0:
                return True
        return False

    def _fetch_centers(self, **data):
        result = []
        http = urllib3.PoolManager()
        response = http.request('GET', self.CALENDAR_BY_DIST_URL, fields=data)
        response = json.loads(response.data)
        if response and response.get('centers'):
            result = response.get('centers')
        return result


def format_message(data):
    return f"Vaccine Slot Available at {data['name']}." \
           f"\nAddress:{data['address']}, {data['district_name']}\nPin Code - {data['pincode']}"


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


if __name__ == '__main__':
    vaccination = Vaccination()
    # vaccination.perform('153') # Gandhinagar
    centers = vaccination.perform('772')  # Gandhinagar Urban
    # vaccination.perform('770') # Ahmedabad
    if centers:
        for center_data in centers:
            message = format_message(center_data)
            du = DispatchUpdate(message)
            du.dispatch_message()
