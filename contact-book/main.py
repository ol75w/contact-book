
import json

mycontacts = {}
FILE_NAME = "contacts.json"


def load_contacts():
    global mycontacts

    try:
        with open(FILE_NAME, "r") as file:
            mycontacts = json.load(file)

        print("Contacts loaded successfully!")

    except FileNotFoundError:
        mycontacts = {}

    except json.JSONDecodeError:
        print("Warning: contacts.json is corrupted. Starting with an empty contact book.")
        mycontacts = {}


def save_contacts():
    with open(FILE_NAME, "w") as file:
        json.dump(mycontacts, file, indent=4)


def addcontact():
    while True:
        name = input("Enter contact name: ").strip()

        if name:
            break
        print("Name cannot be empty!")

    if name in mycontacts:
        print("Contact already exists!")
        update = input("Update the phone number? (y/n): ").strip().lower()

        if update == "y":
            while True:
                phone = input("Enter contact number: ").strip()

                if phone:
                    break
                print("Phone number cannot be empty!")

            mycontacts[name] = phone
            save_contacts()
            print("Contact updated successfully!")

        elif update == "n":
            print("Existing contact unchanged!")

        else:
            print("Invalid choice! Contact unchanged.")

    else:
        while True:
            phone = input("Enter contact number: ").strip()

            if phone:
                break
            print("Phone number cannot be empty!")

        mycontacts[name] = phone
        save_contacts()
        print(f"{name} has been saved!")


def viewcontact():
    if not mycontacts:
        print("No contacts found!")
        return

    print("\n--- All Contacts ---")

    for name, phone in mycontacts.items():
        print(f"Contact name: {name}")
        print(f"Contact phone number: {phone}")
        print("--------------------")


def searchcontact():
    name = input("Enter the contact name: ").strip()

    if name in mycontacts:
        print(f"Contact phone number: {mycontacts[name]}")
    else:
        print("Contact not found!")


def updatecontact():
    name = input("Enter the contact name you want to update: ").strip()

    if name in mycontacts:
        while True:
            phone = input("Enter the updated number: ").strip()

            if phone:
                break
            print("Phone number cannot be empty!")

        mycontacts[name] = phone
        save_contacts()
        print("Contact updated successfully!")

    else:
        print("Contact not found!")


def deletecontact():
    name = input("Enter the contact name you want to delete: ").strip()

    if name in mycontacts:
        del mycontacts[name]
        save_contacts()
        print(f"{name} deleted successfully!")
    else:
        print("Contact not found!")


load_contacts()

while True:
    print("\n===== Contact Book =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Choose an option (1-6): ").strip()

    if choice == "1":
        addcontact()
    elif choice == "2":
        viewcontact()
    elif choice == "3":
        searchcontact()
    elif choice == "4":
        updatecontact()
    elif choice == "5":
        deletecontact()
    elif choice == "6":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")