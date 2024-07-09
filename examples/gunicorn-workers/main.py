from flask import Flask
import os
import time

from ipcx import init_master

class PageCounter:
    
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

app = Flask(__name__)
page_counter = init_master(PageCounter(), 0)

@app.route('/')
def index():
    start = time.time()
    count = page_counter.increment()
    return f"{count} in {round((time.time() - start) * 1000, 3)}ms ({os.getpid()} / {page_counter.__class__ == PageCounter})"

if __name__ == "__main__":
    # gunicorn -w 4 main:app
    app.run()