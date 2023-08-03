from sqlalchemy import Column, INTEGER, DOUBLE, VARCHAR, BOOLEAN, TIMESTAMP, TEXT, ForeignKey, text
from .database import Base, engine

#entities data
class PartTable(Base):
    __tablename__='part_tb'
    pid = Column(INTEGER, autoincrement=True, primary_key=True, nullable=False) 
    part_name = Column(VARCHAR(100), nullable=False)
    mat_comp = Column(VARCHAR(100), nullable=False)
    age = Column(INTEGER, nullable=False)
    condi = Column(BOOLEAN, nullable=False)
    location = Column(VARCHAR(100), nullable=False)
    manufacturer = Column(VARCHAR(100), nullable=False)
    aircraft_mod = Column(VARCHAR(100), nullable=False)

class SustainData(Base):
    __tablename__='sustain_data'
    sid = Column(INTEGER,ForeignKey('part_tb.pid', ondelete='CASCADE'), primary_key=True, nullable=False)
    pot_usecase = Column(VARCHAR(255), nullable=False)
    remanufacPotential = Column(DOUBLE, nullable=False)
    renewableContent = Column(DOUBLE, nullable=False)
    recycleRate = Column(DOUBLE, nullable=False)
    lca = Column(DOUBLE, nullable=False)

class RecycleData(Base):
    __tablename__='recycle_data'
    sid = Column(INTEGER, ForeignKey('sustain_data.sid', ondelete='CASCADE'), primary_key=True, nullable=False)
    rCarbonFP = Column(DOUBLE, nullable=False)
    rWaterUsage = Column(DOUBLE, nullable=False)
    rLandFill = Column(DOUBLE, nullable=False)
    rEneConsum = Column(DOUBLE, nullable=False)
    rToxicScore = Column(DOUBLE, nullable=False)

class NewManuData(Base):
    __tablename__='new_manu_data'
    sid = Column(INTEGER, ForeignKey('sustain_data.sid', ondelete='CASCADE'), primary_key=True, nullable=False)
    nCarbonFP = Column(DOUBLE, nullable=False)
    nWaterUsage = Column(DOUBLE, nullable=False)
    nLandFill = Column(DOUBLE, nullable=False)
    nEneConsum = Column(DOUBLE, nullable=False)
    nToxicScore = Column(DOUBLE, nullable=False)

class recycleEffortScore(Base):
    __tablename__='recycleEffortScore'
    pid = Column(INTEGER, primary_key=True, nullable=False)
    part_name = Column(VARCHAR(100), nullable=False)
    effort = Column(DOUBLE, nullable=False)

class sustainibilityScore(Base):
    __tablename__='sustainibilityScore'
    pid = Column(INTEGER, primary_key=True, nullable=False)
    part_name = Column(VARCHAR(100), nullable=False)
    score = Column(DOUBLE, nullable=False)

class costScore(Base):
    __tablename__='costScore'
    pid = Column(INTEGER, primary_key=True, nullable=False)
    part_name = Column(VARCHAR(100), nullable=False)
    score = Column(DOUBLE, nullable=False)

#credentials
class Manufacturer(Base):
    __tablename__ = 'manufacturer'
    user_id = Column(VARCHAR(100), primary_key=True, nullable=False)
    pwd = Column(VARCHAR(100), nullable=False)
    company = Column(VARCHAR(100), nullable=False)
    # created_at = Column(TIMESTAMP, nullable=False, server_default=text('NOW()'))
    created_at = Column(TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP'))

class Airline(Base):
    __tablename__ = 'airline'
    user_id = Column(VARCHAR(100), primary_key=True, nullable=False)
    pwd = Column(VARCHAR(100), nullable=False)
    company = Column(VARCHAR(100), nullable=False)
    # created_at = Column(TIMESTAMP, nullable=False, server_default=text('NOW()'))
    created_at = Column(TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP'))

class RFacility(Base):
    __tablename__ = 'rfacility'
    user_id = Column(VARCHAR(100), primary_key=True, nullable=False)
    pwd = Column(VARCHAR(100), nullable=False)
    # created_at = Column(TIMESTAMP, nullable=False, server_default=text('NOW()'))
    created_at = Column(TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP'))


Base.metadata.create_all(bind=engine)