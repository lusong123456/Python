import time
import threading

sumA = 0

time1 = time.time()
class MyThread(threading.Thread):
    def __init__(self, thread_name):
        super(MyThread, self).__init__(name=thread_name)

    def run(self):
        lock = threading.Lock()
        global sumA
        lock.acquire()
        while sumA < 100000000:
            sumA += 1
        lock.release()


for i in range(10):
    t = MyThread("threadName" + str(i))
    t.start()
print(sumA)
time2 = time.time()
print(time2-time1)

time3 = time.time()
a = 0
while a < 100000000:
    a += 1
time4 = time.time()
print(time4-time3)


