from opcua import Client

if __name__ == "__main__":
    #Client setup
    client = Client("opc.tcp://localhost:4840")
    try:
        client.connect()

        # Retrieval of the root node and print
        root = client.get_root_node()
        print("Root node is: ", root)

        
        print("Children of root are: ", root.get_children())

        objects = root.get_child(["0:Objects"])

        print("Children of Objects are ", objects.get_children())


        # Retrieval of the elements via navigation of the Address Space
        macchinaL1 = root.get_child(["0:Objects", "2:Linea1"])
        varmL1 = root.get_child(["0:Objects", "2:Linea1", "2:varL1"])
       
        # Retrieval of the object "Linea2" and its variable "varL2"
        # ------------------------

        # Print of the retrieved elements
        print("Linea1: ", macchinaL1)
        print("varL1:  ", varmL1)
        
        # Print of the retrieved object "Linea2" and its variable "varL2"
        print('-------------------------')
        # ------------------------- 
        
        # Print of L1 variable value
        print("L1 Updated Value: ", varmL1.get_value())

        # Print of Linea2 variable value
        # ---------------------------------------

    finally:
        client.disconnect()