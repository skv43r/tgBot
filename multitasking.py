import threading
import logging
import time


logging.basicConfig(level=logging.INFO)


class MyThread(threading.Thread):

    def __init__(self, name):

        threading.Thread.__init__(self)
        self.name = name

    def run(self) -> None:
        time.sleep(3)
        logging.info(f"Thread {self.name} finished")

myTherad = MyThread(1)
myTherad.start()
myTherad.join()
logging.info("MAIN has completed")