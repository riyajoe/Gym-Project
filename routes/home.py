from app import app,db
from flask import render_template
from models.Packages import *
from models.Helper import *
from models.Client import *
from models.Users import requires_roles

@app.route('/Home')
@requires_roles(1)
def Home():
    db.create_all()
    result=Packages.query.filter_by(packagetype='S').all()
    return(render_template('Menu.html',data=result))