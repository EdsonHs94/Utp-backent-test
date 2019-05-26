# -*- coding: utf-8 -*-
import falcon


class Authorization:

    def process_request(self, req: falcon.Request, resp):
        token = req.get_header('Authorization')

        if token is None:
            raise Exception('Token is Empty')

        if token == 'validToken':
            return
        raise Exception('invalidToken')
