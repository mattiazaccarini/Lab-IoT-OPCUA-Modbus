import time
from opcua import Client

'''
 Client for connecting to the OPC UA server and sending commands to control the machine. 
 The client connects to the server, retrieves the variable varL1 and calls the method controls to stop the machine.
'''

if __name__ == "__main__":
    #Client setup
    client = Client("opc.tcp://localhost:4840")
    try:
        client.connect()

        # Read the root node and print its children
        root = client.get_root_node()
        print("Root node is: ", root)

        print("Children of root are: ", root.get_children())

        objects = root.get_child(["0:Objects"])
        print("Children of Objects are ", objects.get_children())

        # Retrieve the nodes of Linea1 and varL1 using their path
        macchinaL1 = root.get_child(["0:Objects", "2:Linea1"])
        varmL1 = root.get_child(["0:Objects", "2:Linea1", "2:varL1"])
        
        print("Linea1: ", macchinaL1)
        print("varL1: ", varmL1)
        
        print(varmL1.get_value())

        
        uri= "OPCUA_SERVER"
        idx= client.get_namespace_index(uri)

        res= objects.call_method("{}:controls".format(idx), "Stop") # Call the method controls with the argument "Stop" to stop the machine
        print("Method result is: ", res) 
        time.sleep(5)
        res= objects.call_method("{}:controls".format(idx), "Start") # Call the method controls with the argument "Start" to start the machine
        print("Method result is: ", res)


    finally:
        client.disconnect()