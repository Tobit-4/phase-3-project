from db.models import session, Farmer, Field, Crop

# List all farmers
def list_farmers():
    farmers = session.query(Farmer).all()
    if not farmers:
        print("No farmers found.")
        return
    print("\n👩‍🌾 Farmers:")
    for farmer in farmers:
        print(f"ID: {farmer.id} | Name: {farmer.name}")

# Add a new farmer
def add_farmer():
    try:
        name = input("Enter farmer name: ").strip()
        if not name:
            print("❌ Name cannot be empty.")
            return
        farmer = Farmer(name=name)
        session.add(farmer)
        session.commit()
        print(f"✅ Farmer '{name}' added.")
    except Exception as e:
        print(f"Error: {e}")
        session.rollback()

# Delete a farmer
def delete_farmer():
    try:
        list_farmers()
        farmer_id = int(input("Enter ID of the farmer to delete: ").strip())
        farmer = session.query(Farmer).get(farmer_id)
        if not farmer:
            print("❌ Farmer not found.")
            return
        session.delete(farmer)
        session.commit()
        print("✅ Farmer deleted.")
    except Exception as e:
        print(f"Error: {e}")
        session.rollback()

# -------------------- FIELDS --------------------

# List all fields
def list_fields():
    fields = session.query(Field).all()
    if not fields:
        print("No fields found.")
        return
    print("\n🌾 Fields:")
    for field in fields:
        print(f"ID: {field.id} | Name: {field.name} | Location: {field.location} | Farmer: {field.farmer.name}")

# Add a new field
def add_field():
    try:
        name = input("Enter field name: ").strip()
        location = input("Enter field location: ").strip()
        list_farmers()
        farmer_id = int(input("Enter farmer ID for this field: ").strip())
        farmer = session.query(Farmer).get(farmer_id)

        if not farmer:
            print("❌ Farmer not found.")
            return

        new_field = Field(name=name, location=location, farmer_id=farmer.id)
        session.add(new_field)
        session.commit()
        print(f"✅ Field '{name}' added successfully.")
    except Exception as e:
        print(f"Error: {e}")
        session.rollback()

# Delete a field
def delete_field():
    try:
        list_fields()
        field_id = int(input("Enter ID of the field to delete: ").strip())
        field = session.query(Field).get(field_id)

        if not field:
            print("❌ Field not found.")
            return

        session.delete(field)
        session.commit()
        print("✅ Field deleted successfully.")
    except Exception as e:
        print(f"Error: {e}")
        session.rollback()

# -------------------- CROPS --------------------

# List all crops
def list_crops():
    crops = session.query(Crop).all()
    if not crops:
        print("No crops found.")
        return
    print("\n🌽 Crops:")
    for crop in crops:
        print(f"ID: {crop.id} | Type: {crop.crop_type} | Quantity: {crop.quantity}kg | Field: {crop.field.name}")

# Add a crop
def add_crop():
    try:
        list_fields()
        field_id = int(input("Enter field ID for this crop: ").strip())
        crop_type = input("Enter crop type: ").strip()
        quantity = float(input("Enter quantity (kg): ").strip())

        field = session.query(Field).get(field_id)
        if not field:
            print("❌ Field not found.")
            return

        crop = Crop(crop_type=crop_type, quantity=quantity, field_id=field.id)
        session.add(crop)
        session.commit()
        print(f"✅ Crop '{crop_type}' added.")
    except Exception as e:
        print(f"Error: {e}")
        session.rollback()
