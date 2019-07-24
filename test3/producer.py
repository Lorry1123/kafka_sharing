import time

from kafka import KafkaProducer

producer = KafkaProducer()

for i in range(100):
    print('sending message ', i)
    producer.flush()
    # 让所有消息立刻发送，否则可能会由于 kafka 的策略产生堆积
    producer.send('test3', value=b'test', key=None)
    # key 决定了消息被存放在哪一个 partition，默认为 None，随机存放
    time.sleep(1)
