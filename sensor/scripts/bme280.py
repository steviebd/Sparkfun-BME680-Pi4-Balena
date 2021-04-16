from time import sleep
import qwiic_bme280
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import os

# Variables used and inputted into the fuctions
my_bucket = os.getenv("INFLUX_DB_BUCKET")
influx_token = os.getenv("INFLUX_DB_TOKEN")
influx_org = os.getenv("INFLUX_DB_ORG")
location = os.getenv("DEVICE_DB_LOCATION")
measurement_name = "bme280"

# # startup of sensor so it doesn't just write 0 values
# API Docs @ https://qwiic-bme280-py.readthedocs.io/en/latest/?
mySensor = qwiic_bme280.QwiicBme280()
mySensor.begin()
sleep(180)

# Connect to client



while True:
    # format the data as a single measurement for influx                     
    humidity_level = Point(measurement_name).tag("location", location).field("Humidity", float(mySensor.humidity))
    pressure_level = Point(measurement_name).tag("location", location).field("Pressure", float(mySensor.pressure))
    dewpoint_celsius = Point(measurement_name).tag("location", location).field("Dewpoint celsius", float(mySensor.dewpoint_celsius))
    temperature_celsius = Point(measurement_name).tag("location", location).field("Celsius", float(mySensor.temperature_celsius))
    #  Write to influxdb
    client = InfluxDBClient(url="http://influxdb:8086", token=influx_token, org=influx_org)
    write_api = client.write_api(write_options=SYNCHRONOUS)
    write_api.write(bucket=my_bucket, record=[humidity_level, pressure_level, dewpoint_celsius, temperature_celsius])
    # Control how often data is written
    client.close()
    sleep(600)

# Maybe impelment to keep the script running and bypass some exception errors if a docker container is restarted th handle some connection errors? 
# try:
#    ....
# except:
#    pass

