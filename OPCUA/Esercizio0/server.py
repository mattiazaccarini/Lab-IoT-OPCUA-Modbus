import time
from opcua import ua, Server


if __name__ == "__main__":

    # Server setup
    server = Server()
    server.set_endpoint("opc.tcp://localhost:4840")

    # Namespace Setup
    uri = "OPCUA_SERVER" # Namespace definition
    # Namespace registration, returns the index 
    # of the namespace, which is used to create nodes in that namespace
    idx = server.register_namespace(uri) 
    # Objects Node
    objects = server.get_objects_node()

    # Step 1 - Association of objects and variables to the server
    # Objects and variables are created as nodes in the 
    # server's address space.

    # Association of the object Linea1 to the server, 
    # and association of the variable varL1 to the object Linea1
    macchinaL1 = objects.add_object(idx, "Linea1")      # Linea1 initialization, specifying namespace and name
    varmL1 = macchinaL1.add_variable(idx, "varL1", 0)   # Variable initialization, specifying namespace, name and initial value (0)
    
    # Set the variable as writable by the client
    varmL1.set_writable()    

    # Step 2 - Processing

    # Simulate the processing of the machine, 
    # incrementing the variable by 1 on each cycle
    # Print the IDs of the nodes created in the server
    print('-------------------------')
    print("Object node is ", objects)
    print("Linea1 ", macchinaL1)
    print("varL1  ", varmL1)
    print('-------------------------')
    

    server.start()

    try:
        while True:
            # Read the value of the variable
            tempL1 = varmL1.get_value()
            
            tempL1 += 1

            # Write the value of the variable
            varmL1.set_value(tempL1)

            print("L1 current value: ", tempL1)
            
            # sleep for 1 second before the next cycle
            time.sleep(1)
            

    finally:
        server.stop()