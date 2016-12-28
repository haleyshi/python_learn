class Vector:
    __privateCount = 0
    publicCount = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return "Vector(%d,%d)" % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

    def increaseCount(self):
        self.__privateCount += 1
        self.publicCount += 1
        print self.__privateCount


v1 = Vector(10, 20)
v2 = Vector(100, 200)

print v1 + v2

v1.increaseCount()

print v1.publicCount

#object._className__attrName
print v1._Vector__privateCount