class Parent:
    parentAttr = 100

    def __init__(self):
        print "Constructor of Parent"

    def parentMethod(self):
        print "Method of Parent"

    def myMethod(self):
        print "myMethod of Parent"

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print "Parent Attr:", Parent.parentAttr

class Child(Parent):
    def __init__(self):
        print "Constructor of Child"

    def childMethod(self):
        print "Method of Child"

    def myMethod(self):
        print "myMethod of Child"


c = Child()
c.parentMethod()
c.childMethod()
c.myMethod()
c.setAttr(123)
c.getAttr()

print issubclass(Child, Parent)
print isinstance(c, Parent)
print isinstance(c, Child)