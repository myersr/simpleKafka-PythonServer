from flask import Flask, Response, request
from kafka import KafkaProducer
import json

#producer = KafkaProducer(bootstrap_servers='host:port',value_serializer=lambda v: json.dumps(v).encode('utf-8'))

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def hello():
    print request.get_json()

    producer = KafkaProducer(bootstrap_servers='localhost:9092',value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    producer.send(body)
    return "Complete"

if __name__ == "__main__":
    app.run('0.0.0.0')

    
