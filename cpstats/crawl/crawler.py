from cpstats.models.model import Session


class Crawler(object):
    def __init__(self):
        self.session = Session()