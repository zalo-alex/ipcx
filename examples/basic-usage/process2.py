from ipcx import connect

ipc = connect(0)

class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

value = ipc.helloworld()
print(value)
print(value[3].name, value[3].age)