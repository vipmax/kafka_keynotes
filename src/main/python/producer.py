from kafka import KafkaProducer
import time
from random import randint

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=str.encode)
topicname = 'test'

for i in range(100000):
    value = str(randint(0, 9))
    producer.send(topicname, value=value)
    print("Sended " + value)
    time.sleep(1)

print("Producer ended")

