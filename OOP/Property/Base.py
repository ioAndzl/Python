class Celsius:

    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature*1.8) + 32

class Celsius_private_attribute:

    def __init__(self, temperature = 0):
        self.__temperature = temperature

    def to_fahrenheit(self):
        return (self.__temperature*1.8) + 32


if __name__ == "__main__":
    cc = Celsius()
    ccp = Celsius_private_attribute()
    print(cc.temperature,cc.__dict__)
    #print(ccp.__temperature,ccp.__dict__)
    print(ccp.__dict__)
