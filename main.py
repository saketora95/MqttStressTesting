import paho.mqtt.client as mqtt
import config_reader
import datetime
import json
import time

# ----- ----- ----- ----- -----

DATETIMEFORMAT = '%y-%m-%d %H:%M:%S'

program_config = config_reader.load_config('config.txt')
print(f"Config: {program_config}")

# ----- ----- ----- ----- -----

def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected {reason_code}")


mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqtt_client.on_connect = on_connect
mqtt_client.username_pw_set(program_config['USERNAME'], program_config['PASSWORD'])

mqtt_client.connect(program_config['HOST'], program_config['PORT'], 60)

test_count = 1
while test_count <= program_config['TESTCOUNT']:
    message_payload = {
        'datetime': datetime.datetime.now().strftime(DATETIMEFORMAT),
        'count': test_count,
        'params': {
            'stream': 'DI',
            'type': 'bool',
            'data': True
        }
    }
    mqtt_client.publish(program_config['TESTTOPIC'], json.dumps(message_payload), qos=2)

    message_payload['params']['data'] = False
    mqtt_client.publish(program_config['TESTTOPIC'], json.dumps(message_payload), qos=2)

    test_count += 1
    if test_count % 100 == 0:
        print(f"{test_count} / {program_config['TESTCOUNT']}")

mqtt_client.loop_forever()