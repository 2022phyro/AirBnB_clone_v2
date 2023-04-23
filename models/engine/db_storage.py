#!/usr/bin/python3
"""This is the db_storage module. It contains our
DbStorage class which is necessary for handling files
in our databse"""
from os import environ, getenv
import sqlalchemy.exc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.user import User


class DBStorage:
    """This class is the storage engine for our
    database. It handles all the tools neeeded to allow
    seamless tranfer of data to and fro the databse"""
    __engine = None
    __session = None

    all_classes = [City, State, Place, Review, Amenity, User]

    def __init__(self):
        """This instantiates the database
        and creates our engine"""
        self.__engine = create_engine(
                 'mysql+mysqldb://{}:{}@{}:3306/{}'.format(
                        environ['HBNB_MYSQL_USER'], environ['HBNB_MYSQL_PWD'],
                        environ['HBNB_MYSQL_HOST'], environ['HBNB_MYSQL_DB']),
                 pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """This returns all items in the database"""
        if cls:
            results = {}
            for record in self.__session.query(cls).all():
                key = "{}.{}".format(record.to_dict()['__class__'], record.id)
                results.update({key: record})
            return results

        results = {}
        for _class in self.all_classes:
            try:
                for record in self.__session.query(_class).all():
                    key = "{}.{}".format(
                            record.to_dict()['__class__'], record.id)
                    results.update({key: record})
            except sqlalchemy.exc.SQLAlchemyError:
                continue
        return results

    def new(self, obj):
        """This adds a new object to the database"""
        self.__session.add(obj)

    def save(self):
        """This saves the current progress/session
        of the database changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """This deletes an item from the database"""
        if obj is not None:
            for record in self.__session.query(obj.__name__):
                if record.id == obj.id:
                    self.__session.delete(record)

    def reload(self):
        """This recreates/sbegins an asql session"""
        Base.metadata.create_all(self.__engine)
        session_fac = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_fac)
        self.__session = Session()

    def close(self):
        """Closes the session"""
        self.__session.close()
