#!/usr/bin/python3
"""
Makes a list of all City objects from the database hbtn_0e_101_usa.
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

    query = session.query(City).all()
    for row in query:
        print("{}: {} -> {}".format(row.id, row.name, row.state.name))

    session.close()
