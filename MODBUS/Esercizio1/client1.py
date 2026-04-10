from pymodbus.client import ModbusTcpClient as ModbusClient

# Setup Modus Client
print('Start Modbus Client')
client = ModbusClient(host='127.0.0.1', port=50001)
client.connect()

# Read / Write configuration
reg=10

# ID of the server to which the client will send the request
address=0

# Data to write on the server
data = [31,32,33,34,35]

# Writing data on the server (40001 to 40005)
print('Write',data)

# Writing the data to the holdings register
result  = client.write_registers(address=reg, values=data, slave=address)

# Closing the connection with the server
client.close()