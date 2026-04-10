from pymodbus.client import ModbusTcpClient as ModbusClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.payload import BinaryPayloadDecoder
import time

# Setup Modus Client
print('Start Modbus Client')
client = ModbusClient(host='127.0.0.1', port=50000)

# Coordinate di lettura / scrittura
# Read/Write address of the holding register
reg=0

# Modbus server unit identifier (slave id)
address=0

# Data to write on the holding register
data = [1,2,3,4,5]

# Writing data on the holding register
print('Write', data)

# Configuration of the builder for the payload 
# to write on the holding register
builder = BinaryPayloadBuilder(byteorder=Endian.BIG, wordorder=Endian.LITTLE)

# Payload building considering a 16 bit codification 
# of the data to write on the holding register
for d in data:
    builder.add_16bit_int(int(d))
payload = builder.build()

# Writing the data on the holding register
# skip_encode=True --> data already correctly encoded through the builder, 
# so it is not necessary to encode it again
result  = client.write_registers(int(reg), payload, skip_encode=True, unit=int(address))

# Reading the registers
numero_dati_da_leggere = 5
rd = client.read_holding_registers(reg, numero_dati_da_leggere).registers
print('Read', rd)

# Close the client connection
client.close()