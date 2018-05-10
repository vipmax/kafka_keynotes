import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.common.serialization.StringDeserializer;

import java.util.Collections;
import java.util.Properties;

class Consumer {
    public static void main(String[] args) {
        Properties props = new Properties();
        props.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "127.0.0.1:9092");
        props.put(ConsumerConfig.GROUP_ID_CONFIG, "KafkaExampleConsumer");
        props.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
        props.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());

        KafkaConsumer consumer = new KafkaConsumer<String, String>(props);

        consumer.subscribe(Collections.singletonList("test2"));

        while (true) {
            final ConsumerRecords<Long, String> consumerRecords = consumer.poll(1000);
            consumerRecords.forEach(record -> {
                System.out.printf("topic=%s key=%d partition=%d offset=%d value=%s  \n",
                        record.topic(),record.key(),
                        record.partition(), record.offset(), record.value());
            });

//            consumer.commitAsync();
        }
    }
}