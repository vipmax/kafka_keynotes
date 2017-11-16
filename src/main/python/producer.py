from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092',
                         value_serializer=str.encode)
for i in range(100000):
    producer.send('test', str(i))
    time.sleep(1)

print("Producer ended")

