#!/usr/bin/python3
"""Start link class to table in database
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            argv[1], argv[2], argv[3]))
    session = Session(engine)
    state = session.query(State).order_by(State.id).filter_by(name=sys.argv[4])
    if state:
        print("{}".format(state[0].id))
    else:
        print("Not found")
    session.close()
