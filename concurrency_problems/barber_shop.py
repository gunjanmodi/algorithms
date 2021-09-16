from threading import Semaphore, Thread, Event, Lock
import time
import random

CUSTOMER_INTERVAL_MIN = 5
CUSTOMER_INTERVAL_MAX = 15
HAIRCUT_DURATION_MIN = 3
HAIRCUT_DURATION_MAX = 15


class BarberShop():
    def __init__(self, barber, capacity):
        self.total_chairs = capacity
        self.waiting_customers = []
        self.barber = barber
        self.lock = Lock()

    def open_shop(self):
        print("Barber shop is opening")
        working_thread = Thread(target=self.barber_go_to_work)
        working_thread.start()

    def barber_go_to_work(self):
        while True:
            self.lock.acquire()
            if len(self.waiting_customers) > 0:
                customer = self.waiting_customers.pop(0)
                self.lock.release()
                self.barber.cut_hair(customer)
            else:
                self.lock.release()
                print("No customer.. going to sleep")
                barber.sleep()

    def enter_shop(self, customer):
        self.lock.acquire()
        print(f"{customer.name} entered the shop and is looking for a seat")

        if len(self.waiting_customers) == self.total_chairs:
            print(f"Waiting room is full, {customer.name} is leaving")
            self.lock.release()
        else:
            self.waiting_customers.append(customer)
            self.lock.release()
            self.barber.wake_up()


class Barber():
    def __init__(self):
        self.barber_working_event = Event()

    def sleep(self):
        self.barber_working_event.wait()

    def wake_up(self):
        self.barber_working_event.set()

    def cut_hair(self, customer):
        self.barber_working_event.clear()
        print(f"Barber is curring a hair of {customer.name}")
        random_int = random.randint(HAIRCUT_DURATION_MIN, HAIRCUT_DURATION_MAX)
        time.sleep(random_int)
        print(f"{customer.name} is done")


class Customer():
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    customers = []
    for i in range(0, 20):
        customers.append(Customer(i))

    barber = Barber()

    barber_shop = BarberShop(barber, 3)
    barber_shop.open_shop()

    while len(customers) > 0:
        customer = customers.pop()
        print(customer.name)
        barber_shop.enter_shop(customer)
        sleep_for = random.randint(
            CUSTOMER_INTERVAL_MIN, CUSTOMER_INTERVAL_MAX)
        time.sleep(sleep_for)
