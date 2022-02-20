'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=153&date=13-08-2021'
import datetime
import json
import time

import urllib3


class Vaccination:
    def __init__(self):
        self.FIND_BY_DISTRICT_URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict'
        self.centers = [646539, 694283, 692635, 655737,
                        655740, 655741, 655745, 655747, 696074, 630210, 694270, 692628,
                        646551, 694280, 777475, 630485, 636626, 692732, 565651, 636642, 646553,
                        376460, 376472, 735455, 694282, 694268, 694267, 466633, 694265, 577153, 637851,
                        601279, 491316, 376465, 709710, 743552, 692741, 582329, 377464, 694266, 607110, 655735, 728044,
                        554944, 595462, 659934, 491453, 554936, 729185,
                        692753, 693166, 703413, 722301, 716574, 694276, 377485, 583759, 589891, 816648, 820822, 588230,
                        660958, 660961, 660966, 660970, 660975, 649562, 599422, 377571, 466176, 377559, 466651, 630384,
                        630450, 587891, 517703, 743535]


    # def _fetch_near_by_centers(self):


    def perform(self, district, preferred_vaccine='COVISHIELD', min_age=18):
        user_filter = {'min_age': min_age, 'district_id': district, 'preferred_vaccine': preferred_vaccine}
        date_range = self._next_date_range(7)

        for date in date_range:
            availables_slots = self._fetch_slots(**{'district_id': district, 'date': date})
            print("******** ", date, "********")
            self._explore_slots(availables_slots,user_filter)
            time.sleep(1)

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



    def _fetch_slots(self, **data):
        result = []
        http = urllib3.PoolManager()
        response = http.request('GET', self.FIND_BY_DISTRICT_URL, fields=data)
        response = json.loads(response.data)
        if response and response.get('sessions'):
            result = response.get('sessions')
        return result

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
    vaccination.perform('153') # Gandhinagar
    # vaccination.perform('770') # Ahmedabad
