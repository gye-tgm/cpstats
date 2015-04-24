from cpstats.models.model import VERDICT_AC, Task
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


def get_user_accounts(username):
    accounts = []
    session = model.Session()
    user = session.query(model.User).filter_by(uname=username).one()
    for acc in user.accounts:
        accounts.append({'handle': acc.handle, 'url': acc.url, 'oj': acc.oj_id})
    return accounts


def get_user_tasks(username):
    session = model.Session()
    user = session.query(model.User).filter_by(uname=username).one()
    # solved, not solved
    tasks = []
    for acc in user.accounts:
        submission_ac = session.query(model.Submission).filter_by(account_id=acc.id, verdict=VERDICT_AC).all()
        tasks.append([])
        for s in submission_ac:
            t = session.query(model.Task).filter_by(id=s.task_id).one()
            d = {'name': t.name, 'url': t.url}
            tasks[0].append(d)
            print(d)
    return tasks

@app.route('/user/<string:username>')
@app.route('/user/<string:username>/general')
def user_general(username):
    return render_template('user_general.html',
                           username=username,
                           accounts=get_user_accounts(username),
                           title='general',
                           subnav=SUBNAV)

@app.route('/user/<string:username>/tasks')
def user_tasks(username):
    # todo: get the tasks man!
    return render_template('user_tasks.html',
                           username=username,
                           accounts=get_user_accounts(username),
                           tasks=get_user_tasks(username),
                           title='tasks',
                           subnav=SUBNAV)