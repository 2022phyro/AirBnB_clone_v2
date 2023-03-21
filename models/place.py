#!/usr/bin/python3
""" Place Module for HBNB project """
from os import environ
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, \
    Integer, Float
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    # from amenity import place_amenity
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship("Review", backref="place", cascade="all, delete-orphan")

    # amenities = relationship("Amenity", secondary=place_amenity, viewonly=False)
    # else:
    #     city_id = ""
    #     user_id = ""
    #     name = ""
    #     description = ""
    #     number_rooms = 0
    #     number_bathrooms = 0
    #     max_guest = 0
    #     price_by_night = 0
    #     latitude = 0.0
    #     longitude = 0.0
    #     amenity_ids = []

    @property
    def reviews(self):
        from models import storage
        from review import Review
        all_reviews = storage.all(Review)
        result = []
        for k, v in all_reviews.items():
            if v['place_id'] == self.id:
                result.append(v)
        return result

    @property
    def amenities(self):
        from models import storage
        from amenity import Amenity
        all_perks = storage.all(Amenity)
        result = []
        for k, v in all_perks.items():
            if v['id'] in self.amenity_ids:
                result.append(v)
        return result

    @amenities.setter
    def amenities(self, value):
        from models import storage
        if value['__class__'] == "Amenity":
            self.amenity_ids.append(value.id)
            storage.save()
