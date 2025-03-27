import contact_manager
def main():
    while True:
        try:
            print("\n Welcome to your Phonebook")
            print("\n 1. Add Contact \n 2. View Contacts \n 3. Delete Contact \n 4. Search Contact \n 5. Quit")
            option = input("Please select an option: ")
            if option == "1":
                name = input("Please enter the full name of the contact you would like to add: ").title()
                phone = input("Please enter the phone number of the contact you would like to add: ")
                email = input("Please enter the email of the contact you would like to add: ")
                contact_manager.add_contact(contact_manager.contacts, name, phone, email)
            elif option == "2":
                contact_manager.view_contacts(contact_manager.contacts)
            elif option == "3":
                name = input("Please enter the full name of the contact you would like to delete: ").title()
                contact_manager.delete_contacts(contact_manager.contacts, name)
            elif option == "4":
                name = input("Please enter the name of the contact you are searching for: ").title()
                contact_manager.search_contacts(contact_manager.contacts, name)
            elif option == "5":
                print("Have an amazing day! \n Goodbye")
                break
        except KeyError:
            print("Please try again.")

if __name__ == "__main__":
    main()
