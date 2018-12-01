#! python3
def application(env, start_response):
    start_response('200 OK', [('Content-type','text/plain')])
    return '<p>Hello, WSGI</p>'

from werkzeug import run_simple
run_simple('0.0.0.0', 8080, application)

