from flask import render_template
from ..models import User
from . import main



@main.route('/', methods=['GET', 'POST'])
def index():
    users=User.query.all()
    return render_template('index.html', users=users)