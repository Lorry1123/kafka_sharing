from kafka import KafkaConsumer

# consumer = KafkaConsumer('test3', group_id='consumer', enable_auto_commit=False)
# 每一条消息消费后不自动向 kafka 发送 ack
consumer = KafkaConsumer('test3', group_id='consumer', enable_auto_commit=True)

# 增加了一个 group，在同一个 group 下才生效
# print('consumer will start at: %s' % consumer.position(TopicPartition('test3', '0')))
for record in consumer:
    print(record)
    print('---')
