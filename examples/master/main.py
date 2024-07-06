import importlib
from multiprocessing import Process

def start_process(i):
    print(f"Thread #{i}")
    importlib.import_module("process")

for i in range(2):
    p = Process(target=start_process, args=(i,))
    p.start()
