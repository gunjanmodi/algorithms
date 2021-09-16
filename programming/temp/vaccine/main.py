'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=153&date=13-08-2021'
import datetime
import json
import time

import urllib3


class Vaccination:
    def __init__(self):
        self.CALENDAR_BY_DIST_URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict'
        # ?district_id=772&date=14-08-2021'

    def perform(self, district, preferred_vaccine='COVISHIELD', min_age=18):
        result = {}
        user_filter = {'min_age': min_age, 'district_id': district, 'preferred_vaccine': preferred_vaccine}
        today = datetime.datetime.today().strftime('%d-%m-%Y')
        availables_centers = self._fetch_slots(**{'district_id': district, 'date': today})
        print("******** ", today, "********")
        for center in availables_centers:
            if self._is_available_and_free(center):
                result['name'] = center['name']
                result['execution_date'] = today
                result['district_name'] = center['district_name']
                result['time'] = f"{center['from']} - {center['to']}"
                result['address'] = center['address']
                result['pincode'] = center['pincode']
                print(f"******** {center['name']}, {center['district_name']} ********")
        # self._explore_slots(availables_centers,user_filter)
        time.sleep(1)

    def _is_available_and_free(self, center):
        if center.get('fee_type') == 'Paid':
            return False
        for session in center.get('sessions'):
            if session.get('vaccine') == 'COVAXIN':
                continue
            if session.get('available_capacity') > 0:
                return True
        return False

    def _fetch_slots(self, **data):
        result = []
        http = urllib3.PoolManager()
        response = http.request('GET', self.CALENDAR_BY_DIST_URL, fields=data)
        response = json.loads(response.data)
        if response and response.get('centers'):
            result = response.get('centers')
        return result

    def _explore_slots(self, slots, user_filter):
        for slot in slots:
            vaccine_name = slot.get('vaccine')
            min_age_limit = slot.get('min_age_limit')
            available_capacity = slot.get('available_capacity')
            fee = int(slot.get('fee'))
            if fee > 0:
                continue
            if vaccine_name == user_filter['preferred_vaccine'] and min_age_limit >= user_filter['min_age']\
                    and available_capacity > 0:
                print('-------------- ', slot['name'], '--------------')
                print("\tNAME: ", slot['name'])
                print("\tADDRESS: ", slot['address'])
                print("\tDistrict: ", slot['district_name'])
                print("\tTIME: ", f"{slot['from']} - {slot['to']}")
                print("\tCAPACITY: ", slot['available_capacity'])
                print("\tFEE: ", slot['fee'])
                print()





    @staticmethod
    def _next_date_range(next_days):
        result = []
        base = datetime.datetime.today()
        for x in range(0, next_days):
            day = base + datetime.timedelta(days=x)
            result.append(day.strftime('%d-%m-%Y'))
        return result


if __name__ == '__main__':
    vaccination = Vaccination()
    # vaccination.perform('153') # Gandhinagar
    vaccination.perform('772') # Gandhinagar
    # vaccination.perform('770') # Ahmedabad
