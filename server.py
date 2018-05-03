from flask import Flask, Response, request
from flask_cors import CORS
from kafka import KafkaProducer
import json

#producer = KafkaProducer(bootstrap_servers='host:port',value_serializer=lambda v: json.dumps(v).encode('utf-8'))

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET","POST"])
def hello():
    print request.get_json()
    body = request.get_json()

    producer = KafkaProducer(bootstrap_servers='172.20.0.2:9092',value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    producer.send('test', body)
    producer.close()
    return "Complete"

if __name__ == "__main__":
    app.run('0.0.0.0')
    print "After app.run"

    
