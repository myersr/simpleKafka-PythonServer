# Simple kafka/flask server.  
Tutorial to come and be linked.

# Project Title

A couple examples of a python app that makes use of Kafka in a docker container, Kafka-python python library, and Flask as a webserver. The intent is to have several branches to cover multiple different scenarios utilizing Kafka.  
 * [kafkaProducerService.py](kafkaProducerService.py)
   * Currently a multi-threaded python script that shoots out messages to a kafka consumer.  
   * Loops for 17 seconds.
     * Thread sends 2 messages to the kafka topic 'test' every three seconds.  
     * only spawns one thread that is a producer
     * //TODO is change it to our specific use case for the tutorial.
 * [server.py](server.py)
   * A flask server
    * accepts a post
    * submits the post body to a kafka topic 'test' as JSON.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system `//TODO`.

### Prerequisites

What things you need to install the software and how to install them.  

These apps require a couple docker containers to run properly. The scripts should be all you need aside from Docker installed.  
Only one of the containers is used for the functionality. The other running container is just used to repeat kafka messages and would be replaced in any kind of deployment. For those reasons I didn't create a docker-compose config. One is just a constant output feed.  
```  
scripts/createTopicOnExistingKafka.sh    - Runs command on the running Kafka container to create a topic.
scripts/listTopicOnExistingKafka.sh      - Checks to make sure the topic was created. It runs a command on an existing Docker container
scripts/listenToKafkaTopic.sh            - Spans a temporary docker container to consume from the Kafka topic and it prints the message on the screen
scripts/startMasterZookeeperContainer.sh - Creates a docker network. Starts a container in the background that runs zookeeper and Kafka in the same container.  
```  

Order to run:
 * `startMasterZookeeperContainer.sh` > Output is the container ID
 * `createTopicOnExistingKafka.sh` > Output is something along the lines of Topic created
 * `listTopicOnExistingKafka.sh` > Output is something along the lines of current topics : <topic>
 * `listenToKafkaTopic.sh` > Output is nothing at first then it is the Kafka messages as they get consumed. Container exits when you Ctrl^C  

You will end with a persistent container running Kafka and Zookeeper in the background, a container printing out to the terminal relaying messages to a Kafka topic.  

### Installing

A step by step series of examples that tell you have to get a development env running. With python Always suggest a virtual environment.  


Install the python packages

```
pip install -r requirements.txt
```


Then you can run the apps.

```
python server.py
```  
or  
```  
python kafkaProducerService.py  
```



## Authors

* **Roy Myers** - *Initial work* - [myersr](https://github.com/myersr)


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

----
## Links and Thanks!
[kafka-python](http://kafka-python.readthedocs.io/en/master/)   
[Flask](http://flask.pocoo.org/)   
[Example kafka-python program/server](https://github.com/dpkp/kafka-python/blob/master/example.py)    
[Spotify image of Kafka](https://hub.docker.com/r/spotify/kafka/)   
[How to better use Kafka](https://gist.github.com/abacaphiliac/f0553548f9c577214d16290c2e751071)



Test if Zookeeper has registered a broker: `echo dump | nc localhost 2181 | grep brokers` and look for an ID   
To run Spotify container `docker run -p 2181:2181 -p 9092:9092 --env ADVERTISED_HOST=kafka-spotify --env ADVERTISED_PORT=9092 --name kafka-spotify spotify/kafka` instead of the supplied command as I don't have docker-machine.
Please Reach-out
