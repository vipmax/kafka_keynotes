bin/kafka-topics.sh --create --zookeeper 192.168.13.109:2181 --replication-factor 2 --partitions 100 --topic test

bin/kafka-topics.sh --list --zookeeper 192.168.13.109:2181

bin/kafka-topics.sh --describe --zookeeper 192.168.13.109:2181 --topic test