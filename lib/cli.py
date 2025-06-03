from lib.db.models import session, Farmer, Field, Crop
from sqlalchemy.exc import SQLAlchemyError
import re


def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def create_farmer():
    try:
        name = input("Enter farmer name: ")
        email = input("Enter farmer email: ")

        if not name or not email:
            print("❌ Name and email are required.")
            return

        if not is_valid_email(email):
            print("❌ Invalid email format. Please use something like 'example@domain.com'.")
            return

        farmer = Farmer(name=name, email=email)
        session.add(farmer)
        session.commit()
        print(f"✅ Farmer '{name}' created successfully.")
    except SQLAlchemyError as e:
        session.rollback()
        print("❌ Database error:", e)


def create_field():
    try:
        name = input("Enter field name: ")
        location = input("Enter field location: ")
        size_in_acres = int(input("Enter field size (in acres): "))
        farmer_id = int(input("Enter farmer ID: "))

        farmer = session.get(Farmer, farmer_id)
        if not farmer:
            print("❌ Farmer not found.")
            return

        field = Field(name=name, location=location, size_in_acres=size_in_acres, farmer=farmer)
        session.add(field)
        session.commit()
        print(f"✅ Field '{name}' created for farmer '{farmer.name}'.")
    except ValueError:
        print("❌ Size and Farmer ID must be numbers.")
    except SQLAlchemyError as e:
        session.rollback()
        print("❌ Database error:", e)

def create_crop():
    try:
        name = input("Enter crop name: ")
        crop_type = input("Enter crop type: ")
        quantity = int(input("Enter quantity: "))
        planting_season = input("Enter planting season: ")
        harvest_season = input("Enter harvest season: ")
        yield_per_acre = int(input("Enter yield per acre: "))
        field_id = int(input("Enter field ID: "))

        field = session.get(Field, field_id)
        if not field:
            print("❌ Field not found.")
            return

        crop = Crop(
            name=name,
            crop_type=crop_type,
            quantity=quantity,
            planting_season=planting_season,
            harvest_season=harvest_season,
            yield_per_acre=yield_per_acre,
            field=field
        )
        session.add(crop)
        session.commit()
        print(f"✅ Crop '{name}' added to field '{field.name}'.")
    except ValueError:
        print("❌ Quantity, yield, and field ID must be numbers.")
    except SQLAlchemyError as e:
        session.rollback()
        print("❌ Database error:", e)

def view_farmers():
    farmers = session.query(Farmer).all()
    if not farmers:
        print("ℹ️ No farmers found.")
        return
    for farmer in farmers:
        print(farmer)

def view_fields():
    fields = session.query(Field).all()
    if not fields:
        print("ℹ️ No fields found.")
        return
    for field in fields:
        print(field)

def view_crops():
    crops = session.query(Crop).all()
    if not crops:
        print("ℹ️ No crops found.")
        return
    for crop in crops:
        print(crop)

def main():
    while True:
        print("\n🌾 Farm Management CLI 🌾")
        print("1. Create Farmer")
        print("2. Create Field")
        print("3. Create Crop")
        print("4. View Farmers")
        print("5. View Fields")
        print("6. View Crops")
        print("7. Exit")

        try:
            choice = input("Select an option: ").strip()
            if choice == "1":
                create_farmer()
            elif choice == "2":
                create_field()
            elif choice == "3":
                create_crop()
            elif choice == "4":
                view_farmers()
            elif choice == "5":
                view_fields()
            elif choice == "6":
                view_crops()
            elif choice == "7":
                print("👋 Exiting the farm management CLI. Goodbye!")
                break
            else:
                print("❌ Invalid option. Please choose 1–7.")
        except KeyboardInterrupt:
            print("\n👋 Exiting CLI. Goodbye!")
            break

if __name__ == "__main__":
    main()
