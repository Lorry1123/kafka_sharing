from kafka import KafkaConsumer

consumer = KafkaConsumer('test2', group_id='consumer')
# 增加了一个 group，指定 group id 后 partition 分配才生效
for record in consumer:
    print(record)
    print('---')
