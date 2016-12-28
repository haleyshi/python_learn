class Employee:
    'Base Class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee: %d" % Employee.empCount

    def displayEmployee(self):
        print "Name:", self.name, ", Salary:", self.salary

    def __del__(self):
        Employee.empCount -= 1
        print self.__class__.__name__, self.name, "destroyed!"



employee1 = Employee("Shi Guohuang", 35000)
employee2 = Employee("Haley Shi", 25000)

employee1.displayEmployee()
employee2.displayEmployee()

employee1.displayCount()

del employee2

employee1.displayCount()

if hasattr(employee1, 'age'):
    print employee1.age
else:
    employee1.age = 33

print getattr(employee1, 'age')

delattr(employee1, 'age')

setattr(employee1, 'sex', 'male')