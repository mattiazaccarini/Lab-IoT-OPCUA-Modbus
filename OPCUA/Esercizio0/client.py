from opcua import Client

if __name__ == "__main__":
    url_server = "opc.tcp://localhost:4840"
    # Client setup
    client = Client(url_server)
    try:
        client.connect()

        # Step 3 - Read
        # The Client navigates within the namespace, retrieves the Root node 
        # within the server, its children and within the Objects node 
        # retrieves Linea1 (which will be associated with the machine) 
        # and varL1 (which will be the machine's variable)
       
        # Retrieval of the root node
        root = client.get_root_node()
        print("Root node is: ", root)

        
        print("Children of root are: ", root.get_children()) # Retrieval of the children of the root node, namely Objects, Types and Views

        # An object can be retrieved by specifying its name or its identifier
        objects = root.get_child(["0:Objects"]) # Retrieval of the Objects object
                                                # 0: indicates the namespace
        
        print("Children of Objects are ", objects.get_children()) # Retrieval of the children of the Objects object
                                                                  # The children are Server and Linea1


        # Retrieval of the elements through navigation of the Address Space
        # And storing them in variables
        macchinaL1 = root.get_child(["0:Objects", "2:Linea1"])          # Retrieval of the Linea1 object from Objects 
                                                                        # Linea1 is in namespace 2
        varmL1 = root.get_child(["0:Objects", "2:Linea1", "2:varL1"])   # Retrieval of the varL1 variable from Linea1 of Objects
                                                                        # varL1 is in namespace 2 (same namespace as Linea1)
        # Print of the nodes retrieved
        print("Linea1: ", macchinaL1)
        print("varL1:  ", varmL1)
        
        # Print of the value of varL1
        print(varmL1.get_value())


    finally:
        client.disconnect()