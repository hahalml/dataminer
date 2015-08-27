__author__ = 'force'
# Imports
import time
from threading import Thread

# Dummy workers
def polo_worker():
    while True:
        time.sleep(3)
        print("polo is mining")

def kraken_worker():
    while True:
        time.sleep(1)
        print("kraken is mining")

def cryptsy_worker():
    while True:
        time.sleep(2)
        print("cryptsy is mining")

def bittrex_worker():
    while True:
        time.sleep(2)
        print("bittrex is mining")

# this is how to multithread
def multithreading():
    polo_thread = Thread(target=polo_worker)
    kraken_thread = Thread(target=kraken_worker)
    cryptsy_thread = Thread(target=cryptsy_worker)
    bittrex_thread = Thread(target=bittrex_worker)

    polo_thread.start()
    kraken_thread.start()
    cryptsy_thread.start()
    bittrex_thread.start()

# For windows compatibility we need if __name == "__main__":
if __name__ == "__main__":
    multithreading()






# print("time", time.perf_counter() - start)

