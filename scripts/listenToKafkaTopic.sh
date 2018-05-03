# Starts a docker container on the kafka-net docker network
# Exits on close Ctrl^C
# From spotify/kafka docker image
# Listens on topic test
docker run -it --rm --network kafka-net spotify/kafka /opt/kafka_2.11-0.10.1.0/bin/kafka-console-consumer.sh --bootstrap-server kafka-spotify:9092 --topic test --from-beginning
