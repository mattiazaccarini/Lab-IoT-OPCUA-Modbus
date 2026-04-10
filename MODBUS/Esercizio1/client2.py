from pymodbus.client import ModbusTcpClient as ModbusClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.payload import BinaryPayloadDecoder
import time

# Setup Modus Client
print('Start Modbus Client')
client = ModbusClient(host='127.0.0.1', port=50001)

# Select the offset of the register to read/write
# Hint: it is the same used in the server to initialize the data store
# reg = -----

# ID of the modbus server to which the client will send the request
# address = -----


# Define the data to read from the server
# value_count = -----

# Read and print the data
#rd = ----- 
#print('Read: ', -----)

client.close()