from kafka import KafkaConsumer

consumer = KafkaConsumer(bootstrap_servers='192.168.13.109:9092',
                         group_id="test",
                         value_deserializer=bytes.decode)

consumer.subscribe(['test'])

for message in consumer:
    print ("topic={} partition={} offset={} key={} value={}".format(message.topic,
        message.partition, message.offset, message.key,message.value)
    )
