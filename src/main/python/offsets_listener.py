import time
from kafka import KafkaConsumer, TopicPartition

consumer = KafkaConsumer(
    bootstrap_servers='127.0.0.1:9092',
    group_id="test",
    enable_auto_commit=False
)

while True:
    for p in consumer.partitions_for_topic('test'):
        tp = TopicPartition('test', p)
        consumer.assign([tp])
        committed = consumer.committed(tp)
        consumer.seek_to_end(tp)
        last_offset = consumer.position(tp)

        current_timestamp = int(time.time())
        print(current_timestamp)
        print("topic: {} partition: {} committed: {} last: {} ".format(
            'test', p, committed, last_offset)
        )

    time.sleep(1)

consumer.close(autocommit=False)