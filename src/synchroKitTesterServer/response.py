# -*- coding: utf-8 -*-
 
from synchroKitTesterServer.utils import serialize_to_json
from django.http import HttpResponse

 
class JSONResponse(HttpResponse):
    def __init__(self, content='', json_opts={}, mimetype="application/json", *args, **kwargs):

        if content:
            content = serialize_to_json(content, **json_opts)
        else:
            content = serialize_to_json([], **json_opts)
        super(JSONResponse, self).__init__(content, mimetype, *args, **kwargs)
