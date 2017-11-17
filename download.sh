scala_version='2.11'
version='1.0.0'

wget http://apache-mirror.rbc.ru/pub/apache/kafka/${version}/kafka_${scala_version}-${version}.tgz
tar -zxvf kafka_${scala_version}-${version}.tgz
rm kafka_${scala_version}-${version}.tgz
#ln -s kafka_${scala_version}-${version} kafka