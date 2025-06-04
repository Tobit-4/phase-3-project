from sqlalchemy import Column, Integer, String, ForeignKey, Table, create_engine
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

engine = create_engine('sqlite:///farm.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

field_crop = Table(
    'field_crop', Base.metadata,
    Column('field_id', ForeignKey('fields.id'), primary_key=True),
    Column('crop_id', ForeignKey('crops.id'), primary_key=True)
)

class Farmer(Base):
    __tablename__ = 'farmers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

    fields = relationship('Field', back_populates='farmer', cascade='all, delete-orphan')

    def __repr__(self):
        return f"Farmer(id={self.id}, name='{self.name}', email='{self.email}')"

class Field(Base):
    __tablename__ = 'fields'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    size_in_acres = Column(Integer)
    farmer_id = Column(Integer, ForeignKey('farmers.id'))

    farmer = relationship('Farmer', back_populates='fields')
    crops = relationship('Crop', back_populates='field', cascade='all, delete-orphan')

    def __repr__(self):
        return f"Field(id={self.id}, name='{self.name}', size_in_acres={self.size_in_acres})"

class Crop(Base):
    __tablename__ = 'crops'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    crop_type = Column(String)
    quantity = Column(Integer)
    planting_season = Column(String)
    harvest_season = Column(String)
    yield_per_acre = Column(Integer)
    field_id = Column(Integer, ForeignKey('fields.id'))

    field = relationship('Field', back_populates='crops')

    def __repr__(self):
        return f"Crop(id={self.id}, name='{self.name}')"

# Create the tables
Base.metadata.create_all(engine)
