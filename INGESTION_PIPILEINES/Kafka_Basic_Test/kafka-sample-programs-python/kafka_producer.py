from time import sleep
from json import dumps
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=lambda x:dumps(x).encode('utf-8'))
#producer = KafkaProducer(bootstrap_servers='localhost:9092',)





for e in range(1000):
    print('Number',e)
    data = {'number' : e}
    future=producer.send('fast-messages1', value=e)
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


