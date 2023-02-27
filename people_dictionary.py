dictionary = {}


def add_data():
    name_add = input("name: ")
    age_add = int(input("age: "))
    address_add = input("address: ")
    new_person = {"age": age_add, "address": address_add}
    dictionary[name_add] = new_person


def name_search():
    name_input = input("enter name: ")
    for name, data in dictionary.items():
        if name_input in name:
            age = data["age"]
            address = data["address"]
            print(f"Name: {name}" + "\n" + f"Age: {age}" + "\n" + f"Address: {address}")


def age_search():
    age_input = int(input("enter age: "))
    for name, data in dictionary.items():
        if age_input in data["age"]:
            age = data["age"]
            address = data["address"]
            print(f"Name: {name}" + "\n" + f"Age: {age}" + "\n" + f"Address: {address}")


def address_search():
    address_input = input("enter address: ")
    for name, data in dictionary.items():
        if address_input in data["address"]:
            age = data["age"]
            address = data["address"]
            print(f"Name: {name}" + "\n" + f"Age: {age}" + "\n" + f"Address: {address}")


def change():
    change_input = input("change the data of: ")
    for name, value in dictionary.items():
        if change_input == name:
            print(dictionary[name])
            change_data = input("which data do you want to change: ")
            if "name" in change_data:
                name_change = input("change name to: ")
                dictionary[name_change] = dictionary.pop(change_input)
            if "age" in change_data:
                age_change = int(input("change age to: "))
                dictionary[change_input]["age"] = age_change
            if "address" in change_data:
                address_change = input("change address to: ")
                dictionary[change_input]["address"] = address_change


while True:
    command = input("enter command: ")
    if "list" in command:
        print(dictionary)
    if "add" in command:
        add_data()
    if "change" in command:
        change()
    if "search" in command:
        search_input = input("search for: ")
        if "name" in search_input:
            name_search()
        if "age" in search_input:
            age_search()
        if "address" in search_input:
            address_search()
