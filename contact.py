class ContactMaster:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email):
        """Add a new contact."""
        if name in self.contacts:
            print(f"Contact with the name '{name}' already exists.")
        else:
            self.contacts[name] = {'Phone': phone, 'Email': email}
            print(f"Contact '{name}' added successfully.")

    def delete_contact(self, name):
        """Delete an existing contact."""
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")

    def search_contact(self, name):
        """Search for a contact by name."""
        if name in self.contacts:
            print(f"Contact found: {name} - Phone: {self.contacts[name]['Phone']}, Email: {self.contacts[name]['Email']}")
        else:
            print(f"Contact '{name}' not found.")

    def display_contacts(self):
        """Display all contacts."""
        if not self.contacts:
            print("No contacts available.")
        else:
            for name, details in self.contacts.items():
                print(f"Name: {name}, Phone: {details['Phone']}, Email: {details['Email']}")


def main():
    cm = ContactMaster()

    while True:
        print("\n--- Contact Master ---")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. Display All Contacts")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            cm.add_contact(name, phone, email)
        elif choice == '2':
            name = input("Enter the name of the contact to delete: ")
            cm.delete_contact(name)
        elif choice == '3':
            name = input("Enter the name of the contact to search: ")
            cm.search_contact(name)
        elif choice == '4':
            cm.display_contacts()
        elif choice == '5':
            print("Exiting Contact Master. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
