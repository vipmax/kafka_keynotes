from kafka import KafkaProducer
import time
from random import randint

producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092',
                         value_serializer=str.encode)
for i in range(100000):
    value = str(randint(0, 9))
    producer.send('test2', value)
    print("Sended " + value)
    time.sleep(1)

print("Producer ended")

