# Home network project with environmental senors

Built on Raspberry Pi 4 with the [SparkFun Environmental Combo Breakout - CCS811/BME280 (Qwiic)](https://github.com/sparkfun/Qwiic_BME280_CCS811_Combo) on Python.

Using [Balena.io](http://balena.io/) who provide a full technology stack develop, deploy, and manage projects at any scale; all on the cloud.

Pihole + unbound copied from [klutchell](https://github.com/klutchell/balena-pihole).

pHAT Shutown button copied from [sparkfun reboot and shutdown guide](https://learn.sparkfun.com/tutorials/raspberry-pi-safe-reboot-and-shutdown-button/all).

## Setup on Balena for service variables/environmental variables

Device Service Variables used for this repo that would need to be added to the Balena Cloud Dashboard under the service sensor for individual devices.

DEVICE_DB_LOCATION = The device location
INFLUX_DB_BUCKET = The bucket name for Influx DB
INFLUX_DB_TOKEN = Token generated from Influx DB. More infomration can be found at [InfluxDB's documentation](https://docs.influxdata.com/influxdb/v2.0/security/tokens/)
INFLUX_DB_ORG = The organisation ID for your bucket

Sensor uses Python and [influxdb-client-python](https://github.com/influxdata/influxdb-client-python) libaries to write into influxdb.

## Setup of initial persistant InfluxDB database and users

Setup details can be found [here](https://docs.influxdata.com/influxdb/v2.0/reference/cli/influx/setup/) and the easiest way is to open up the influxdb url @ http://deviceip:8086 and follow the intial setup prompts.

Alternatively on the Balena dashboard, open up th CLI for influx db and type in:

influx setup 

Press enter and follow the instructions. Make note of the details as they will be used next.

## Setup of scripts for the sensor

The bucket & org would be entered into the Device Service Variable in your balena machine.

On the Balena dashboard under device service variables, please input the following enviromental variables

INFLUX_DB_BUCKET: ${Your influxdb bucket that was setup}
INFLUX_DB_TOKEN: ${Your influxdb token. Used to upload data from the scripts} Instructions found [here](https://docs.influxdata.com/influxdb/cloud/security/tokens/create-token/)
INFLUX_DB_ORG: ${Your influxdb organisation name}
DEVICE_DB_LOCATION: ${Used as a flag for your device on influxdb to filter by location}

Alterinatively you can go into the Python scripts and hardcode these values in directly.

Scripts needed are:

    - bme280.py
    - ccs811.py
    - weather_bom.py

Finally under weather_bom.py / BOMURL please point the URL to your local data feed under [Observations - Individual Stations](http://www.bom.gov.au/catalogue/data-feeds.shtml) as these feeds provide the necessary .json files which this is written in to accept.

## Setup of Grafana

A template dashboard will be in place with some of the datapoints. Follow the [instructions here](https://grafana.com/docs/grafana/latest/datasources/influxdb/) to connect Grafana to Influx DB via Flux.