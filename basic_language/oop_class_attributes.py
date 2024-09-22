# using a class attribute to track data across all instances of a class
# in this case, we track all existing Person instances in a class attribute

class Person:
    # no self & defined outside constructor -> a class attribute
    person_list = []

    def __init__(self, name):
        self.name = name
        self.person_list.append(self) # usage via self may be a bit strange

    def getName():
        return(self.name)

p1 = Person("Clemens")
p2 = Person("Susi")

persons = [pl.name for pl in Person.person_list]
print(persons)
