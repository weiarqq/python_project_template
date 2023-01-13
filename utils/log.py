import re
import os
import json
import traceback
import logging
from config import config
from logging.handlers import TimedRotatingFileHandler


format = json.dumps({
    "level": "%(levelname)s",
    "module": "%(module)s",
    "line": "%(lineno)s",
    "time": "%(asctime)s",
    "message": "%(message)s",
    "applicationName": "%(name)s"
})


# 按时间间隔分割日志文件
def create_logger(name=None):
    if not name:
        name = config.application.name
    if not os.path.exists(config.log.log_dir):
        os.mkdir(config.log.log_dir)
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    formater = logging.Formatter(format)
    # formater = format
    # when:时间单位 S–秒 M–分 H–时 D—天 midnight-Roll over at midnight 大小写不敏感
    # interval:间隔多长时间分割一个日志文件
    # backupCount:保留最近文件的个数 默认 0 不删除文件
    file_time_handler = TimedRotatingFileHandler(f"{config.log.log_dir}/{name}.log", when="MIDNIGHT", interval=1, backupCount=0)
    file_time_handler.suffix = '%Y-%m-%d_%H:%M:%S.log'
    file_time_handler.extMatch = re.compile(r'^\d{4}-\d{2}-\d{2}_\d{2}:\d{2}:\d{2}.log$')
    file_time_handler.setFormatter(formater)
    logger.addHandler(file_time_handler)

    return logger


def error_format():
    return traceback.format_exc().replace("\n", "@@").replace('"', "'")


log_file = os.environ.get("LOG_FILE", None)
logger = create_logger(log_file)
