# app/models.py

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Bakery(db.Model, SerializerMixin):
    __tablename__ = 'bakeries'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    baked_goods = relationship('BakedGood', back_populates='bakery')

class BakedGood(db.Model, SerializerMixin):
    __tablename__ = 'baked_goods'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    bakery_id = db.Column(db.Integer, db.ForeignKey('bakeries.id'))
    bakery = relationship('Bakery', back_populates='baked_goods')
