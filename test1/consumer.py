from kafka import KafkaConsumer

consumer = KafkaConsumer('test1')
for record in consumer:
    print(record)
