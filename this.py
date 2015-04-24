from cpstats.models.model import *
from cpstats.crawl.codeforces import * 

session = Session()

gdis_cf = CodeforcesAccount(handle='gdisastery', url='http://codeforces.com/profile/gdisastery', rating=2059, contribution=12)
gdisastery = User(uname='gdisastery')
gdisastery.accounts.append(gdis_cf)

session.add(gdisastery)
session.add(gdis_cf)
session.commit()

print("Account created")
c = CodeforcesCrawler()
c.crawl_tasks()
print("Tasks crawled")
c.crawl_submissions('gdisastery')
print("Submissions of gdisastery crawled")
