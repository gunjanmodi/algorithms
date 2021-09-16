from threading import Condition
from threading import Thread
from threading import current_thread
import random
import time


class BlockingQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.curr_size = 0
        self.q = []
        self.cond = Condition()

    def enqueue(self, item):
        self.cond.acquire()
        if self.curr_size == self.max_size:
            self.cond.wait()

        self.q.append(item)
        self.curr_size += 1

        self.cond.notifyAll()
        self.cond.release()

    def dequeue(self):
        self.cond.acquire()
        if self.curr_size == 0:
            self.cond.wait()

        item = self.q.pop(0)
        self.curr_size -= 1

        self.cond.notifyAll()
        self.cond.release()


def consumer_thread(q):
    while True:
        item = q.dequeue()
        print(f"\n{current_thread().getName()} consumed item {item}", flush=True)
        time.sleep(random.randint(1, 3))


def producer_thread(q, val):
    item = val
    while True:
        q.enqueue(val)
        item += 1
        time.sleep(0.1)


if __name__ == "__main__":
    blocking_q = BlockingQueue(5)

    consumer_thread1 = Thread(target=consumer_thread,
                              name="consumer-1", args=(blocking_q,))
    consumer_thread2 = Thread(target=consumer_thread,
                              name="consumer-2", args=(blocking_q,))
    producer_thread1 = Thread(target=producer_thread,
                              name="producer-1", args=(blocking_q, 1))
    producer_thread2 = Thread(target=producer_thread,
                              name="producer-2", args=(blocking_q, 100))

    consumer_thread1.start()
    consumer_thread2.start()
    producer_thread1.start()
    producer_thread2.start()

    time.sleep(15)
    print("Main thread exiting")
