from kafka import KafkaConsumer

consumer = KafkaConsumer('test_topic')
for record in consumer:
    print(record)
