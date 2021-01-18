from abc import ABC, abstractmethod

class AbstractClassExample(ABC):

    def __init__(self, value):
        self.value = value
        super().__init__()

    @abstractmethod
    def do_something():
        pass


class DoAdd42(AbstractClassExample):

    def do_something(self):
        return self.value = 42

class DoMul42(AbstractClassExample):

    def do_something(self):
        return self.value * 42

class AbstractClassExample2(ABC):

    @abstractmethod
    def do_something(self):
        print("Some implementation")

class AnotherSubclass(AbstractClassExample2):

    def do_something(self):
        super().do_someting()
        print("The enrichment from AnotherSubclass")

    
if __name__ == "__main__":
    x = AnotherSubClass()
    pass

x = DoAdd42(10)
y = DoMul42(10)
print(x.do_something())
print(y.do_something())
    

    #def get_radius():
    #    raise NotImplementedError