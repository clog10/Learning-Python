from Person import Person

class Client(Person):
    def __init__(self, name, lastname, id, phone, category):
        super().__init__(name, lastname, id, phone)
        self.category = category

    def __str__(self) -> str:
        return super().__str__() + "\nCategory: " + self.category