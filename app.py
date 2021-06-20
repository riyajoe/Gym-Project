from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
from flask_login import LoginManager



app = Flask(__name__)


app.config['SECRET_KEY'] = 'SECURITY_KEY'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:root@localhost/gym'
db=SQLAlchemy(app)
login = LoginManager(app)
login.login_view

from routes.setup import *
from routes.home import *
from routes.deals import *
from routes.package import *
from routes.schedule import *
from routes.membership import *
from routes.trainerdashoard import *
from routes.login import *
from routes.clientdashboard import *
import forms
from requestlogger import WSGILogger, ApacheFormatter
from logging.handlers import TimedRotatingFileHandler
from wsgiref.simple_server import make_server

def application(environ, start_response):
    response_body = 'The request method was %s' % environ['REQUEST_METHOD']
    response_body = response_body.encode('utf-8')
    response_headers = [('Content-Type', 'text/plain'),
                        ('Content-Length', str(len(response_body)))]
    start_response('200 OK', response_headers)
    return [response_body]

handlers = [ TimedRotatingFileHandler('access.log', 'd', 7) , ]
loggingapp = WSGILogger(application, handlers, ApacheFormatter())


if __name__ == "__main__":
    app.run(debug=True)
   
    http = make_server('', 5000, loggingapp)
    http.serve_forever()








        