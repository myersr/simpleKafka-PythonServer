# Simple kafka/flask server.  

A couple examples of a python app that makes use of Kafka in a docker container, Kafka-python python library, and Flask as a webserver. The intent is to have several branches to cover multiple different scenarios utilizing Kafka.
  
This repository handles a couple Kafka use cases. In an incredibly simple overview:  
 * a __Producer__ sends a message to __Kafka__ 
 * __Kafka__ accepts the message and then looks for a consumer
 * a __Consumer__ grabs the message from __Kafka__ to process  

One very loose metaphor for a kafka system could be subscribing to a magazine. The Company(Producer) prints the magazine. They have your address but don't know how to get to you.  

The company delivers a stack of magazines to UPS(Kafka). UPS has no knowledge/use of what is in that magazine, but they know how to get it to the reader's(Consumer) address. UPS is in charge of delivering, tracking, and keeping the magazine safe.   

The reader(Consumer) has a mailbox with his address on the side therefore UPS drops off the magazine.

There are a couple of things to note here. 
 * Kafka messages are organized by topics 
   * A _consumer_ and _producer_ both read/write to the same topic
   * You can think of a topic like an address in the above scenario. It could be a business with multiple people working at the same location or it could be a single home with 1 occupant.
 * Kafka does a ton of stuff in the background that I will not get into in this repo. It handles replication and logging and the likes. The [Official Docs](https://kafka.apache.org/) are a good resource if you would like to learn more.  

This repo provides a basis for 2 different __Producer__ scenarios.  
 1. A running python Flask server that accepts a POST request and then opens a connection to Kafka. The server sends the POST body to kafka as JSON and closes the connection after the message is sent. 
    * [server.py](server.py)
 2. A python script that spawns a thread that opens a connection to Kafka and sends two messages every couple seconds for 17 seconds.  
    * [kafkaProducerService.py](kafkaProducerService.py)

This repo provides a basis for 1 __Consumer__ scenario.  
 1. A python script to spawn a thread that runs for 20 seconds and opens a connection to listen on a topic. The thread prints all messages to stdout then closes the connection after the 20 seconds.  
    * [kafkaConsumerService.py](kafkaConsumerService.py)  

This is not a tutorial for using/configuring Kafka. To make things simple, I use the spotify/kafka image that has all the needed functionality inside one container. This also nullifies a lot of the benefits that Kafka can provide. To make it easy, I have included scripts to get the container(s) up and running. The scripts have comments and I implore you to read the commands and be very familiar with what you are running.  
//Tutorial to come and be linked.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system `//TODO`.

### Prerequisites

What things you need to install the software and how to install them.  

These apps require a couple docker containers to run properly. The scripts should be all you need aside from Docker to handle the docker set-up.  
Only one of the containers is necessary, the one running Kafka/Zookeeper. A script is provided to run a Kafka Consumer that prints kafka messages for testing/debugging. For these reasons I didn't create a docker-compose config.  
```  
scripts/createTopicOnExistingKafka.sh    - Executes a command on the running Kafka container to create a topic.
scripts/listTopicOnExistingKafka.sh      - Checks to make sure the topic was created. It runs a command on an existing Docker container and lists all topics.
scripts/listenToKafkaTopic.sh            - Spawns a temporary docker container to consume from the Kafka topic. It prints the messages to stdout and exits on interrupt. 
scripts/startMasterZookeeperContainer.sh - Creates a docker network. Starts 1 container in the background that runs zookeeper and Kafka. This is the only necessary container and should be created first.  
```  

Order to run:
 * `startMasterZookeeperContainer.sh` > Output is the container ID
 * `createTopicOnExistingKafka.sh` > Output is something along the lines of Topic created
 * `listTopicOnExistingKafka.sh` > Output is something along the lines of current topics : <topic>
 * `listenToKafkaTopic.sh` > Output is nothing at first then it is the Kafka messages as they get consumed. Container exits when you Ctrl^C  

You will end with a persistent container running Kafka and Zookeeper in the background, a container printing out to the terminal relaying messages to a Kafka topic.  

## Installing

A step by step series of examples that tell you have to get a development env running. With python I Always suggest a virtual environment.  

__The docker container must be running for the producers to connect.__

Install the python packages

```
pip install -r requirements.txt
```  

To run the Consumer run  
```  
python kafkaConsumerService.py #Remember this only runs for 20 seconds
```  

Then you can run the consumers.

```
python server.py #Runs indefinitally but only sends a message when it recieves a POST
```  
or  
```  
python kafkaProducerService.py #Remember this only runs for 17 seconds
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
