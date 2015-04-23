from flask import render_template
from cpstats.models import model
from cpstats import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

SUBNAV = [
    'general',
    'submissions',
    'tasks',
    'achievements'
]

def user_accounts(username):
    accounts = []
    session = model.Session()
    user = session.query(model.User).filter_by(uname=username).one()
    for acc in user.accounts:
        accounts.append({'handle': acc.handle, 'url': acc.url, 'oj': acc.oj_id})
    return accounts

@app.route('/user/<string:username>')
@app.route('/user/<string:username>/general')
def user_general(username):
    return render_template('user_general.html',
                           username=username,
                           accounts=user_accounts(username),
                           title='general',
                           subnav=SUBNAV)

@app.route('/user/<string:username>/tasks')
def user_tasks(username):
    # todo: get the tasks man!
    tasks = None
    return render_template('user_tasks.html',
                           username=username,
                           accounts=user_accounts(username),
                           tasks=tasks,
                           title='tasks',
                           subnav=SUBNAV)