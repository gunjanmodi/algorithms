from threading import Condition, Thread, current_thread
import time
import random


class ReadWriteLock():
    def __init__(self):
        self.cond = Condition()
        self.writing_in_progress = False
        self.read_count = 0

    def acquire_read_lock(self):
        self.cond.acquire()
        if self.writing_in_progress:
            self.cond.wait()
        self.read_count += 1
        self.cond.release()

    def release_read_lock(self):
        self.cond.acquire()

        self.read_count -= 1

        if self.read_count == 0:
            self.cond.notifyAll()
        self.cond.release()

    def acquire_write_lock(self):
        self.cond.acquire()
        if self.read_count != 0 or self.writing_in_progress:
            self.cond.wait()
        self.writing_in_progress = True
        self.cond.release()

    def release_write_locK(self):
        self.cond.acquire()
        self.writing_in_progress = False
        self.cond.notifyAll()
        self.cond.release()


def writer_task(lock):
    while True:
        lock.acquire_write_lock()
        print("\n{0} writing at {1} and current readers = {2}".format(current_thread().getName(), time.time(),
                                                                      lock.read_count), flush=True)
        write_for = random.randint(1, 3)
        time.sleep(write_for)

        print("\n{0} releasing at {1} and current readers = {2}".format(current_thread().getName(), time.time(),
                                                                        lock.read_count))
        lock.release_write_locK()
        time.sleep(1)


def reader_task(lock):
    while True:
        lock.acquire_read_lock()
        print("\n{0} reading at {1} and write in progress = {2}".format(current_thread().getName(), time.time(),
                                                                        lock.writing_in_progress), flush=True)
        read_for = random.randint(1, 2)
        time.sleep(read_for)
        print("\n{0} releasing at {1} and write in progress = {2}".format(current_thread().getName(), time.time(),
                                                                          lock.writing_in_progress), flush=True)
        lock.release_read_lock()
        time.sleep(1)


if __name__ == '__main__':
    rw_lock = ReadWriteLock()

    writer_thread = Thread(target=writer_task, args=(rw_lock,), daemon=True)

    readers = list()
    for i in range(0, 3):
        readers.append(Thread(target=reader_task,
                              name=f"reader-{i+1}",
                              args=(rw_lock,), daemon=True))

    for reader_thread in readers:
        reader_thread.start()

    writer_thread.start()

    time.sleep(15)
