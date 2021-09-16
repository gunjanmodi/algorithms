from threading import Thread, Condition, current_thread
import time


class AsyncExecutor():
    def work(self, callback):
        time.sleep(5)
        callback()

    def execute(self, say_hi):
        Thread(target=self.work, args=(say_hi,)).start()


class SyncExecutor(AsyncExecutor):

    def __init__(self):
        self.condition = Condition()
        self.is_done = False

    def work(self, callback):
        super().work(callback)
        print(f"Notifying to thread {current_thread().getName()}")
        self.condition.acquire()
        self.condition.notifyAll()
        self.is_done = True
        self.condition.release()

    def execute(self, say_hi):
        super().execute(say_hi)
        self.condition.acquire()
        while not self.is_done:
            self.condition.wait()
        print(f"Woken up the main thread {current_thread().getName()}")
        self.condition.release()


def say_hi():
    print("Hi")


if __name__ == '__main__':
    # executor = AsyncExecutor()
    executor = SyncExecutor()
    executor.execute(say_hi)
    print("Main thread exiting")
