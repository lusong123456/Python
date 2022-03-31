import time
import threading
import queue

q = queue.Queue(10)

def productor(i):
    while True:
        q.put("初始 %s 做的包子" %(i))
        time.sleep(2)

def consumer(j):
    while True:
        print("顾客 %s 吃了以额 %s" %(j, q.get()))
        time.sleep(1)

for i in range(20):
    t = threading.Thread(target=productor, args=(i,))
    t.start()

for j in range(10):
    v = threading.Thread(target=consumer, args=(j,))
    v.start()