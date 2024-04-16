
class Demo():
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"{self.name} is {self.age} years old"