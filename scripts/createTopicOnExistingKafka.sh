# Runs command on the existing and running container kafka-spotify
# hits zookeeper and creates topic test
docker exec kafka-spotify /opt/kafka_2.11-0.10.1.0/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test
