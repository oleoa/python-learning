class Contact:
    name: str
    phone: int

    def __init__(self, name: str, phone: int) -> None:
        self.name = name
        self.phone = phone

    def __str__(self) -> str:
        return f"Name: {self.name}, Phone: {self.phone}"

class Book:
    contacts: list[Contact]

    def __init__(self):
        self.contacts = []

    def add_contact(self, *contacts: Contact) -> None:
        for contact in contacts:
            self.contacts.append(contact)

    def remove_contacts(self, phone: int) -> list[Contact]:
        contacts = [contact for contact in self.contacts if contact.phone == phone]
        for contact in contacts:
            self.contacts.remove(contact)
        return contacts

    def view_contacts(self, phone: int) -> list[str]:
        contacts = [str(contact) for contact in self.contacts if contact.phone == phone]
        return contacts

book = Book()

while True:
    response = input().split(" ")
    method = response[0]
    arguments = "".join(response[1:])
    if method not in ["add", "list", "remove", "view"]:
        print("The only methods avaiable are 'add', 'list', 'remove' and 'view'")
    if method == "add":
        if not arguments:
            contact = input("Type the new contact's name and phone number separated by a ',': ")
        else:
            contact = arguments
        name = str(contact.split(",")[0])
        phone = int(contact.split(",")[1])
        book.add_contact(Contact(name, phone))
        print("Contact added successfully")
    if method == "list":
        contacts = [contact for contact in book.contacts]
        print("----------")
        for contact in contacts:
            print(contact)
        print("----------")
    if method == "remove":
        phone = int(input("Type the contact phone number: "))
        removed_contacts = book.remove_contacts(phone)
        print(f"The following contacts were removed: {", ".join([contact.name for contact in removed_contacts])}")
    if method == "view":
        phone = int(input("Type the contact phone number: "))
        contacts = book.view_contacts(phone)
        print(f"The following contacts has this phone number: [{"] and [".join([contact for contact in contacts])}]")
