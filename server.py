from flask import Flask, Response, request
from flask_cors import CORS
from kafka import KafkaProducer
import json

#producer = KafkaProducer(bootstrap_servers='host:port',value_serializer=lambda v: json.dumps(v).encode('utf-8'))

#Initialize the Flask app
app = Flask(__name__)
#VERY UNSAFE for production. 
#Allows flask to accept cross-origin requests for local development
CORS(app)

#Register a function @ / that could be GET or POST
# defaults to http://localhost:5000/
@app.route("/", methods=["GET","POST"])
def hello(): #hello() is registered to route /
    #Gets the POST body as a JSON object
    print request.get_json()
    body = request.get_json()

    #Bootstraps an instance of a Kafka producer.
    #Initializes the producer and identifies the docker server.
    #kafka-spotify is listed in /etc/hosts with the ip of the container
    #Sets the producer serializer to JSON
    producer = KafkaProducer(bootstrap_servers='kafa-python:9092',value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    #Send a message to the kafka topic 'test'
    #passes the POST JSON body as the message
    producer.send('test', body)
    #Closes the TCP stream to Kafka
    producer.close()
    #Returns a Complete string
    return "Complete"

#Main process function
if __name__ == "__main__":
    #Bind to broadcast so you can access the server
    app.run('0.0.0.0')

    
