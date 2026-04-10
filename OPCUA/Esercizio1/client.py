from opcua import Client

if __name__ == "__main__":
    #Client setup
    client = Client("opc.tcp://localhost:4840")
    try:
        client.connect()

        # Read the Root node and print its children
        root = client.get_root_node()
        print("Root node is: ", root)

        
        print("Children of root are: ", root.get_children())

        # Read the Objects node and print its children
        objects = root.get_child(["0:Objects"])

        print("Children of Objects are ", objects.get_children())


        # Read the variable node and print its value through its path 
        # in the address space
        macchinaL1 = root.get_child(["0:Objects", "2:Linea1"])
        varmL1 = root.get_child(["0:Objects", "2:Linea1", "2:varL1"])
        
        print("Linea1: ", macchinaL1)
        print("varL1: ", varmL1)
        
        # Read the value of the variable before writing
        print("Value before writing: ", varmL1.get_value())

        # Write a new value to the variable
        # -----------------------------

        # Print the value of the variable after writing
        # -----------------------------


    finally:
        client.disconnect()