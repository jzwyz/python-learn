#!/usr/local/bin/python3
"""
kafka
"""
from kafka_consumer import MyConsumer
from kafka_producer import MyProducer
from threading import Thread

class ConsumerTask(Thread):
    """
    消费消息任务
    """

    def __init__(self, topic="demo"):
        super().__init__()
        self.topic = topic
        self.consumer = MyConsumer(topic)
    
    def run(self):
        print('%s 正在拉取数据', self.topic)
        self.consumer.pull_message()


def main():
    """
    测试Kafka消费者和生产者
    """
    task_1 = ConsumerTask('demo')
    task_2 = ConsumerTask('jzw')
    task_1.start()
    task_2.start()

if __name__ == "__main__":
    main()
