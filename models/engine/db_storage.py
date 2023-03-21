from os import environ

import sqlalchemy.exc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import Base
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.user import User


class DBStorage:
    __engine = None
    __session = None

    all_classes = [City, State, Place, Review, Amenity, User]

    def __init__(self):
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'.format(
                environ['HBNB_MYSQL_USER'], environ['HBNB_MYSQL_PWD'],
                environ['HBNB_MYSQL_HOST'], environ['HBNB_MYSQL_DB']),
            pool_pre_ping=True)
        if environ['HBNB_ENV'] == 'test':
            Base.metadata.drop_all(self.__engine)
            pass

    def all(self, cls=None):
        if cls:
            results = {}
            for record in self.__session.query(cls).all():
                key = f"{record.to_dict()['__class__']}.{record.id}"
                results.update({key: record})
            return results

        results = {}
        for _class in self.all_classes:
            try:
                for record in self.__session.query(_class).all():
                    key = f"{record.to_dict()['__class__']}.{record.id}"
                    results.update({key: record})
            except sqlalchemy.exc.SQLAlchemyError:
                continue
        return results

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            for record in self.__session.query(obj.__name__):
                if record.id == obj.id:
                    self.__session.delete(record)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = Session()
