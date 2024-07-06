from ipcx import init_master

import time

class Master:

    def __init__(self) -> None:
        self.value = 0

    def increment(self):
        self.value += 1
        return self.value

master = init_master(Master(), 0)

while True:
    start = time.time()
    print(master.increment())
    print((time.time() - start) * 1000, "ms")
    time.sleep(1)