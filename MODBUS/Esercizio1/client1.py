from pymodbus.client import ModbusTcpClient as ModbusClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.payload import BinaryPayloadDecoder
import time

# Setup Modus Client
print('Start Modbus Client')
client = ModbusClient(host='127.0.0.1', port=50001)

# Read / Write configuration
reg=10

# ID of the server to which the client will send the request
address=0

# Data to write on the server
data = [31,32,33,34,3]

# Writing data on the server (40001 to 40005)
print('Write',data)
builder = BinaryPayloadBuilder(byteorder=Endian.BIG, wordorder=Endian.LITTLE)

# Building the payload in 16-bit format
for d in data:
    builder.add_16bit_int(int(d))
payload = builder.build()

# Writing the data to the holdings register
result  = client.write_registers(int(reg), payload, skip_encode=True, unit=int(address))

# Closing the connection with the server
client.close()