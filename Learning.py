# Classes Video 1


class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Donal', 'McGrath', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1.fullname())
print(Employee.fullname(emp_1))

# the above replaces all that is below

# print(emp_1)
# print(emp_2)
#
#
# emp_1.first = 'Donal'
# emp_1.last = 'McGrath'
# emp_1.email = 'Donal.McGrath@gmail.com'
# emp_1.pay = 50000
#
# emp_2.first = 'Test'
# emp_2.last = 'User'
# emp_2.email = 'Test.User@gmail.com'
# emp_2.pay = 60000
#
#
print(emp_1.email)
print(emp_2.email)


# Classes Video 2
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Donal', 'McGrath', 50000)
emp_2 = Employee('Test', 'User', 60000)
