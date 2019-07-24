from kafka import KafkaConsumer

consumer = KafkaConsumer('test2', group_id='consumer')
# 增加了一个 group，在同一个 group 下才生效
for record in consumer:
    print(record)
    print('---')
