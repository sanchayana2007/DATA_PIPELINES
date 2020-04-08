from kafka import KafkaConsumer
#from pymongo import MongoClient
from json import loads

consumer = KafkaConsumer(
    'fast-messages1',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',#Consume all the messages before the starting of the Consumer 
     enable_auto_commit=True,
     group_id='my-group',value_deserializer=lambda x: loads(x.decode('utf-8')))

for message in consumer:
 #   collection.insert_one(message)
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))
