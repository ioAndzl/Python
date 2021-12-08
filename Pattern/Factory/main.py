from factory import Car, Bike

# creational pattern
class TransportFactory:
    @staticmethod
    def getTransport(type):
        if type == "car":
            return Car()
        if type == "bike":
            return Bike()
        assert 0, "Coudn't find transport "+ type

if __name__=="__main__":
    car = TransportFactory.getTransport("car")
    car.giveRide()