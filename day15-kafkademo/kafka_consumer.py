#!/usr/local/bin/python3
from kafka import KafkaConsumer

class MyConsumer:
    """
    消费者
    """

    def __init__(self, topic='demo'):
        """
        auto_offset_reset='earliest', enable_auto_commit=False  获取所有队列数据
        """
        super().__init__()
        self.consumer = KafkaConsumer(topic, bootstrap_servers='localhost:9092',
                                      auto_offset_reset='earliest', enable_auto_commit=False)

    def pull_message(self):
        """
        获取主题信息
        此处是等待的,会一直轮训队列
        """
        for message in self.consumer:
            print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                                 message.offset, message.key,
                                                 bytes.decode(message.value)))


def main():
    """
    测试Kafka消费者和生产者
    """
    c = MyConsumer("jzw")
    c.pull_message()


if __name__ == "__main__":
    main()
