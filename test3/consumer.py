from kafka import KafkaConsumer

consumer = KafkaConsumer('test3', group_id='consumer', enable_auto_commit=False)
# 每一条消息消费后不自动向 kafka 发送 ack
# consumer = KafkaConsumer('test3', group_id='consumer', enable_auto_commit=True)

for record in consumer:
    print(record)
    print('---')
