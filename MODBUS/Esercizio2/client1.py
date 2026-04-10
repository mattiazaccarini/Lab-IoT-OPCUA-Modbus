from pymodbus.client import ModbusTcpClient as ModbusClient

# Setup Modus Client
print('Start Modbus Client')
client = ModbusClient(host='127.0.0.1', port=50002)

# Read / Write configuration
reg=50

# ID Modbus slave (server) 
address=0

# Data to write on the server registers
data = [101, 252, 300, 403, 500]

# Writing data on the server registers
print('Write', data)
result  = client.write_registers(address=reg, values=data, slave=address)

# Chiusura della comunicazione
client.close()