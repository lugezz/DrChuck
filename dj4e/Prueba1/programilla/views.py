from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils.html import escape
from django.views import View

import logging

logger = logging.getLogger(__name__)

def helloworld(request):
    logging.error('Hello world DJ4E in the log...')
    print('Hello world DJ4E in a print statement...')
    response = """<html><body><p>Hello world DJ4E in HTML</p>
    <p>This sample code is available at
    <a href="https://github.com/csev/dj4e-samples">
    https://github.com/csev/dj4e-samples</a></p>
    </body></html>"""
    return HttpResponse(response)


def tracks(request):
    response = """<html><body><p>Tracks Data Modeling Example</p>
    <p>This sample code is available at
    <a href="https://github.com/csev/dj4e-samples">
    https://github.com/csev/dj4e-samples</a></p>
    <p>This example needs to be run in the Django shell in the command line
    and <a href="/admin">the admin console</a> after making a superuser.
    </body></html>"""
    return HttpResponse(response)

def funky(request):
    response = """<html><body><p>This is the funky function sample</p>
    <p>This sample code is available at
    <a href="https://github.com/csev/dj4e-samples">
    https://github.com/csev/dj4e-samples</a></p>
    </body></html>"""
    return HttpResponse(response)

def danger(request) :
    response = """<html><body>
    <p>Your guess was """+request.GET['guess']+"""</p>
    </body></html>"""
    return HttpResponse(response)

def danger2(request) :
    response = """<html><body>
    <p>Your guess was """+request.GET['guess2']+"""</p>
    </body></html>"""
    return HttpResponse(response)

def game(request) :
    response = """<html><body>
    <p>Your guess was """+escape(request.GET['guess'])+"""</p>
    </body></html>"""
    return HttpResponse(response)

def rest(request, guess) :
    response = """<html><body>
    <p>Your guess was """+escape(guess)+"""</p>
    </body></html>"""
    return HttpResponse(response)

# This is a command to the browser
def bounce(request) :
    return HttpResponseRedirect('https://www.dj4e.com/simple.htm')

# https://docs.djangoproject.com/en/3.0/topics/class-based-views/
class MainView(View) :
    def get(self, request):
        response = """<html><body><p>Hello world MainView in HTML</p>
        <p>This sample code is available at
        <a href="https://github.com/csev/dj4e-samples">
        https://github.com/csev/dj4e-samples</a></p>
        </body></html>"""
        return HttpResponse(response)

class RestMainView(View) :
    def get(self, request, guess):
        print("We got a slug from the URL",guess);
        response = """<html><body>
        <p>Your guess was """+escape(guess)+"""</p>
        </body></html>"""
        return HttpResponse(response)

class RestMainView2(View) :
    def get(self, request, guess):
        print("We got a slug from the URL",guess);
        response = """<html><body>
        <p>Your guess was """+guess+"""</p>
        </body></html>"""
        return HttpResponse(response)

class Juego1(View):
    def get(self, request, num):
        context = {'num': num}

        return render(request, 'programilla/juego1.html' ,context)