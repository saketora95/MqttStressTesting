import paho.mqtt.client as mqtt
import config_reader

# ----- ----- ----- ----- -----

program_config = config_reader.load_config('config.txt')
print(program_config)