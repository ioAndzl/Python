class Pizza(object):

    def __init__(self, size):
        self.size = size

    def get_size(self):
        return self.size
    
    @staticmethod
    def get_sum(x,y):
        return x+y
    
    @classmethod
    def from_string(cls, string):
        size = int(string)
        return cls(string)

if __name__ == "__main__":
    
    s = Pizza.get_sum(5,6)
    print(s)
    pizza = Pizza.from_string('15')
    print(pizza.get_size())