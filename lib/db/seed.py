# lib/db/seed.py

from models import session, Farmer, Crop, Field

# 🚫 Clear existing data
session.query(Field).delete()
session.query(Farmer).delete()
session.query(Crop).delete()

# 👩‍🌾 Add Farmers
farmer1 = Farmer(name="Alice Kimani", email="alice@farm.com")
farmer2 = Farmer(name="James Mwangi", email="james@farm.com")

# 🌽 Add Crops
crop1 = Crop(name="Maize", planting_season="March", harvest_season="August", yield_per_acre=30)
crop2 = Crop(name="Wheat", planting_season="May", harvest_season="November", yield_per_acre=25)

# 🌾 Add Fields
field1 = Field(name="North Farm", size_in_acres=15, farmer=farmer1, crop=crop1)
field2 = Field(name="South Farm", size_in_acres=10, farmer=farmer2, crop=crop2)

# ✅ Save to DB
session.add_all([farmer1, farmer2, crop1, crop2, field1, field2])
session.commit()

print("🌱 Database seeded successfully with sample data.")
