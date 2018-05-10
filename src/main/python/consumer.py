from kafka import KafkaConsumer

consumer = KafkaConsumer(bootstrap_servers='127.0.0.1:9092',
                         group_id="test",
                         value_deserializer=bytes.decode)

consumer.subscribe(['test2'])

for message in consumer:
    print ("topic={} partition={} offset={} key={} value={}".format(message.topic,
        message.partition, message.offset, message.key,message.value)
    )
