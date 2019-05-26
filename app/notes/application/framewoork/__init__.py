import falcon
import json

from notes.application.framewoork.authorization import Authorization
from notes.application.services.notes import GetAllNotesService, SaveNotesService


class FalconApi:
    def __init__(self):
        self.api = falcon.API(
            middleware=[
                Authorization()
            ],
        )
        self.api.add_route('/', HomeHandler())
        self.api.add_route('/notes', NotesHandler())


class HomeHandler:
    def on_get(self, req, resp):
        """Handles GET requests"""
        quote = {
            'message': (
                "Para la funcionalidad principal dirigirce al servicio /notes"
            )
        }

        resp.media = quote


class NotesHandler:

    def on_get(self, req, resp):

        notes_service = GetAllNotesService()

        service_response = notes_service.execute()
        notes = []
        for note in service_response:
            notes.append(
                {
                    'id': note.id,
                    'message': note.message,
                    'author': note.author,
                    'name': note.name,
                }
            )

        """Handles GET requests"""
        quote = {
            'message': (
                "Peticion Exitosa"
            ),
            'result': notes
        }

        resp.media = quote

    def on_post(self, req, resp):
        request_data = req.stream.read()
        decoded_data = request_data.decode('utf-8')
        data_set = json.loads(decoded_data)
        notes_service = SaveNotesService()

        response = notes_service.execute(data_set)
        note = {
            'id': response.id,
            'message': response.message,
            'author': response.author,
            'name': response.name
        }

        """Handles GET requests"""
        quote = {
            'message': (
                "Peticion Exitosa"
            ),
            'result': note
        }

        resp.media = quote

