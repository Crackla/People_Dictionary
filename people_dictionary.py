dictionary = {}


def add_data():
    name_add = input("name: ")
    age_add = int_input("age: ")
    address_add = input("address: ")
    new_person = {"name": name_add, "age": age_add, "address": address_add}
    numbers = len(dictionary.keys())
    dictionary[numbers] = new_person


def number_search():
    number_input = int_input("enter number: ")
    for number, data in dictionary.items():
        if number_input == number:
            name = data["name"]
            age = data["age"]
            address = data["address"]
            print(f"Nr.: {number}" + "\n" + f"Name: {name}" + "\n" + f"Age: {age}" + "\n" + f"Address: {address}")


def name_search():
    name_input = input("enter name: ")
    for number, data in dictionary.items():
        if name_input in data["name"]:
            name = data["name"]
            age = data["age"]
            address = data["address"]
            print(f"Nr.: {number}" + "\n" + f"Name: {name}" + "\n" + f"Age: {age}" + "\n" + f"Address: {address}")


def age_search():
    age_input = int_input("enter age: ")
    for number, data in dictionary.items():
        if age_input == data["age"]:
            name = data["name"]
            age = data["age"]
            address = data["address"]
            print(f"Nr.: {number}" + "\n" + f"Name: {name}" + "\n" + f"Age: {age}" + "\n" + f"Address: {address}")


def address_search():
    address_input = input("enter address: ")
    for number, data in dictionary.items():
        if address_input in data["address"]:
            name = data["name"]
            age = data["age"]
            address = data["address"]
            print(f"Nr.: {number}" + "\n" + f"Name: {name}" + "\n" + f"Age: {age}" + "\n" + f"Address: {address}")


def change():
    change_input = int_input("number of the person: ")
    for number, data in dictionary.items():
        if change_input == number:
            print(dictionary[number])
            change_data = input("which data do you want to change: ")
            if "name" in change_data:
                name_change = input("change name to: ")
                dictionary[change_input]["name"] = name_change
            if "age" in change_data:
                age_change = int_input("age: ")
                dictionary[change_input]["age"] = age_change
            if "address" in change_data:
                address_change = input("change address to: ")
                dictionary[change_input]["address"] = address_change


def int_input(text):
    while True:
        try:
            age = int(input(text))
            return age
        except ValueError:
            print("please enter a number")
            continue


while True:
    command = input("enter command: ")
    if "list" in command:
        for number, data in dictionary.items():
            print(number, data)
    if "add" in command:
        add_data()
    if "change" in command:
        change()
    if "search" in command:
        search_input = input("search for: ")
        if "number" in search_input:
            number_search()
        if "name" in search_input:
            name_search()
        if "age" in search_input:
            age_search()
        if "address" in search_input:
            address_search()
