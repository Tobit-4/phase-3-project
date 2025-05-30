from helpers import (
    list_farmers, add_farmer, delete_farmer,
    list_fields, add_field, delete_field,
    list_crops, add_crop,
)
import sys

def main_menu():
    print("\n🌱 Welcome to the Farm Management CLI 🌱")
    print("1. Manage Farmers")
    print("2. Manage Fields")
    print("3. Manage Crops")
    print("4. Exit")

def farmer_menu():
    print("\n👩‍🌾 Farmer Management")
    print("1. View all farmers")
    print("2. Add a new farmer")
    print("3. Delete a farmer")
    print("4. Go back")

def field_menu():
    print("\n🌾 Field Management")
    print("1. View all fields")
    print("2. Add a new field")
    print("3. Delete a field")
    print("4. Go back")

def crop_menu():
    print("\n🌽 Crop Management")
    print("1. View all crops")
    print("2. Add a new crop")
    print("3. Go back")

def run():
    while True:
        main_menu()
        choice = input("Select an option: ").strip()

        if choice == "1":
            while True:
                farmer_menu()
                sub = input("Choose: ").strip()
                if sub == "1":
                    list_farmers()
                elif sub == "2":
                    add_farmer()
                elif sub == "3":
                    delete_farmer()
                elif sub == "4":
                    break
                else:
                    print("Invalid choice. Try again.")

        elif choice == "2":
            while True:
                field_menu()
                sub = input("Choose: ").strip()
                if sub == "1":
                    list_fields()
                elif sub == "2":
                    add_field()
                elif sub == "3":
                    delete_field()
                elif sub == "4":
                    break
                else:
                    print("Invalid choice. Try again.")

        elif choice == "3":
            while True:
                crop_menu()
                sub = input("Choose: ").strip()
                if sub == "1":
                    list_crops()
                elif sub == "2":
                    add_crop()
                elif sub == "3":
                    break
                else:
                    print("Invalid choice. Try again.")

        elif choice == "4":
            print("👋 Exiting the farm manager. Goodbye!")
            sys.exit()

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    run()
