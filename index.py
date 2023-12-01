class Person():
    def __init__(self):
        self.fname = 'Anton'
        self.lname ='Sorokey'
        self.age = 26

    def __repr__(self):
        return "<Person Class - fname: {0}, lname: {1}, age: {2}>".format(self.fname, self.lname, self.age)

    def __str__(self):
        return "{0} {1} is {2}".format(self.fname, self.lname, self.age)

    def __bytes__(self):
        val = "Person:{0}:{1}:{2}".format(self.fname, self.lname, self.age)
        return bytes(val.encode('utf-8'))

me = Person()

print(repr(me))
print(str(me))
print(bytes(me))
# print("{0}".format(me))
