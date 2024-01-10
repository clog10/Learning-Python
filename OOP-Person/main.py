from Employee import Employee
from Client import Client

people = []

def charge():
    answer = input("Do you want add a employee? ")
    name = input("Enter a name ")
    lastname = input("Enter a Lastname ")
    id = input("Enter an id ")
    phone = input("Enter a phone number ")

    if(answer == 'yes'):
        salary = int(input("Enter a salary"))
        emp = Employee(name, lastname, id, phone, salary)
        people.append(emp)
    else:
        category = input("Enter a category")
        cli = Client(name, lastname, id, phone, category)
        people.append(cli)

charge()

for person in people:
    print(person)

