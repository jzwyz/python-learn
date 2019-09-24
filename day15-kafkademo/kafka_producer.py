#!/usr/local/bin/python3
from kafka import KafkaProducer
from kafka.errors import KafkaError

class MyProducer:
    """
    生产者
    """

    def __init__(self):
        super().__init__()
        self.producer = KafkaProducer(bootstrap_servers=["localhost:9092"])

    def send_message(self, topic="demo", msg=None):
        """
        发送消息
        :msg 消息体
        :topic 主题
        """
        if msg is None: 
            print('消息为空')
            return
        future = self.producer.send(topic, msg.encode('utf-8'))
        record_metadata = future.get(timeout=10)
        print("%s:%d:%d: value=%s" % (record_metadata.topic, record_metadata.partition,
                                             record_metadata.offset, msg))

def main():
    pro = MyProducer()
    pro.send_message("jzw", "My Name is Jason")

if __name__ == "__main__":
    main()
