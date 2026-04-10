from pymodbus.client import ModbusTcpClient as ModbusClient
import struct

# Setup Modus Client
print('Start Modbus Client')
client = ModbusClient(host='127.0.0.1', port=50002)

# Define the registers to read/write
# Hint: register 1 should be the one used for the write operation
#reg_1 = -----
#reg_2 = -----

# ID Modbus slave (server)
address=0

# Amount of data to read/write
values_count = 5

# Read data from the server registers
# -------------------------------

# Compute the mean of the read values
# -------------------------------

# Manage the case of floating point value
# -------------------------------


# Write the mean value on the server registers
# -------------------------------

client.close()