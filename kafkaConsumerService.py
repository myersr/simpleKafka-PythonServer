import threading, logging, time
import multiprocessing
import os

from kafka import  KafkaConsumer


#Thread class that continuously consumes messages from a Kafka message queue/topic
#  Input:
#    threading.Thread = instance of multiproccessing thread
class Consumer(multiprocessing.Process):
    #default initializing function of the thread.
    # Input:
    #   takes self to modify and initialize
    def __init__(self):
        #initializes thread and passes self. Magic multithreading stuff
        multiprocessing.Process.__init__(self)
        #Gives the thread an envent called stop_event so it can be interrupted.
        self.stop_event = multiprocessing.Event()

    #Function to stop the process        
    def stop(self):
        #Calls even stop_event and sets it. 
        #This gives context to the thread from the outside and lets you stop it.
        self.stop_event.set()
 
    #The main run function called when you call start.
    def run(self):
        if hasattr(os, 'getppid'):  # only available on Unix
           print 'parent process:', os.getppid()
           procID = os.getppid()
        #Bootstraps an instance of a Kafka producer.
        #Initializes the producer and identifies the docker server.
        #kafka-spotify is listed in /etc/hosts with the ip of the container
        #Input:
        #  topic to subscribe to: 'test'
        #  Id to identify the consumer should be unique to the connection
        #  Servers kafka is advertising as
        #  Which message rule to subscribe to. 'earliest' will grab the earliest unprocessed message
        #  Timeout limit
        consumer = KafkaConsumer('test',
                                 client_id='python-consumer-%s' % (procID),
                                 bootstrap_servers=['kafka-spotify:9092'],
                                 auto_offset_reset='latest',
                                 consumer_timeout_ms=1000)
        
        #Alternative way to subscribe to a topic
        #consumer.subscribe(['test'])

        #loop until the thread is stopped by checking the stop event
        while not self.stop_event.is_set():
            #Loop through ConsumerRecord objects in the consumer object
            for message in consumer:
                #print the messages to the screen with a note of the thread/client ID
                #print("python-consumer-%s processed message:  %s" % (procID, message))
                #print the messages to the screen with a note of the thread/client ID, Current Topic, message number,                #               The value of the message decoded as it is sent as bytecode
                print ("python-consumer-%s processed message: %s:%d: value=%s" % (procID, message.topic,
                               message.offset, message.value.decode('utf-8')))
                #break out of the for loop if the thread was notified of closure
                if self.stop_event.is_set():
                   break
       
        #Close the TCP connection to kafka  
        consumer.close()


#Main function called when the app is run
def main():
    #initialize a Consumer object/thread
    kafkConsumer = Consumer()

    #Start the thread working.
    kafkConsumer.start()

    #sleep for 17 second. If we weren't using threads this would halt the code
    time.sleep(20)
    
    #Call stop to set the thread event so it knows to stop
    print("Stopping kafkConsumer")
    kafkConsumer.stop()

    #Wait until the thread terminates. Can see the docs for more
    #https://docs.python.org/2/library/threading.html?highlight=thread#threading.Thread.join
    print("Waiting for execution to halt")
    kafkConsumer.join()

#the logic to run as process
if __name__ == "__main__":
    #Set logging format and level
    #logging.basicConfig(
    #    format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
    #    level=logging.INFO)

    #Call the main function
    main()

