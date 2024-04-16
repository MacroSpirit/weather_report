from sqlalchemy import create_engine, Column, Integer, DateTime, JSON
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from datetime import datetime



engine = create_engine(
    'sqlite:///weather_report.db'
)


Session = sessionmaker(engine)

class Model(DeclarativeBase):
    pass

class WeatherDataTable(Model):
    __tablename__ = 'weather_report'
    id = Column(Integer, primary_key=True)
    data = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)

def create_table():
    Model.metadata.create_all(engine)