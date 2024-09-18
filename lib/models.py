from sqlalchemy import ForeignKey, Column, Integer, String, MetaData,create_engine,Boolean
from sqlalchemy.orm import relationship,declarative_base,sessionmaker
# from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

engine=create_engine('sqlite:///theater.db')
Session = sessionmaker(bind=engine)
session = Session()

class Role(Base):
    __tablename__ = 'roles'
    
    id = Column(Integer, primary_key=True)
    character_name = Column(String)
    
    def __repr__(self):
       return f"<Role id: {self.id}: Character name {self.character_name} >"
    
    
    auditions = relationship("Audition", back_populates="role")

    
    # returns a list of names from the actors associated with this role.
    def actors(self):
        return list(audition.actor for audition in self.auditions)
    
    # returns a list of locations from the auditions associated with this role.
    def locations(self):
        return list(audition.location for audition in self.auditions)

    #  returns the first instance of the audition that was hired for this 
    # role or returns a string 'no actor has been hired for this role'.
    def lead(self):
        hired_auditions = sorted([a for a in self.auditions if a.hired], key=lambda x: x.id)
        return hired_auditions[0].actor if hired_auditions else "no actor has been hired for this role"
    
    # returns the second instance of the audition that was hired for this role or returns a string 
    # 'no actor has been hired for understudy for this role'.
    def understudy(self):
        hired_auditions = sorted([a for a in self.auditions if a.hired], key=lambda x: x.id)
        return hired_auditions[1].actor if len(hired_auditions) > 1 else "no actor has been hired for understudy for this role"

    

    
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
         f"location {self.location}," + \
         f"phone: {self.phone}" +\
         f"hired: {self.hired} >"
    
    role = relationship("Role", back_populates="auditions")
 
    # will change the the hired attribute to True
    def call_back(self):
        self.hired = True

