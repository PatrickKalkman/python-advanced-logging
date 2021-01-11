import socket
import struct

with open('dynamic_log_new.config', 'rb') as logging_config:
    configuration_data = logging_config.read()

config_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
config_socket.connect(('localhost', 9000))
config_socket.send(struct.pack('>L', len(configuration_data)))
config_socket.send(configuration_data)
config_socket.close()
