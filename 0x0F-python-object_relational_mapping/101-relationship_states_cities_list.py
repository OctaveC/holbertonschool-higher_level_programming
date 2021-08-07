#!/usr/bin/python3
"""
Lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()

    query = session.query(State).order_by(State.id).all()
    for row in query:
        print("{}: {}".format(row.id, row.name))
        for column in row.cities:
            print("\t{}: {}".format(column.id, column.name))

    session.close()
