from heapq import heappop, heappush
from threading import Thread, Condition
import math
import time


class DeferredCallbackExecuter():
    def __init__(self):
        self.actions = list()
        self.cond = Condition()
        self.sleep = 0

    def add_action(self, action):
        action.execute_at = time.time() + action.exec_secs_after

        self.cond.acquire()
        heappush(self.actions, action)
        self.cond.notify()
        self.cond.release()

    def start(self):
        while True:
            self.cond.acquire()

            while len(self.actions) == 0:
                self.cond.wait()

            while len(self.actions) is not 0:
                next_action = self.actions[0]
                sleep_for = next_action.execute_at - math.floor(time.time())
                if sleep_for <= 0:
                    break

                self.cond.wait(timeout=sleep_for)

                action_to_execute_now = heappop(self.actions)
                action_to_execute_now.action(*(action_to_execute_now, ))

                self.cond.release()


class DeferredAction(object):
    def __init__(self, exec_secs_after, name, action):
        self.exec_secs_after = exec_secs_after
        self.action = action
        self.name = name

    def __lt__(self, other):
        return self.execute_at < other.execute_at


def say_hi(action):
    print(
        f"hi, I am {action.name} executed at {math.floor(time.time())} and required at {math.floor(action.execute_at)}")


if __name__ == '__main__':
    action1 = DeferredAction(3, ("A",), say_hi)
    action2 = DeferredAction(2, ("B",), say_hi)
    action3 = DeferredAction(1, ("C",), say_hi)
    action4 = DeferredAction(7, ("D",), say_hi)

    executor = DeferredCallbackExecuter()
    t = Thread(target=executor.start, daemon=True)
    t.start()

    executor.add_action(action1)
    executor.add_action(action2)
    executor.add_action(action3)
    executor.add_action(action4)

    time.sleep(15)
