import redis    # 导入redis 模块


class DBRedis:
    def __init__(self, config):
        self.pool = redis.ConnectionPool(host=config.host, port=6379, password=config.password, decode_responses=True)

    def get_redis_client(self):
        return redis.Redis(connection_pool=self.pool)


def get_batch_doc_id(redis_client, key, batch_size=100):
    i = 0
    batch_user_ids = []
    while i < batch_size:
        user_id = redis_client.lpop(key)
        if not user_id:
            break
        batch_user_ids.append(user_id)
        i += 1
    return batch_user_ids


def add_doc_id_to_redis(redis_client, key, user_ids):
    redis_client.rpush(key, user_ids)










