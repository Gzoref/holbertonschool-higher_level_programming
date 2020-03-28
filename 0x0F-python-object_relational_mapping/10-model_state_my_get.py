#!/usr/bin/python3
'''
Prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
'''

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                       format(argv[1], argv[2], argv[3], pool_pre_ping=True))

state_name = argv[4]


Session = sessionmaker(bind=engine)
session = Session()


for state in session.query(State).order_by(State.id):
    if state.name == state_name:
        print('{}'.format(state.id))
        '''
        Not sure why only exit() gets correct output!!!
        '''
        exit()
print('Not found')

session.close()
