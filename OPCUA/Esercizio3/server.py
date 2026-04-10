import time
from opcua import ua, Server, uamethod

check = True

def move():
    global check
    check = True

# Method to stop the machine, setting the global variable check to False
def stop():
    global check
    check = False

# Method to control the machine, it receives a string as input and returns a string as output
@uamethod
def controls(parent, x):    
    
    msg = "Invalid command"  # default message in case of invalid command

    if x == "Stop":
        stop()              # stop the machine by setting check to False
        msg = "Machine stopped"     # set the return message

    if x == "Start":
        move()
        msg = "Machine started"   # set the return message

    return msg

if __name__ == "__main__":

    #Server setup
    server = Server()
    server.set_endpoint("opc.tcp://localhost:4840")

    #Namespace Setup
    uri = "OPCUA_SERVER"
    idx = server.register_namespace(uri)

    #Objects Node
    objects = server.get_objects_node()

    # Add a new object to the server, called Linea1, and a variable varL1 to the object Linea1
    macchinaL1 = objects.add_object(idx, "Linea1")
    varmL1 = macchinaL1.add_variable(idx, "varL1", 0)
    
    varmL1.set_writable()    

    print('-------------------------')
    print("Object node is ", objects)
    print("Linea1 ", macchinaL1)
    print("varL1  ", varmL1)
    print('-------------------------')
    
    # Definition of the method arguments
    inarg= ua.Argument()
    inarg.Name= "Input"                                 # Name of the argument
    inarg.DataType= ua.NodeId(ua.ObjectIds.String)      # Data type of the argument
    inarg.ValueRank= -1
    inarg.ArrayDimensions= []
    inarg.Description= ua.LocalizedText("Command")      # Description of the argument

    outarg= ua.Argument()
    outarg.Name= "Output"
    outarg.DataType= ua.NodeId(ua.ObjectIds.String)
    outarg.ValueRank= -1
    outarg.ArrayDimensions= []
    outarg.Description= ua.LocalizedText("Message")

    # Istanzio l’oggetto metodo controls
    multiply_node = objects.add_method(idx, "controls", controls, [inarg], [outarg]) # Creo il metodo controls passando gli argomenti in input (inarg) e in output (outarg)
                                                                                     # idx è il namespace 

    server.start()

    try:
        while True:
            while check:
                time.sleep(1)
                # Read the value of the variable varL1
                tempL1 = varmL1.get_value()
                
                tempL1 += 1

                # Write the new value on the variable varL1
                varmL1.set_value(tempL1)

                print("Value L1: ", tempL1)
            

    finally:
        server.stop()