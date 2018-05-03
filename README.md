Simple kafka/flask server.  
Tutorial to come.


----
## Links
[kafka-python](http://kafka-python.readthedocs.io/en/master/)   
[Flask](http://flask.pocoo.org/)   
[Example kafka-python program/server](https://github.com/dpkp/kafka-python/blob/master/example.py)    
[Spotify image of Kafka](https://hub.docker.com/r/spotify/kafka/)   
[How to better use Kafka](https://gist.github.com/abacaphiliac/f0553548f9c577214d16290c2e751071)



Test if Zookeeper has registered a broker: `echo dump | nc localhost 2181 | grep brokers` and look for an ID   
To run Spotify container `docker run -p 2181:2181 -p 9092:9092 --env ADVERTISED_HOST=kafka-spotify --env ADVERTISED_PORT=9092 --name kafka-spotify spotify/kafka` instead of the supplied command as I don't have docker-machine.
