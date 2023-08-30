#!/usr/bin/python3

''' this script uses SQLAlchemy ORM to cretae table like classes '''

import MySQLdb
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    db_query = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    user = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    in_state = sys.argv[4]

    engine = create_engine(db_query.format(user, pwd, db), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).filter(State.name == in_state).\
        order_by(State.id).first()

    if result is None:
        print('Not found')
    else:
        print(f"{result.id}")
