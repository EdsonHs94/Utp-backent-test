from notes.infraestructure.sqlalchemy.notes import NotesSqlAlchemyRepository
from notes.domain.entity.notes import Notes


class NotesDomainService(object):

    def __init__(self):
        self.__repository = NotesSqlAlchemyRepository()

    def get_all_notes(self):
        return self.__repository.get_all()

    def create(self, new_note):
        note = Notes(
            new_note['message'],
            new_note['name'],
            new_note['author'],
        )
        return self.__repository.create(note)
