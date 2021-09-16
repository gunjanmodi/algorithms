import time
from threading import Condition, Thread


class Semaphore():
    def __init__(self, max_out):
        self.max_out = max_out
        self.given_out = 0
        self.cond = Condition()

    def acquire(self):
        self.cond.acquire()
        if self.max_out == self.given_out:
            print("waiting to acquire semaphore")
            self.cond.wait()

        self.given_out += 1
        self.cond.notifyAll()
        self.cond.release()

    def release(self):
        self.cond.acquire()
        if self.given_out == 0:
            print("waiting to release semaphore")
            self.cond.wait()

        self.given_out -= 1
        self.cond.notifyAll()
        self.cond.release()


def task1(sema):
    sema.acquire()
    sema.acquire()
    time.sleep(1)
    sema.acquire()


def task2(sema):
    time.sleep(2)
    sema.release()
    sema.release()
    sema.release()


if __name__ == '__main__':
    semaphore = Semaphore(2)
    thread1 = Thread(target=task1, args=(semaphore,))
    thread2 = Thread(target=task2, args=(semaphore,))

    thread1.start()
    time.sleep(1)
    thread2.start()

    thread1.join()
    thread2.join()
