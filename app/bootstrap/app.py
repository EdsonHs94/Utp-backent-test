# -*- coding: utf-8 -*-
from notes.application.framewoork import FalconApi
from notes.infraestructure.sqlalchemy.mapping import load_mapper


class App:
    """Class App Base"""

    def __init__(self):
        load_mapper()
        self.api = FalconApi().api
