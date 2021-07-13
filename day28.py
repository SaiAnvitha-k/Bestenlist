# define a subclass using threading , instantiate the subclass and trigger the thread to print the current date
import threading
import datetime

class MyThread(threading.Thread):
    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        self.threadID = counter
        self.name = name
        self.counter = counter
    def run(self):
        print("Starting" + self.name)
        print_date(self.name, self.counter)

def print_date(threadName, counter):
    datafields = []
    today = datetime.date.today()
    datafields.append(today)
    print("{}[{}]: {}".format(threadName, counter, datafields[0]))

thread1 = MyThread("Thread", 1)
thread2 = MyThread("Thread", 2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
