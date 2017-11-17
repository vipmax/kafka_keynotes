from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers='192.168.13.109:9092',
                         value_serializer=str.encode)
for i in range(100000):
    producer.send('test', str(i),partition=33)
    time.sleep(1)

print("Producer ended")

