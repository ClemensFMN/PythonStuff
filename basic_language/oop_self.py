# https://www.geeksforgeeks.org/self-in-python-class/

class car():
    # init method or constructor
    def __init__(self, model, color):
        print("Address of self = ",id(self))
        self.model = model
        self.color = color
         
    def show(self):
        print("Model is", self.model )
        print("color is", self.color )
         
# both objects have different self which
# contain their attributes
audi = car("audi a4", "blue")
print("Address of audi = ",id(audi))

ferrari = car("ferrari 488", "green")
print("Address of ferrari = ",id(audi))

audi.show()     # same output as car.show(audi)
ferrari.show()  # same output as car.show(ferrari)
