from threading import Thread, Condition, current_thread, Semaphore
import time


class UnisexBathroomProblem():
    def __init__(self, max_employee):
        self.in_use_by = None
        self.cond = Condition()
        self.emps_in_bathroom = 0
        self.max_emps_sem = Semaphore(3)

    def male_use_bathroom(self, name):
        with self.cond:
            while self.in_use_by == "female":
                print(f"{name} is waiting")
                self.cond.wait()
            self.max_emps_sem.acquire()
            self.emps_in_bathroom += 1
            self.in_use_by = "male"

        self.use_bathroom(name)
        self.max_emps_sem.release()

        with self.cond:
            self.emps_in_bathroom -= 1
            if self.emps_in_bathroom == 0:
                self.in_use_by = None
            self.cond.notifyAll()

    def female_use_bathroom(self, name):
        with self.cond:
            while self.in_use_by == "male":
                print(f"{name} is waiting")
                self.cond.wait()
            self.max_emps_sem.acquire()
            self.emps_in_bathroom += 1
            self.in_use_by = "female"

        self.use_bathroom(name)
        self.max_emps_sem.release()

        with self.cond:
            self.emps_in_bathroom -= 1
            if self.emps_in_bathroom == 0:
                self.in_use_by = None
            self.cond.notifyAll()

    def use_bathroom(self, name):
        print(
            f"{name} is using bathroom. {self.emps_in_bathroom} employees in the bathroom")
        time.sleep(3)
        print(f"{name} is done using the bathroom")


if __name__ == '__main__':
    problem = UnisexBathroomProblem(3)

    female1 = Thread(target=problem.female_use_bathroom, args=("Lisa", ))
    male1 = Thread(target=problem.male_use_bathroom, args=("Salman", ))
    male2 = Thread(target=problem.male_use_bathroom, args=("Shahrukh", ))
    male3 = Thread(target=problem.male_use_bathroom, args=("Akshay", ))

    female2 = Thread(target=problem.female_use_bathroom, args=("Kajol", ))
    male4 = Thread(target=problem.male_use_bathroom, args=("Ajay", ))
    male5 = Thread(target=problem.male_use_bathroom, args=("Varun", ))
    male5 = Thread(target=problem.male_use_bathroom, args=("Navaz", ))
    male6 = Thread(target=problem.male_use_bathroom, args=("Irfan", ))
    male7 = Thread(target=problem.male_use_bathroom, args=("Mogembo", ))
    male8 = Thread(target=problem.male_use_bathroom, args=("Pankaj", ))

    female1.start()
    male1.start()
    male2.start()
    male3.start()

    female2.start()
    male4.start()
    male5.start()
    male6.start()
    male7.start()
    male8.start()

    female1.join()
    male1.join()
    male2.join()
    male3.join()

    female2.join()
    male4.join()
    male5.join()
    male6.join()
    male7.join()
    male8.join()

    print("Employees in bathroom at the end {0}".format(
        problem.emps_in_bathroom))
