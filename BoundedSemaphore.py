"""
Created on Mon Feb 13 20:01:56 2023
@author: prpa
"""

from multiprocessing import Process
from multiprocessing import current_process
from multiprocessing import Value, Array
from multiprocessing import BoundedSemaphore
import time
import random 

N = 8

def task(common, tid, semaphore):
    for i in range(10):
        print(f'{tid}−{i}: Non−critical Section', flush=True)
        time.sleep(random.random())
        print(f'{tid}−{i}: End of non−critical Section', flush=True)
        semaphore.acquire()
        print(f'{tid}−{i}: Critical section', flush=True)
        v = common.value + 1
        time.sleep(random.random())
        print(f'{tid}−{i}: Inside critical section', flush=True)
        common.value = v
        print(f'{tid}−{i}: End of critical section', flush=True)
        semaphore.release()

def main():
    lp = []
    common = Value('i', 0)
    semaphore = BoundedSemaphore()
    
    for tid in range(N):
        lp.append(Process(target=task, args=(common, tid, semaphore)))
    print (f"Valor inicial del contador {common.value}", flush=True)
    for p in lp:
        p.start()

    for p in lp:
        p.join()

    print (f"Valor final del contador {common.value}", flush=True)
    print ("fin", flush=True)

if __name__ == "__main__":
    main()