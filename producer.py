from kafka import KafkaProducer

producer = KafkaProducer()

for i in range(100):
    print('sending message ', i)
    producer.send('test_topic', b'lua!')
