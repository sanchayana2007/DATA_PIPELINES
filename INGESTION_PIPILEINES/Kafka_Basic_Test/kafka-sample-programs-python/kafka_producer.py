from time import sleep
from json import dumps
from kafka import KafkaProducer

#Set this as Config Files or Environ Vraibales 
KAFKA_BROKER_URL='localhost:9092'
TRANSACTIONS_TOPIC ='fast-messages1'

#Producer is Intialised 
producer = KafkaProducer(bootstrap_servers=[KAFKA_BROKER_URL],value_serializer=lambda x:dumps(x).encode('utf-8'))





for e in range(1000):

    #This data is produced by teh stream and it changes wd ebery stream
    amt=1+e
    data = {"source": "Jpe2zq1QDYTn", "target": "lLbLnl0FSr7T", "amount": amt, "currency": "EUR"}

    future=producer.send(TRANSACTIONS_TOPIC, value=data)
    sleep(2)
    # Block for 'synchronous' sends
    try:
        record_metadata = future.get(timeout=10)
    except KafkaError:
        # Decide what to do if produce request failed...
        log.exception()
        pass

    # Successful result returns assigned partition and offset
    print (record_metadata.topic)
    print (record_metadata.partition)
    print (record_metadata.offset)


