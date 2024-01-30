import numpy as np
from itertools import count
from classes.Nodes import Nodes
#from lib.stamping_functions import stamp_y_sparse, stamp_j_sparse

class Capacitors:
    def __init__(self, name, from_node, to_node, c):
        self.name = name
        self.c = c
        self.from_node = from_node
        self.to_node = to_node
        # You are welcome to / may be required to add additional class variables   

    # Some suggested functions to implement, 
    def assign_node_indexes(self,node_counter,node_dict):
        if self.from_node != "gnd":
            self.from_node_idx = node_dict[self.from_node]
        if self.to_node != "gnd":
            self.to_node_idx = node_dict[self.to_node]


        #creating an auxilary node for the voltage source
        self.capacitor_index = node_counter
        node_dict[self.name] = self.capacitor_index
        node_counter +=1
        self.aux_cap_index = node_counter
        node_dict['Cap_Aux'] = self.aux_cap_index
        node_counter +=1
        print(node_counter)
        return(node_counter)
        
    def stamp_sparse(self,):
        pass

    def stamp_dense(self,Y,J,delta_t,Vbefore):


        if self.to_node != 'gnd':
            vt = Vbefore[self.from_node_idx]-Vbefore[self.to_node_idx]
        else:
            vt = Vbefore[self.from_node_idx]

        R = delta_t/(2*self.c)
        V = Vbefore[self.aux_cap_index]*R+vt


    #stamp resistor in companion model for the capacitor
        Y[self.capacitor_index, self.capacitor_index] += R

        if self.to_node != "gnd": 
            Y[self.capacitor_index, self.to_node_idx] += -R
            Y[self.to_node_idx, self.capacitor_index] += -R
            Y[self.to_node_idx, self.to_node_idx] += R

    #stamping current thru the aux voltage source

        J[self.capacitor_index] =  -V
        if self.to_node != "gnd":
            J[self.to_node_idx] =  V
  

 #stamp aux voltage source
#aux = vs , vp = self cap , vn = to

       
        Y[self.aux_cap_index, self.from_node_idx] += 1
        Y[self.aux_cap_index, self.capacitor_index] += -1
        Y[self.from_node_idx, self.aux_cap_index] += 1
        Y[self.capacitor_index, self.aux_cap_index] += -1

        J[self.aux_cap_index,] = 0


    def stamp_open(self,):
        pass