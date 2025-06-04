from models import session, Farmer, Field, Crop

session.query(Field).delete()
session.query(Crop).delete()
session.query(Farmer).delete()

# Create Farmers
farmer1 = Farmer(name="Alice Kimani", email="alice@farm.com")
farmer2 = Farmer(name="James Mwangi", email="james@farm.com")

# Create Crops
crop1 = Crop(
    name="Maize",
    crop_type="Grain",
    quantity=300,
    planting_season="March",
    harvest_season="August",
    yield_per_acre=30
)

crop2 = Crop(
    name="Wheat",
    crop_type="Grain",
    quantity=200,
    planting_season="May",
    harvest_season="November",
    yield_per_acre=25
)

# Create Fields
field1 = Field(name="North Farm", location="Kiambu", size_in_acres=15, farmer=farmer1)
field2 = Field(name="South Farm", location="Nakuru", size_in_acres=10, farmer=farmer2)

# Associate crops with fields
field1.crops.append(crop1)
field2.crops.append(crop2)

# Save all to database
session.add_all([farmer1, farmer2, crop1, crop2, field1, field2])
session.commit()

print("🌱 Database seeded successfully with sample data.")
