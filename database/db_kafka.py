import cat
from utils.log import logger
from kafka import KafkaConsumer


class DBKafka:
    def __init__(self, config):
        self.topic = config.database.kafka.kafka_topic
        self.group = config.database.kafka.kafka_group
        self.kafka_bootstrap_servers = config.database.kafka.kafka_bootstrap_servers
        self.offset = 0
        self.consumer = KafkaConsumer(self.topic, group_id=self.group,
                                      bootstrap_servers=self.kafka_bootstrap_servers,
                                      max_poll_records=1)

    def messages_generate(self):
        """
        消费kafka信息
        :return:
        """
        while True:
            logger.info("table: %s" % self.topic)
            try:
                for message in self.consumer:
                    yield message
            except Exception as e:
                cat.log_exception(e)
