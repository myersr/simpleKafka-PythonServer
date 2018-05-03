import threading, logging, time
import multiprocessing

from kafka import  KafkaProducer


#Thread class that continuously sends messages to a Kafka message queue
#  Input:
#    threading.Thread = instance of multiproccessing thread
class Producer(threading.Thread):
    #default initializing function of the thread.
    # Input:
    #   takes self to modify and initialize
    def __init__(self):
        #initializes thread and passes self. Magic multithreading stuff
        threading.Thread.__init__(self)
        #Gives the thread an envent called stop_event so it can be interrupted.
        self.stop_event = threading.Event()

    #Function to stop the thread        
    def stop(self):
        #Calls even stop_event and sets it. 
        #This gives context to the thread from the outside and lets you stop it.
        self.stop_event.set()
 
    #The main run function called when you call start.
    def run(self):
        #Bootstraps an instance of a Kafka producer.
        #Initializes the producer and identifies the docker server.
        #kafka-spotify is listed in /etc/hosts with the ip of the container
        producer = KafkaProducer(bootstrap_servers='kafka-spotify:9092')

        #loop until the thread is stopped by checking the stop event
        while not self.stop_event.is_set():
            #Send two messages of type binary to the 'test' Topic
            producer.send('test', b"test")
            producer.send('test', b"\xc2Hola, mundo!")
            #Sleep for 3 seconds
            time.sleep(3)
       
        #Close the TCP stream to Kafka
        producer.close()


#Main function called when the app is run
def main():
    #initialize a producer object/thread
    kafkProducer = Producer()

    #Start the thread working.
    kafkProducer.start()

    #sleep for 17 second. If we weren't using threads this would halt the code
    time.sleep(17)
    
    #Call stop to set the thread event so it knows to stop
    kafkProducer.stop()

    #Wait until the thread terminates. Can see the docs for more
    #https://docs.python.org/2/library/threading.html?highlight=thread#threading.Thread.join
    kafkProducer.join()

#the logic of running as process
if __name__ == "__main__":
    #Set logging format and level
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
        )
    #Call the main function
    main()
