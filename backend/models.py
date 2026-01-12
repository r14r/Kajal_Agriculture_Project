from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
    ForeignKey,
    create_engine,
)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime

Base = declarative_base()


class Farmer(Base):
    __tablename__ = 'farmers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(String)
    location = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    crops = relationship('CropRecord', back_populates='farmer')
    soil_records = relationship('SoilRecord', back_populates='farmer')
    water_records = relationship('WaterRecord', back_populates='farmer')


class CropRecord(Base):
    __tablename__ = 'crop_records'
    id = Column(Integer, primary_key=True)
    farmer_id = Column(Integer, ForeignKey('farmers.id'))
    crop_name = Column(String, nullable=False)
    yield_kg = Column(Float)
    date_recorded = Column(String)
    planted_on = Column(DateTime, default=datetime.utcnow)
    notes = Column(String)

    farmer = relationship('Farmer', back_populates='crops')


class SoilRecord(Base):
    __tablename__ = 'soil_records'
    id = Column(Integer, primary_key=True)
    farmer_id = Column(Integer, ForeignKey('farmers.id'))
    ph = Column(Float)
    nitrogen = Column(Float)
    phosphorus = Column(Float)
    potassium = Column(Float)
    moisture = Column(Float)
    soil_type = Column(String)
    date_recorded = Column(String)
    recorded_at = Column(DateTime, default=datetime.utcnow)
    notes = Column(String)

    farmer = relationship('Farmer', back_populates='soil_records')


class WaterRecord(Base):
    __tablename__ = 'water_records'
    id = Column(Integer, primary_key=True)
    farmer_id = Column(Integer, ForeignKey('farmers.id'))
    ph = Column(Float)
    ec = Column(Float)
    tds = Column(Float)
    amount_l = Column(Float)
    date_recorded = Column(String)
    recorded_at = Column(DateTime, default=datetime.utcnow)
    notes = Column(String)

    farmer = relationship('Farmer', back_populates='water_records')


def init_db(path='sqlite:///agri_data.db'):
    engine = create_engine(path, connect_args={"check_same_thread": False})
    Base.metadata.create_all(engine)
    return engine


def get_session(engine):
    return sessionmaker(bind=engine)()
