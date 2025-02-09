import json

class Contact:
    name: str
    age: int
    phone: str

    def __init__(self, name: str, age: int, phone: str) -> None:
        self.name = name
        self.age = age
        self.phone = phone

    def __str__(self) -> str:
        return f"{self.name}, {self.age}y, {self.phone}"

class Book:
    contacts: list[Contact]

    def __init__(self):
        self.contacts = []
        file = open('./contacts.json', 'r')
        content = file.read()
        file.close()
        saved_contacts = json.loads(content)
        for new_contact in saved_contacts:
            self.add(Contact(new_contact["name"], new_contact["age"], new_contact["phone"]))

    def add(self, contact: Contact) -> None:
        self.contacts.append(contact)

    def remove(self, phone: str) -> list[Contact]:
        removing_contacts = [contact for contact in self.contacts if contact.phone == phone]
        for contact in removing_contacts:
            self.contacts.remove(contact)
        return removing_contacts

    def save(self) -> None:
        contacts_dictionaries = [contact.__dict__ for contact in self.contacts]
        json_dumps = json.dumps(contacts_dictionaries)
        file = open('./contacts.json', 'w')
        file.write(json_dumps)
        file.close()

book = Book()
while True:
    method = input("Type 'add(a)', 'list(l)', 'remove(r)' or 'quit(q)': ")
    if method not in ["add", "a",  "list", "l",  "remove", "r",  "quit", "q"]:
        print("The only methods avaiable are 'add(a)', 'list(l)', 'remove(r)' or 'quit(q)'")
    else:
        if method == "add" or method == "a":
            print("--------------------")
            name = input("Name: ")
            age = int(input("Age: "))
            phone = input("Phone number: ")
            book.add(Contact(name, age, phone))
            book.save()
            print("Contact added successfully")
            print("--------------------")
        if method == "list" or method == "l":
            print("--------------------")
            contacts = [contact for contact in book.contacts]
            for contact in contacts:
                print(contact)
            print("--------------------")
        if method == "remove" or method == "r":
            print("--------------------")
            phone = input("Type the contact phone number: ")
            removed_contacts = book.remove(phone)
            book.save()
            print(f"The following contacts were removed: {", ".join([contact.name for contact in removed_contacts])}")
            print("--------------------")
        if method == "quit" or method == "q":
            break
