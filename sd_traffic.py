
import threading
import time
import datetime
import queue
import random
from enum import Enum

lock = threading.RLock();

cd1 = threading.Condition()
cd2 = threading.Condition()

buffer = 0

Nq = queue.Queue()
Nl = threading.RLock()
Eq = queue.Queue()
El = threading.RLock()
Sq = queue.Queue()
Sl = threading.RLock()
Wq = queue.Queue()
Wl = threading.RLock()

Direction = Enum('Direction', ('N', 'E', 'S', 'W'))

queues = [Nq, Eq, Sq, Wq]
locks = [Nl, El, Sl, Wl]


def NS(cd1: threading.Condition, cd2: threading.Condition):
    with cd1:
        while (True):
            prev = datetime.datetime.now()
            while ((datetime.datetime.now() - prev).total_seconds() < 2):
                print("NS pass")
                time.sleep(1)
            try:
                cd2.notify()
            except:
                time.sleep(2)
                continue
            cd1.wait()


def EW(cd1: threading.Condition, cd2: threading.Condition):
    with cd2:
        while (True):
            print("waiting NS to wake me")
            cd2.wait()
            prev = datetime.datetime.now()
            while ((datetime.datetime.now() - prev).total_seconds() < 2):
                print("EW pass")
                time.sleep(1)
            try:
                cd1.notify()
            except:
                pass


cs1 = threading.Thread(name='cons', target=NS, args=(cd1, cd2,))

cs2 = threading.Thread(name='prod', target=EW, args=(cd1, cd2,))

cs2.start()
cs1.start()


def enterCriticalSection():
    carNum = 0

    while (carNum < 50):
        rand = random.randint(0, 3)
        q = queues[rand]
        l = locks[rand]
        l.acquire()
        q.put(carNum)
        l.release()
        carNum += 1
