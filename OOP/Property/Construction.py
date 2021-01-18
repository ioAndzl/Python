class Celsius0:

    def __init__(self, temperature=0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return self.get_temperature() * 1.8 + 32

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        if value < -273.15:   
            raise ValueError("Temperature is below -273,15")
        self._temperature = value

class Celsius1:

    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return self.temperature* 1.8 + 32

    def get_temperature(self):
        print('getting value')
        return self._temperature

    def set_temperature(self, value):
        print('setting value')
        if value < -273.15:   
            raise ValueError("Temperature is below -273,15")
        self._temperature = value

    #creating property object 
    temperature = property(get_temperature, set_temperature)

class Celsius2:

    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        
        return self.temperature* 1.8 + 32

    def get_temperature(self):
        print('getting value')
        return self._temperature

    def set_temperature(self, value):
        print('setting value')
        if value < -273.15:   
            raise ValueError("Temperature is below -273,15")
        self._temperature = value

    #creating property object 
    temperature = property(get_temperature, set_temperature)



if __name__ == "__main__":
    cc0 = Celsius0()
    print(cc0.__dict__)
    cc1 = Celsius1()
    print(cc1.__dict__)
    print(cc1._temperature)
    #print(cc1.set_temperature(10))