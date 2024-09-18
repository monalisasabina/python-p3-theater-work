from sqlalchemy import ForeignKey, Column, Integer, String, MetaData,create_engine,Boolean
from sqlalchemy.orm import relationship,declarative_base,sessionmaker
# from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

engine=create_engine('sqlite:///theater.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

class Role(Base):
    __tablename__ = 'roles'
    
    id = Column(Integer, primary_key=True)
    character_name = Column(String)
    
    def __repr__(self):
       return f"<Role id: {self.id}: Character name {self.character_name} >"
    
    
    auditions = relationship("Audition", back_populates="role")

    

    
class Audition(Base):
    __tablename__ = 'auditions'
    
    id = Column(Integer, primary_key=True)
    actor = Column(String)
    location = Column(String)
    phone = Column(Integer)
    hired = Column(Boolean, default=False)
    role_id = Column(Integer, ForeignKey('roles.id'))

    def __repr__(self):
       return f"<Audition id: {self.id}: actor is {self.actor}," + \
         f"location {self.loaction}," + \
         f"phone: {self.phone}" +\
         f"hired: {self.hired} >"
    
    role = relationship("Role", back_populates="auditions")

