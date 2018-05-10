scala_version='2.11'
kafka_version='1.0.0'

wget http://apache-mirror.rbc.ru/pub/apache/kafka/${kafka_version}/kafka_${scala_version}-${kafka_version}.tgz
tar -zxvf kafka_${scala_version}-${kafka_version}.tgz
rm kafka_${scala_version}-${kafka_version}.tgz
ln -s kafka_${scala_version}-${version} kafka