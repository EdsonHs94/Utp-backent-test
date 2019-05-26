from notes.infraestructure.adapter.sqlalchemy import SqlAlchemyAdapter
from notes.domain.entity.notes import Notes


class NotesSqlAlchemyRepository:

    def __init__(self):
        self.__adapter = SqlAlchemyAdapter()
        self.__adapter.entity = Notes

    def create(self, notes: Notes):
        try:
            return self.__adapter.create(notes)
        except Exception as e:
            raise e

    def get_all(self):
        return self.__adapter.find_all()
