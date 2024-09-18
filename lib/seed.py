#!/usr/bin/env python3

from models import Role, Audition, session,engine, Base

Base.metadata.create_all(engine)

if __name__ == "__main__":

    # avoid repetition
    session.query(Role).delete()
    session.query(Audition).delete()

    #creating role
    hamlet_role = Role(character_name="Hamlet")
    ophelia_role = Role(character_name="Ophelia")

    session.add_all([hamlet_role, ophelia_role])  
   

    # creating audtions
    audition1 = Audition(actor="John Doe", location="New York", phone=1234567890, role_id=hamlet_role.id)
    audition2 = Audition(actor="Jane Smith", location="Los Angeles", phone=9876543210, role_id=hamlet_role.id)
    audition3 = Audition(actor="Bob Johnson", location="Chicago", phone=5551234567, role_id=ophelia_role.id)

    session.add_all([audition1, audition2, audition3])

    # Commit changes
    session.commit()

    # checking all roles and auditions
    print('')
    print('Roles')
    roles= session.query(Role).all()
    print(roles)

    print('')
    print('Au')
    auditions = session.query(Audition).all()
    print(auditions)


