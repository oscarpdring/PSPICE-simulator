
#this function will assign inducies 
def assign_node_indexes(devices,node_dict):
    #making a counter to irrate the indexs
    node_index_counter = 0
    
    

   # # # Unpack parsed device objects in case you need them # # #
    #create list of all the elements in the json file
    nodes = devices['nodes']
    voltage_sources = devices['voltage_sources']
    resistors = devices['resistors']
    capacitors = devices['capacitors']
    inductors = devices['inductors']
    switches = devices['switches']
    induction_motors = devices['induction_motors']


    print(nodes)

#each node is assigned an index
    for node in nodes:
        if node.name != "gnd":
            #calling the fuction in "nodes"
            node_index_counter = node.assign_index_in_nodes(node_index_counter, node_dict)

    for node in nodes:
        if node.name != "gnd":
            print("Node name is %s and node index is %g" %(node.name, node_dict[node.name]))
        
        #print("Node name is %g and node index is %g" %(resistor.from_node, resistor))

#resistor needs the index, it does not assign the index
    for resistor in resistors:
        resistor.assign_node_indexes(node_dict)

        if node.name != "gnd":
            print("resistor from node name is %s and from node indec is %g" % (resistor.from_node, resistor.from_node_index))
        if node.name != "gnd":
            print("resistor to node name is %s and to node indec is %g" % (resistor.to_node, resistor.to_node_index))
            
            
            print(resistor.from_node, node_dict[resistor.from_node])
            print(resistor.to_node, node_dict[resistor.from_node_index])

#voltage sources
    for vs in voltage_sources:
    #vs.assign_indices_in_vs(node_dict)
        node_index_counter = vs.assign_node_indexes(node_index_counter, node_dict)


#inductor needs te index, but may also assign an index
    for inductor in inductors:
        node_index_counter = inductor.assign_node_indexes(node_index_counter, node_dict)
    print(node_dict)
    return( node_index_counter)


