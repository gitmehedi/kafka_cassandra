from kafka import KafkaConsumer
from cassandra.cluster import Cluster
import random,string,time
from json import loads

PORT = 9042
IP = ['192.168.56.22']
KEYSPACE = 'test_keyspace'

cluster = Cluster(IP,port=PORT)
cursor = cluster.connect(keyspace=KEYSPACE)

consumer = KafkaConsumer(
    'numtest',
     bootstrap_servers=['192.168.56.22:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))


for message in consumer:
    username = message.value['username']
    password = message.value['password']
    cursor.execute("INSERT INTO USERS (username,password,fullname) VALUES (%s,%s,%s)",(username,password,username))