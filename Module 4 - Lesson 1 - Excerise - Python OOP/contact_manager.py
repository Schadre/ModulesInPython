import re

contacts = [
    {
        "name": "John Doe",
        "phone": "1-789-456-0808",
        "email": "Doe@outlook.com"},
    {
        "name": "Jane Doe",
        "phone": "1-123-456-9119",
        "email": "JanieDoe@gmail.com"
    },

]

def add_contact(contacts, name, phone, email):
    contacts.append(
        {
            'name': name,
            'phone': phone,
            'email': email
        }
    )
    print(f"{name} has been added to your contacts!")

def view_contacts(contacts):
    for contact in contacts:
        print(f" \n Name: {contact['name']}, \n Phone: {contact['phone']},\n Email: {contact['email']}")

def search_contacts(contacts, name):
    for contact in contacts:
        x = re.search(name, contact['name'])
        if x:
            print(f"Found: {x.group(0)}")
        else: 
            continue

def delete_contacts(contacts, name):
    for contact in contacts:
        if contact['name'] == name:
            contacts.remove(contact)
    print(contacts)
        


    