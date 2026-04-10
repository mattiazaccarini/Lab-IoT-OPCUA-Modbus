from pymodbus.client import ModbusTcpClient as ModbusClient
import struct

# Setup Modus Client
print('Start Modbus Client')
client = ModbusClient(host='127.0.0.1', port=50002)

# Registers to read/write 
#reg_1 = ------
#reg_2 = ------

# ID Modbus slave (server)
address=0

# Data to read
# If you want to manage floating point, modify the number of data to read for reg2 and handle the data returned by the server
# Hint for floating point: use the struct package
values_count_reg1 = 5
values_count_reg2 = 2 # --> 2 registers are needed to manage a floating point value

# Read data from the server registers
#rd_1 = -----
#rd_2 = -----

# Reconstruct the mean value in case of floating point
payload = struct.pack('HH', rd_2[0], rd_2[1])
mean = struct.unpack('f', payload)[0]

print('Read first registry', rd_1)
print('Read second registry', round(mean, 2))

# Chiusura del client
client.close()