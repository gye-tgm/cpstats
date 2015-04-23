from flask import render_template
from cpstats.models import model
from cpstats import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/user/<uname>')
def user_profile(uname):
    accounts = []
    session = model.Session()
    user = session.query(model.User).filter_by(uname=uname).one()
    for acc in user.accounts:
        accounts.append({'handle': acc.handle, 'url': acc.url, 'oj': acc.oj_id})
    return render_template('user.html',
                           username=uname,
                           accounts=accounts)