from models import Role, Audition,session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# engine = create_engine('sqlite:///theater.db')
# Session = sessionmaker(bind=engine)
# session = Session()

def exit_program():
    print("Goodbye!")
    exit()

def list_roles():
    roles = session.query(Role).all()
    return roles

def find_role_by_name():
    name = input("Enter the role's character name: ")
    role = session.query(Role).filter_by(character_name=name).first()
    return role

def find_role_by_id():
    id = input("Enter the role's id: ")
    role = session.query(Role).get(id)
    return role

def create_role():
    character_name = input("Enter the role's character name: ")
    role = Role(character_name=character_name)
    session.add(role)
    session.commit()
    return role

def update_role():
    id = input("Enter the role's id: ")
    role = session.query(Role).get(id)
    if role:
        character_name = input("Enter the role's new character name: ")
        role.character_name = character_name
        session.commit()
        return role
    return None

def delete_role():
    id = input("Enter the role's id: ")
    role = session.query(Role).get(id)
    if role:
        session.delete(role)
        session.commit()
        return role
    return None

def list_auditions(role_id=None):
    if role_id:
        return session.query(Audition).filter_by(role_id=role_id).all()
    return session.query(Audition).all()

def find_audition_by_id():
    id = input("Enter the audition's id: ")
    audition = session.query(Audition).get(id)
    return audition

def create_audition():
    actor = input("Enter the actor's name: ")
    location = input("Enter the audition location: ")
    phone = int(input("Enter the actor's phone number: "))
    role_id = int(input("Enter the role's id: "))
    audition = Audition(actor=actor, location=location, phone=phone, role_id=role_id)
    session.add(audition)
    session.commit()
    return audition

def update_audition():
    id = input("Enter the audition's id: ")
    audition = session.query(Audition).get(id)
    if audition:
        actor = input("Enter the actor's new name: ")
        location = input("Enter the new audition location: ")
        phone = int(input("Enter the actor's new phone number: "))
        role_id = int(input("Enter the new role's id: "))
        
        audition.actor = actor
        audition.location = location
        audition.phone = phone
        audition.role_id = role_id
        
        session.commit()
        return audition
    return None

def delete_audition():
    id = input("Enter the audition's id: ")
    audition = session.query(Audition).get(id)
    if audition:
        session.delete(audition)
        session.commit()
        return audition
    return None

def call_back_audition():
    id = input("Enter the audition's id: ")
    audition = session.query(Audition).get(id)
    if audition:
        audition.hired = True
        session.commit()
        return audition
    return None

def list_role_auditions():
    role_id = int(input("Enter the role's id: "))
    return session.query(Audition).filter_by(role_id=role_id).all()

def get_role_lead():
    role_id = int(input("Enter the role's id: "))
    role = session.query(Role).get(role_id)
    if role:
        hired_auditions = sorted([a for a in role.auditions if a.hired], key=lambda x: x.id)
        return hired_auditions[0] if hired_auditions else "No actor has been hired for this role"
    return None

def get_role_understudy():
    role_id = int(input("Enter the role's id: "))
    role = session.query(Role).get(role_id)
    if role:
        hired_auditions = sorted([a for a in role.auditions if a.hired], key=lambda x: x.id)
        return hired_auditions[1] if len(hired_auditions) > 1 else "No understudy has been hired for this role"
    return None