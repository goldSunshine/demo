import time
import logging
import datetime
import decimal
import uuid

from flask import Response, jsonify, make_response
from flask.json import JSONEncoder as BaseJSONEncoder
from logging.handlers import TimedRotatingFileHandler


class JSONEncoder(BaseJSONEncoder):
    def default(self, o):
        if hasattr(o, "keys") and hasattr(o, "__getitem__"):
            return dict(o)
        if isinstance(o, datetime.datetime):
            # 格式化时间
            return o.strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(o, datetime.date):
            # 格式化日期
            return o.strftime("%Y-%m-%d")
        if isinstance(o, decimal.Decimal):
            # 格式化高精度数字
            return str(o)
        if isinstance(o, uuid.UUID):
            # 格式化uuid
            return str(o)
        if isinstance(o, bytes):
            # 格式化字节数据
            return o.decode("utf-8")
        return super(JSONEncoder, self).default(o)


class MyResponse(Response):
    @classmethod
    def force_type(cls, response, environ=None):
        if isinstance(response, (list, dict)):
            response = jsonify(response)
        return super(Response, cls).force_type(response, environ)


def json_response(code=200, data=None):
    if not data:
        data = {"msg": "success"}
    response = make_response(data, code)
    return response


def get_loghandler():
    # 默认日志等级的设置
    logging.basicConfig(level=logging.INFO)

    log_file_name = "log/" + time.strftime('%Y-%m-%d', time.localtime(time.time())) + ".log"
    # 创建日志记录器，指明日志保存路径,每个日志的大小，保存日志的上限
    file_log_handler = TimedRotatingFileHandler(log_file_name, when="midnight", interval=1, backupCount=10)
    # 设置日志的格式                   发生时间    日志等级     日志信息文件名      函数名          行数        日志信息
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(message)s')
    # 将日志记录器指定日志的格式
    file_log_handler.setFormatter(formatter)

    return file_log_handler