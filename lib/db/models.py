from sqlalchemy import Column, Integer, String, ForeignKey,create_engine
from sqlalchemy.orm import relationship, declarative_base,sessionmaker

engine = create_engine('sqlite:///farm.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Farmer(Base):
    __tablename__ = 'farmers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

    fields = relationship('Field', back_populates='farmer', cascade='all, delete-orphan')

    def __repr__(self):
        return f"Farmer(id={self.id}, name='{self.name}', email='{self.email}')"

class Crop(Base):
    __tablename__ = 'crops'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    planting_season = Column(String)
    harvest_season = Column(String)
    yield_per_acre = Column(Integer)

    fields = relationship('Field', back_populates='crop')

    def __repr__(self):
        return f"Crop(id={self.id}, name='{self.name}')"

class Field(Base):
    __tablename__ = 'fields'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    size_in_acres = Column(Integer)
    farmer_id = Column(Integer, ForeignKey('farmers.id'))
    crop_id = Column(Integer, ForeignKey('crops.id'))

    farmer = relationship('Farmer', back_populates='fields')
    crop = relationship('Crop', back_populates='fields')

    def __repr__(self):
        return f"Field(id={self.id}, name='{self.name}', size_in_acres={self.size_in_acres})"
Base.metadata.create_all(engine)
