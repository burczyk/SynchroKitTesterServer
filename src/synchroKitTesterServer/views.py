# Create your views here.

from synchroKitTesterServer.models import User, Message
from synchroKitTesterServer.response import JSONResponse
from django.shortcuts import render_to_response

def get_model(request, model):

    modelResponses = { 
                        "User":     JSONResponse(User.objects.all().values('id', 'name', 'birthDate')),
                        "Message":  JSONResponse(Message.objects.all().values('id', 'text', 'user_id')),
                      }      

    return modelResponses.get(model, render_to_response('404jsontab.html'))