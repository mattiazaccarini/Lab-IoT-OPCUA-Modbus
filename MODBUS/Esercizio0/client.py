from pymodbus.client import ModbusTcpClient as ModbusClient

# Setup Modus Client
print('Start Modbus Client')
client = ModbusClient(host='127.0.0.1', port=50000)
client.connect()

# Read/Write address of the holding register
reg=0

# Modbus server unit identifier (slave id)
address=0

# Data to write on the holding register
data = [1,2,3,4,5]

# Writing data on the holding register
print('Write', data)
result  = client.write_registers(address=reg, values=data, slave=address)

# Reading the registers
values_count = 5
rd = client.read_holding_registers(address=reg, count=values_count, slave=address).registers
print('Read: ', rd)

# Close the client connection
client.close()