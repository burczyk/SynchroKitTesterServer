# -*- coding: utf-8 -*-
 
from django.db.models.base import ModelBase
from django.utils import simplejson
from django.utils.encoding import force_unicode
 
class LazyJSONEncoder(simplejson.JSONEncoder):

    def default(self, o):
        # this handles querysets and other iterable types
        try:
            iterable = iter(o)
        except TypeError:
            pass
        else:
            return list(iterable)
 
        # this handles Models
        try:
            isinstance(o.__class__, ModelBase)
        except Exception:
            pass
        else:
            return force_unicode(o)
 
        return super(LazyJSONEncoder, self).default(o)
 
def serialize_to_json(obj, *args, **kwargs):
    kwargs['ensure_ascii'] = False #kwargs.get('ensure_ascii', False)
    kwargs['cls'] = kwargs.get('cls', LazyJSONEncoder)
 
    return simplejson.dumps(obj, *args, **kwargs)