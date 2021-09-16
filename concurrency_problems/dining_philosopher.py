from threading import Thread, Semaphore
import random
import time


class DiningPhilosopherProblem:
    def __init__(self):
        self.forks = [None] * 5
        self.forks[0] = Semaphore(1)
        self.forks[1] = Semaphore(1)
        self.forks[2] = Semaphore(1)
        self.forks[3] = Semaphore(1)
        self.forks[4] = Semaphore(1)

        self.max_diners = Semaphore(4)

        self.exit = False

    def life_cycle_of_a_philosopher(self, id):
        while self.exit is False:
            self.contemplate()
            self.eat(id)

    def contemplate(self):
        sleep_for = random.randint(100, 500) / 1000
        time.sleep(sleep_for)

    def eat(self, id):
        self.max_diners.acquire()

        self.forks[id].acquire()
        self.forks[(id + 4) % 5].acquire()

        print(f"Philosopher {id} is eating")

        self.forks[id].release()
        self.forks[(id + 4) % 5].release()

        self.max_diners.release()


if __name__ == '__main__':
    problem = DiningPhilosopherProblem()

    philosophers = list()

    for i in range(0, 5):
        philosophers.append(
            Thread(target=problem.life_cycle_of_a_philosopher, args=(i,)))

    for philosopher in philosophers:
        philosopher.start()

    time.sleep(6)
    problem.exit = True

    for philosopher in philosophers:
        philosopher.join()
