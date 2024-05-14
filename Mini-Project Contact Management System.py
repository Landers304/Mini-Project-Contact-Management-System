import re
import json
import os
import shutil

class ContactManagementSystem:
    def __init__(self):
        self.contacts = {}
        self.categories = {}

    def display_menu(self):
        print("Welcome to the Contact Management System!")
        print("Menu:")
        print("1. Add a new contact")
        print("2. Edit an existing contact")
        print("3. Delete a contact")
        print("4. Search for a contact")
        print("5. Display all contacts")
        print("6. Export contacts to a text file")
        print("7. Import contacts from a text file")
        print("8. Add a contact category")
        print("9. Search contacts by category")
        print("10. Sort contacts by name")
        print("11. Backup contacts")
        print("12. Restore contacts from backup")
        print("13. Quit")

    def add_contact(self):
        print("Adding a new contact:")
        identifier = input("Enter unique identifier (e.g., phone number or email address): ")
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email address: ")
        additional_info = input("Enter additional information: ")
        category = input("Enter category (press Enter to skip): ")
        if category:
            self.categories.setdefault(category, []).append(identifier)
        self.contacts[identifier] = {
            "name": name,
            "phone_number": phone_number,
            "email": email,
            "additional_info": additional_info,
            "category": category
        }
        print("Contact added successfully.")

    def edit_contact(self):
        print("Editing an existing contact:")
        identifier = input("Enter unique identifier of the contact to edit: ")
        if identifier in self.contacts:
            print("Current details:")
            print("Name:", self.contacts[identifier]["name"])
            print("Phone Number:", self.contacts[identifier]["phone_number"])
            print("Email:", self.contacts[identifier]["email"])
            print("Additional Info:", self.contacts[identifier]["additional_info"])
            print("Category:", self.contacts[identifier]["category"])
            self.contacts[identifier]["name"] = input("Enter new name: ")
            self.contacts[identifier]["phone_number"] = input("Enter new phone number: ")
            self.contacts[identifier]["email"] = input("Enter new email address: ")
            self.contacts[identifier]["additional_info"] = input("Enter new additional information: ")
            self.contacts[identifier]["category"] = input("Enter new category (press Enter to skip): ")
            if self.contacts[identifier]["category"]:
                self.categories.setdefault(self.contacts[identifier]["category"], []).append(identifier)
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    def delete_contact(self):
        print("Deleting a contact:")
        identifier = input("Enter unique identifier of the contact to delete: ")
        if identifier in self.contacts:
            if self.contacts[identifier]["category"]:
                self.categories[self.contacts[identifier]["category"]].remove(identifier)
            del self.contacts[identifier]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    def search_contact(self):
        print("Searching for a contact:")
        identifier = input("Enter unique identifier of the contact to search: ")
        if identifier in self.contacts:
            print("Contact details:")
            print("Name:", self.contacts[identifier]["name"])
            print("Phone Number:", self.contacts[identifier]["phone_number"])
            print("Email:", self.contacts[identifier]["email"])
            print("Additional Info:", self.contacts[identifier]["additional_info"])
            print("Category:", self.contacts[identifier]["category"])
        else:
            print("Contact not found.")

    def display_all_contacts(self):
        print("Displaying all contacts:")
        for identifier, details in self.contacts.items():
            print("Identifier:", identifier)
            print("Name:", details["name"])
            print("Phone Number:", details["phone_number"])
            print("Email:", details["email"])
            print("Additional Info:", details["additional_info"])
            print("Category:", details["category"])
            print()

    def export_to_text_file(self, filename):
        with open(filename, "w") as file:
            json.dump({"contacts": self.contacts, "categories": self.categories}, file)
        print("Contacts exported to", filename, "successfully.")

    def import_from_text_file(self, filename):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.contacts = data.get("contacts", {})
                self.categories = data.get("categories", {})
            print("Contacts imported from", filename, "successfully.")
        except FileNotFoundError:
            print("File not found.")

    def add_contact_category(self):
        category = input("Enter new category: ")
        self.categories[category] = []

    def search_contacts_by_category(self):
        category = input("Enter category to search: ")
        if category in self.categories:
            print("Contacts in category", category + ":")
            for identifier in self.categories[category]:
                print("Name:", self.contacts[identifier]["name"])
                print("Phone Number:", self.contacts[identifier]["phone_number"])
                print("Email:", self.contacts[identifier]["email"])
                print("Additional Info:", self.contacts[identifier]["additional_info"])
                print()
        else:
            print("Category not found.")

    def sort_contacts_by_name(self):
        sorted_contacts = sorted(self.contacts.values(), key=lambda x: x["name"])
        print("Contacts sorted by name:")
        for contact in sorted_contacts:
            print("Name:", contact["name"])
            print("Phone Number:", contact["phone_number"])
            print("Email:", contact["email"])
            print("Additional Info:", contact["additional_info"])
            print("Category:", contact["category"])
            print()

    def backup_contacts(self):
        backup_folder = "backup"
        os.makedirs(backup_folder, exist_ok=True)
        backup_filename = os.path.join(backup_folder, "contacts_backup.json")
        with open(backup_filename, "w") as file:
            json.dump({"contacts": self.contacts, "categories": self.categories}, file)
        print("Contacts backed up successfully to", backup_filename)

    def restore_contacts_from_backup(self):
        backup_folder = "backup"
        backup_filename = os.path.join(backup_folder, "contacts_backup.json")
        if os.path.exists(backup_filename):
            with open(backup_filename, "r") as file:
                data = json.load(file)
                self.contacts = data.get("contacts", {})
                self.categories = data.get("categories", {})
            print("Contacts restored successfully from backup.")
        else:
            print("Backup file not found.")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_contact()
            elif choice == "2":
                self.edit_contact()
            elif choice == "3":
                self.delete_contact()
            elif choice == "4":
                self.search_contact()
            elif choice == "5":
                self.display_all_contacts()
            elif choice == "6":
                filename = input("Enter filename to export contacts: ")
                self.export_to_text_file(filename)
            elif choice == "7":
                filename = input("Enter filename to import contacts from: ")
                self.import_from_text_file(filename)
            elif choice == "8":
                self.add_contact_category()
            elif choice == "9":
                self.search_contacts_by_category()
            elif choice == "10":
                self.sort_contacts_by_name()
            elif choice == "11":
                self.backup_contacts()
            elif choice == "12":
                self.restore_contacts_from_backup()
            elif choice == "13":
                print("Thank you for using the Contact Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    cms = ContactManagementSystem()
    cms.run()
