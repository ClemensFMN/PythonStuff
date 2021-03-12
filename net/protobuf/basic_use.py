import basic_pb2

person = basic_pb2.Person()
person.id = 1234
person.name = "Clemens"

phone = person.phones.add()
phone.number = "555-4321"
phone.type = basic_pb2.Person.HOME

print("person: {}".format(person))

out = person.SerializeToString()
print("person serialized: {}".format(out))

person2 = basic_pb2.Person()
print("Person 2: {}".format(person2))
person2.ParseFromString(out)
print("deserialized: {}".format(person2))

