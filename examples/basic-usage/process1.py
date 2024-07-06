from ipcx import share, serv

import time

class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

@share()
def helloworld():
    print("helloworld executed !")
    return ("Hello World !", 1, {"a": "b"}, Person("Linus", 54))

serv(0)

while True:
    time.sleep(1)