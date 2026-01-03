contact_list  = []
contact_dic = {}

def add_contact(name, phone, email, address):
    contact_dic = {'name': name, 'phone': phone, 'email': email, 'address': address}
    contact_list.append(contact_dic)
    print(f"Contact {name} added successfully.")
def view_contacts():
    if contact_list == []:
        print("No contacts available.")
        return
    for idx, contact in enumerate(contact_list, start=1):
        print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
def update_contact(name, phone=None, email=None, address=None):
    for contact in contact_list:
        if contact['name'] == name:
            if phone:
                contact['phone'] = phone
            if email:
                contact['email'] = email
            if address:
                contact['address'] = address
            print(f"Contact {name} updated successfully.")
            return
    print("Contact not found.")
def search_contact(name):
    for contact in contact_list:
        if contact['name'] == name:
            if contact['phone'] or contact['email'] or contact['address']:
                print(f"Contact found: {contact}")
            return
    print("Contact not found.")
def delete_contact(name):
    if contact_list == []:
        print("No contacts available to delete.")
        return
    for contact in contact_list:
        if contact['name'] == name:
            contact_list.remove(contact)
            print(f"Contact {name} deleted successfully.")
            return
while True:
    print("\n===== CONTACT MANAGEMENT SYSTEM =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        add_contact(name, phone, email, address)

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        name = input("Enter name to search: ")
        search_contact(name)

    elif choice == "4":
        name = input("Enter name to update: ")
        print("Leave blank if you don't want to change a field")
        phone = input("Enter new phone: ")
        email = input("Enter new email: ")
        address = input("Enter new address: ")

        # pass None if user leaves input blank
        update_contact(
            name,
            phone if phone else None,
            email if email else None,
            address if address else None
        )

    elif choice == "5":
        name = input("Enter name to delete: ")
        delete_contact(name)

    elif choice == "6":
        print("Exiting Contact Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
