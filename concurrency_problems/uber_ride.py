from threading import Lock, Thread, current_thread, Semaphore, Barrier
import random
import time


class UberRideProblem(object):
    def __init__(self):
        self.democrats_count = 0
        self.democrats_waiting = Semaphore(0)
        self.republicans_count = 0
        self.republicans_waiting = Semaphore(0)
        self.lock = Lock()
        self.barrier = Barrier(4)
        self.ride_count = 0

    def drive(self):
        self.ride_count += 1
        print("Uber ride # {0} filled and on its way".format(self.ride_count))

    def seated(self, party):
        print(f"{party} {current_thread().getName()} seated")

    def seat_democrat(self):
        ride_leader = False
        self.lock.acquire()

        self.democrats_count += 1

        if self.democrats_count == 4:
            self.democrats_waiting.release()
            self.democrats_waiting.release()
            self.democrats_waiting.release()
            ride_leader = True
            self.democrats_count -= 4

        elif self.democrats_count == 2 and self.republicans_count >= 2:
            self.democrats_waiting.release()
            self.republicans_waiting.release()
            self.republicans_waiting.release()
            ride_leader = True
            self.democrats_count -= 2
            self.republicans_count -= 2

        else:
            self.lock.release()
            self.democrats_waiting.acquire()

        self.seated("Democrat")
        self.barrier.wait()

        if ride_leader:
            self.drive()
            self.lock.release()

    def seat_republican(self):
        ride_leader = False

        self.lock.acquire()

        self.republicans_count += 1

        if self.republicans_count == 4:
            self.republicans_waiting.release()
            self.republicans_waiting.release()
            self.republicans_waiting.release()
            ride_leader = True
            self.republicans_count -= 4

        elif self.republicans_count == 2 and self.democrats_count >= 2:
            self.republicans_waiting.release()
            self.democrats_waiting.release()
            self.democrats_waiting.release()
            ride_leader = True
            self.democrats_count -= 2
            self.republicans_count -= 2

        else:
            self.lock.release()
            self.republicans_waiting.acquire()

        self.seated("Republican")
        self.barrier.wait()

        if ride_leader:
            self.drive()
            self.lock.release()


def controlled_simulation():
    problem = UberRideProblem()

    dems = 10
    repubs = 10

    total = dems + repubs
    print(f"Total {dems} dems and {repubs} repubs\n")

    riders = list()

    while total != 0:
        toss = random.randint(0, 1)
        if toss == 1 and dems != 0:
            riders.append(Thread(target=problem.seat_democrat))
            dems -= 1
            total -= 1
        elif toss == 0 and repubs != 0:
            riders.append(Thread(target=problem.seat_republican))
            repubs -= 1
            total -= 1

    for rider in riders:
        rider.start()

    for rider in riders:
        rider.join()


if __name__ == '__main__':
    controlled_simulation()
