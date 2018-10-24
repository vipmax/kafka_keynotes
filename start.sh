#bin/zookeeper-server-start.sh config/zookeeper.properties
#bin/kafka-server-start.sh config/server.properties

nohup kafka/bin/zookeeper-server-start.sh kafka/config/zookeeper.properties > zoo.log &
sleep 1s
nohup kafka/bin/kafka-server-start.sh kafka/config/server.properties > kafka.log &

echo "zookeeper, kafka started"