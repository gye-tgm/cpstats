from cpstats.crawl.crawler import Crawler
from cpstats.models.model import VERDICT_AC, VERDICT_WA, VERDICT_TLE, VERDICT_CE, VERDICT_RTE, Submission, Task
import requests


class CodeforcesCrawler(Crawler):

    def __init__(self):
        super().__init__()
        self.vm = {
            "OK": VERDICT_AC,
            "WRONG_ANSWER": VERDICT_WA,
            "COMPILATION_ERROR": VERDICT_CE,
            "TIME_LIMIT_EXCEEDED": VERDICT_TLE,
            "RUNTIME_ERROR": VERDICT_RTE
        }

    def crawl_tasks(self):
        url = "http://codeforces.com/api/problemset.problems"
        data = requests.get(url).json()
        for task in data['result']['problems']:
            self.session.add(Task(name=task['name']))
        self.session.commit()

    def crawl_submissions(self, handle, count=65536):
        url = "http://codeforces.com/api/user.status?handle=%s&from=1&count=%d" % (handle, count)
        data = requests.get(url).json()
        for submission in data['result']:
            s = Submission(verdict=self.vm[submission['verdict']],
                           language=submission['programmingLanguage'])
            self.session.add(s)
        self.session.commit()
        return True


    @staticmethod
    def user_info(handle):
        url = "http://codeforces.com/api/user.info?handles=" + handle
        return requests.get(url).json()['result'][0]

if __name__ == '__main__':
    c = CodeforcesCrawler()
    c.crawl_tasks()
