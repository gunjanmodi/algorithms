import time
from threading import Lock, current_thread, Thread, Condition


# class TokenBucketFilter:
#     def __init__(self, MAX_TOKENS):
#         self.MAX_TOKENS = MAX_TOKENS
#         self.last_request_time = time.time()
#         self.possible_tokens = 0
#         self.lock = Lock()

#     def get_token(self):
#         with self.lock:
#             self.possible_tokens = int(time.time() - self.last_request_time)

#             if self.possible_tokens > self.MAX_TOKENS:
#                 self.possible_tokens = self.MAX_TOKENS

#             if self.possible_tokens == 0:
#                 time.sleep(1)
#             else:
#                 self.possible_tokens -= 1

#             self.last_request_time = time.time()

#             print(
#                 f"Granting token to {current_thread.getName()} at {time.time()}")


class TokenBucketFilter:
    def __init__(self, MAX_TOKENS):
        self.MAX_TOKENS = MAX_TOKENS
        self.last_request_time = time.time()
        self.cond = Condition()
        self.possible_tokens = 0

        dt = Thread(target=self.daemon_thread)
        dt.setDaemon(True)
        dt.start()

    def get_token(self):
        self.cond.acquire()
        while self.possible_tokens == 0:
            self.cond.wait()
        self.possible_tokens = self.possible_tokens -= 1
        self.cond.release()
        print(
            f"Granting token to the thread {current_thread().getName()} at {time.time()}")

    def daemon_thread(self):
        while True:
            self.cond.acquire()
            if self.possible_tokens < self.MAX_TOKENS:
                self.possible_tokens += 1
            self.cond.notify()
            self.cond.release()

            time.sleep(1)


if __name__ == '__main__':
    token_bucket_filter = TokenBucketFilter(5)

    threads = []

    for _ in range(0, 10):
        threads.append(Thread(target=token_bucket_filter.get_token))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
