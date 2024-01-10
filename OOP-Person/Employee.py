from Person import Person

class Employee(Person):
    def __init__(self, name, lastname, id, phone, salary):
        super().__init__(name, lastname, id, phone)
        self.salary = salary

    def __str__(self) -> str:
        return super().__str__() + "\nSalary: " + str(self.salary)