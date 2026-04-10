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

    # Objects and Variables setup
    macchinaL1 = objects.add_object(idx, "Linea1")
    varmL1 = macchinaL1.add_variable(idx, "varL1", 0)

    varmL1.set_writable()    

    # Create a new object and variable for Linea2 
    # --------------------------------------
     
    # Association of the new variable to the new object with a value of 100
    # ---------------------------------------

    # Set the variable to be writable
    # ---------------------------------------

    # Print of the objects and variables for Linea1
    print('-------------------------')
    print("Object node is ", objects)
    print("Linea1 ", macchinaL1)
    print("varL1  ", varmL1)
    # Print of the new object and variable for Linea2
    print('-------------------------')
    # ---------------------------------------

    server.start()

    try:
        while True:
            time.sleep(1)
            # Retrieval of the value of the variable and increment of 1
            tempL1 = varmL1.get_value()
            
            tempL1 += 1

            # Update of the variable with the new value
            varmL1.set_value(tempL1)

            print("L1 updated value: ", tempL1)

            # Decrement of the value of varL2 by 1
            # ---------------------------------------

            # Update of varL2 with the new value
            # ---------------------------------------



            

    finally:
        server.stop()