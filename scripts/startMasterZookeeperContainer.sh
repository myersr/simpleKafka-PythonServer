# Starts container in the background from spotify/kafka
# Runs Zookeeper and kafka in same container
# ADVERTISED_HOST 
#      is set to the container name as it is the advertised domain name
#      the container tries to connect to itself at this domain
#      MUST add the record `<docker machine ip>    kafka-spotify` to /etc/hosts
# On kafka-net so domain record is shared by containers
# named kafka-spotify. This must be the same as the advertised_host var
docker network create -d bridge kafka-net
docker run -d -p 2181:2181 -p 9092:9092 --env ADVERTISED_HOST=kafka-spotify --env ADVERTISED_PORT=9092 --network kafka-net --name kafka-spotify spotify/kafka
