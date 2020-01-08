IP="127.0.0.1"
ACCESS_TOKEN=Ck4j1XdmAqeDm7gtSbjB
FILE="telemetry-data.json"

mosquitto_pub -d -h $IP -t "v1/devices/me/telemetry" -u "$ACCESS_TOKEN" -f $FILE