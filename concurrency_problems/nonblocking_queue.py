from threading import Thread, Lock, current_thread
from concurrent.futures import Future
import time
import random


# class NonBlockingQueue:
#     def __init__(self, max_size):
#         self.max_size = max_size
#         self.q = []
#         self.lock = Lock()

#     def dequeue(self):
#         with self.lock:
#             curr_size = len(self.q)

#             if curr_size != 0:
#                 return self.q.pop(0)
#             else:
#                 return False

#     def endqueue(self, item):
#         with self.lock:
#             curr_size = len(self.q)

#             if curr_size == self.max_size:
#                 return False
#             else:
#                 self.q.append(item)
#                 return True


class NonBlockingQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.q = []
        self.lock = Lock()
        self.q_waiting_puts = []
        self.q_waiting_gets = []

    def dequeue(self):

        result = None
        future = None
        with self.lock:
            curr_size = len(self.q)

            if curr_size != 0:
                result = self.q.pop(0)
                # remember to resolve a pending future for
                # a put request
                if len(self.q_waiting_puts) != 0:
                    self.q_waiting_puts.pop(0).set_result(True)
            else:
                # queue is empty so create a future for a get
                # request
                future = Future()
                self.q_waiting_gets.append(future)
        return result, future

    def enqueue(self, item):
        future = None
        with self.lock:
            curr_size = len(self.q)

            if curr_size == self.max_size:
                # queue is full so create a future for a put
                # request
                future = Future()
                self.q_waiting_puts.append(future)
            else:
                self.q.append(item)
                if len(self.q_waiting_gets) != 0:
                    self.q_waiting_gets.pop(0).set_result(True)
        return future


def producer_thread(q):
    item = 1
    while True:
        future = q.enqueue(item)
        if future is not None:
            future.item = item
            future.q = q
            future.add_done_callback(retry_enqueue)
        else:
            item += 1


def retry_enqueue(future):
    item = future.ite


def consumer_thread(q):
    while True:
        item, future = q.dequeue()

        if item == False:
            print("Consumer could not dequeue an item")
        else:
            print(
                f"\n{current_thread().getName()} consumed the item {item}",
                flush=True
            )

        time.sleep(random.randint(1, 3))


if __name__ == '__main__':
    nonblocking_queue = NonBlockingQueue(5)

    producer_thread1 = Thread(target=producer_thread,
                              name="producer", args=(nonblocking_queue, ))

    consumer_thread1 = Thread(target=consumer_thread,
                              name="consumer", args=(nonblocking_queue, ))

    producer_thread1.start()
    consumer_thread1.start()

    time.sleep(15)
    print("Main thread is exiting")
