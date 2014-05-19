from django.http import HttpResponse, Http404
from django.template import Context, RequestContext
from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.template.loader import get_template

from noncertGmail import Gmail
import json

# Create your views here.
def home(request):
    #when the user has selected the form
    if request.method == 'POST':
        username = request.POST['gmailusername']
        password = request.POST['gmailpassword']
        gmail = Gmail(username, password)
        msgData = ""
        try:
            msgData = gmail.getGooglePlay()
        except:
            html = render_to_response('user.html', None, RequestContext(request))
            return HttpResponse(html)
        #msgData = msgData + gmail.getAmazon()
        #msgData = msgData + gmail.getSquare()
        

        template = get_template('gmail.html')
    	html = template.render(Context({'messages': msgData}))
        #gmail.closeGmail()
        return HttpResponse(html) 

    html = render_to_response('user.html', None, RequestContext(request))
    return HttpResponse(html)