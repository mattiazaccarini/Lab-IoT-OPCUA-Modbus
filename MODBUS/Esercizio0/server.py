from pymodbus.server import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext

def run_async_server():
    # server configuration
    port = 50000
    URL = 'localhost'
    address_ip = "127.0.0.1"

    # Registers configuration
    nreg = 200

    # Datastore initialization of the server corresponding to the server 
    # registers (respectively: discrete input, coils, holding register, 
    # input register)
    store = ModbusSlaveContext(
        di=ModbusSequentialDataBlock(0, [15]*nreg),
        co=ModbusSequentialDataBlock(0, [16]*nreg),
        hr=ModbusSequentialDataBlock(0, [17]*nreg),
        ir=ModbusSequentialDataBlock(0, [18]*nreg))
    context = ModbusServerContext(slaves=store, single=True)

    # Server identity configuration
    identity = ModbusDeviceIdentification()
    identity.VendorName = 'TestLab-IoT'
    identity.ProductCode = 'TestLab-IoT'
    identity.VendorUrl = ''
    identity.ProductName = 'Modbus Server'
    identity.ModelName = 'Modbus Server'
    identity.MajorMinorRevision = '3.0.2'


    # Start TCP Server
    print(f'Modbus server started on {URL} port {port}')
    StartTcpServer(context=context, host=URL, identity=identity, address=(address_ip, port))
    

if __name__ == "__main__":
    run_async_server()
    
    