import time
from opcua import ua, Server


if __name__ == "__main__":

    #Server setup
    server = Server()
    server.set_endpoint("opc.tcp://localhost:4840")

    #Namespace Setup
    uri = "OPCUA_SERVER"
    idx = server.register_namespace(uri)

    #Objects Node
    objects = server.get_objects_node()

    # Step 1 - Association of objects and variables to the server
    # Objects and variables are created as nodes in the server's address space.
    macchinaL1 = objects.add_object(idx, "Linea1")
    varmL1 = macchinaL1.add_variable(idx, "varL1", 0)
    # Set the variable as writable by the client
    varmL1.set_writable()    

    # Step 2 - Processing
    print('-------------------------')
    print("Object node is ", objects)
    print("Linea1 ", macchinaL1)
    print("varL1  ", varmL1)
    print('-------------------------')
    

    server.start()

    try:
        while True:
            time.sleep(1)
            # Read the value of the variable
            tempL1 = varmL1.get_value()
            
            tempL1 += 1

            # Write the value of the variable
            varmL1.set_value(tempL1)

            print("Valore L1: ", tempL1)
            

    finally:
        server.stop()