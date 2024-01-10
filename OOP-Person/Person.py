class Person:
    def __init__(self, name, lastname, id, phone):
        self.name = name
        self.lastname = lastname
        self.id = id
        self.phone = phone

    def __str__(self) -> str:
        return "Name: " + self.name + " " + self.lastname + "\nID: " + self.id + "\nPhone: " + self.phone