import cat
from dbutils.pooled_db import PooledDB
import pymysql
from pymysql.err import OperationalError
from common.entity import MysqlEntity


class DBMysql:
    def __init__(self, config):
        self.pool = PooledDB(pymysql, mincached=config.limit_count, maxcached=0,
                             maxconnections=config.maxconnections,
                             host=config.host,
                             user=config.user,
                             port=config.port,
                             passwd=config.password,
                             db=config.database,
                             charset='utf8',
                             use_unicode=True,
                             blocking=True)

    @cat.transaction("SQL", "insert")
    def insert(self, entity):
        sql = "insert into xxxx(v1, v2, v3, v4) value(%s, %s, %s, %s)"
        conn = self.pool.connection()
        cursor = conn.cursor()
        results = []
        try:
            cursor.execute(sql, args=(entity.v1, entity.v2, entity.v3, entity.v4))
            conn.commit()
        except OperationalError as e:
            cat.log_exception(e)
        finally:
            cursor.close()
            conn.close()
        return results

    @cat.transaction("SQL", "query")
    def query(self, qid):
        sql = f"select v1, v2, v3, v4 from xxxx where id = %s"
        conn = self.pool.connection()
        cursor = conn.cursor()
        results = []
        try:
            cursor.execute(sql, args=(qid))
            for entity in map(MysqlEntity._make, cursor.fetchall()):
                results.append(entity)
        except OperationalError as e:
            cat.log_exception(e)
        finally:
            cursor.close()
            conn.close()
        return results
