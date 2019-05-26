from notes.domain.services.notes import NotesDomainService


class GetAllNotesService(object):

    def __init__(self):
        self.__domain_service = NotesDomainService()

    def execute(self):
        return self.__domain_service.get_all_notes()


class SaveNotesService(object):

    def __init__(self):
        self.__domain_service = NotesDomainService()

    def execute(self, note):
        return self.__domain_service.create(note)
