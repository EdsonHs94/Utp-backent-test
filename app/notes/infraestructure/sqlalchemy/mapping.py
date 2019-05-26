from sqlalchemy import MetaData, Table, Column, String, Integer, Text, SmallInteger, DateTime, Float, Boolean
from sqlalchemy.orm import mapper, clear_mappers
from notes.domain.entity.notes import Notes

metadata = MetaData()

notes = Table('notes', metadata,
              Column('id', Integer, primary_key=True, nullable=False),
              Column('message', String(200), nullable=False),
              Column('author', String(50), nullable=False),
              Column('name', String(50), nullable=False),
              )


def load_mapper():
    clear_mappers()
    mapper(Notes, notes)
