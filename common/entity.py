from collections import namedtuple

class User:
    def __init__(self, user_id, user_status, experiment_strategy=None):
        self.user_id = user_id
        self.user_status = user_status
        self.experiment_strategy = experiment_strategy


MysqlEntity = namedtuple("entity", "v1, v2, v3, v4")
