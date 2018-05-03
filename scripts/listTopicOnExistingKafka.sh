# Runs command on existing running container kafka-spotify
# Tells zookeeper to list all topics and then it exits
docker exec kafka-spotify /opt/kafka_2.11-0.10.1.0/bin/kafka-topics.sh --list --zookeeper localhost:2181
