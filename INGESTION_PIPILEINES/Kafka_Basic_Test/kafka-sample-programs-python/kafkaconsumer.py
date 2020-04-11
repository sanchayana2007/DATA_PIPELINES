from kafka import KafkaConsumer
#from pymongo import MongoClient
from json import loads

#Set this as Config Files or Environ Vraibales 
KAFKA_BROKER_URL='localhost:9092'
TRANSACTIONS_TOPIC ='fast-messages1'


consumer = KafkaConsumer(
    TRANSACTIONS_TOPIC,
     bootstrap_servers=[KAFKA_BROKER_URL],
     auto_offset_reset='earliest',#Consume all the messages before the starting of the Consumer 
     enable_auto_commit=True,
     group_id='my-group',value_deserializer=lambda x: loads(x.decode('utf-8')))

#Stream data is stored as Key Value Paair
for message in consumer:
 #   collection.insert_one(message)
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))
