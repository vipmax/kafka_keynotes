bin/kafka-topics.sh --create --zookeeper 127.0.0.1:2181 --replication-factor 1 --partitions 10 --topic test10

bin/kafka-topics.sh --list --zookeeper 192.168.13.109:2181

bin/kafka-topics.sh --describe --zookeeper 192.168.13.109:2181 --topic test