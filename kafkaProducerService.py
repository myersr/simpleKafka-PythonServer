import threading, logging, time
import multiprocessing

from kafka import  KafkaProducer


class Producer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.stop_event = threading.Event()
        
    def stop(self):
        self.stop_event.set()

    def run(self):
        producer = KafkaProducer(bootstrap_servers='172.20.0.2:9092')

        while not self.stop_event.is_set():
            producer.send('test', b"test")
            producer.send('test', b"\xc2Hola, mundo!")
            time.sleep(3)

        producer.close()


def main():
    kafkProducer = Producer()

    kafkProducer.start()

    time.sleep(17)
    
    kafkProducer.stop()

    kafkProducer.join()


if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
        )
    main()
