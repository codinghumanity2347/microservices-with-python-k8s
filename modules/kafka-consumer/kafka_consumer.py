import os
import time
from datetime import datetime

import psycopg2
from google.protobuf.timestamp_pb2 import Timestamp
from kafka import KafkaConsumer

import location_pb2

TOPIC_NAME = 'locations'
KAFKA_ADD = os.environ["KAFKA_ADD"]

consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=KAFKA_ADD)
location_message = location_pb2.Location()
timestamp = Timestamp()
DB_USERNAME = os.environ["DB_USERNAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_NAME = os.environ["DB_NAME"]
conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USERNAME, password=DB_PASSWORD)
sql = """insert into public.location 
( person_id, coordinate, creation_time) values (%s,ST_SetSRID(ST_MakePoint(%s, %s), 4326),%s);
"""
for message in consumer:

    location_message.ParseFromString(message.value)
    dt_object = datetime.fromtimestamp(time.time())

    record_to_insert = (
        location_message.personId, location_message.latitude, location_message.longitude, dt_object)
    try:
        conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USERNAME, password=DB_PASSWORD)
        cur = conn.cursor()
        cur.execute(sql, record_to_insert)
        cur.close()
        conn.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
