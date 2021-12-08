class TransportInterface:
    
    def giveRide(self):
        pass
    
class Car(TransportInterface):

    def giveRide(self):
        print("Give ride by car")

class Bike(TransportInterface):
    
    def giveRide(self):
        print("Give ride by bike")