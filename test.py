from cpstats.model import *

session = Session()

gdis = User(uname='gdisastery')
session.add(gdis)

taxi = Task(name='Taxicab Driver\'s Problem', url='goo.gl/nDX5vu')
burg = Task(name='Burger Happiness', url='goo.gl/LCUQKP')
mist = Task(name='Correcting Mistakes', url='http://codeforces.com/problemset/problem/533/E')

session.add(taxi)
session.add(burg)
session.add(mist)
session.commit()

gdis.created_tasks.append(taxi)
gdis.created_tasks.append(burg)

session.commit()

# Print the tasks that gdisastery has created
print("tasks crafted by gdis")
for task in gdis.created_tasks:
  print(task.url)

cf = OnlineJudge(name='Codeforces', url='codeforces.com')
hr = OnlineJudge(name='HackerRank', url='hackerrank.com')
tc = OnlineJudge(name='TopCoder', url='topcoder.com')

session.add(cf)
session.add(hr)
session.add(tc)
session.commit()

hr.problemset.append(taxi)
hr.problemset.append(burg)
cf.problemset.append(mist)
session.commit()

# gdis_cf = CodeforcesAccount(handle='gdisastery', url='http://codeforces.com/profile/gdisastery', oj_id=cf.id)
gdis_hr = Account(handle='gdisastery', url='https://www.hackerrank.com/gdisastery', oj_id=hr.id)
gdis_tc = Account(handle='gdisastery', url='http://community.topcoder.com/tc?module=MemberProfile&cr=23074694', oj_id=hr.id)
gdis_cf = CodeforcesAccount(handle='gdisastery', url='http://codeforces.com/profile/gdisastery', rating=2059, contribution=12)

session.add(gdis_hr)
session.add(gdis_tc)
session.add(gdis_cf)
session.commit()

print("problemset of hackerrank")
for task in hr.problemset:
    u = session.query(User).filter_by(id = task.author_id).one()
    print("author: ", u.uname, " name: ", task.name, " link:", task.url)

gdis.accounts.append(gdis_hr)
gdis.accounts.append(gdis_tc)
gdis.accounts.append(gdis_cf)
session.commit()

print("accounts of gdis")
for acc in gdis.accounts:
    if isinstance(acc, CodeforcesAccount):
        print("handle: ", acc.handle, " url: ", acc.url, "rating: ", acc.rating, " contribution: ", acc.contribution)


gdis_mist = Submission(account_id=gdis_cf.id, task_id=mist.id, verdict="AC", language="C++")
session.add(gdis_mist)

# print all solved tasks
print("Solved tasks:")
solved_tasks = []
for st in gdis_cf.submitted_tasks:
    if st.verdict == "AC":
        task = session.query(Task).filter_by(id=st.task_id).one()
        solved_tasks.append(task)

for task in solved_tasks:
    print(task.name, " url: ", task.url)