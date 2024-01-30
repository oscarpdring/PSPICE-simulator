import sys
sys.path.append("..")
import numpy as np
from itertools import count
from classes.Nodes import Nodes
# from lib.stamping_functions import stamp_y_sparse, stamp_j_sparse

class Inductors:
    def __init__(self, name, from_node, to_node, l):
        self.name = name
        self.from_node = from_node
        self.to_node = to_node
        self.l = l  
        # You are welcome to / may be required to add additional class variables   

    # Some suggested functions to implement, 
    def assign_node_indexes(self, node_counter, node_dict):
        if self.from_node != "gnd":
            self.from_node_idx = node_dict[self.from_node]
        if self.to_node != "gnd":
            self.to_node_idx = node_dict[self.to_node]

#creating an auxilary node for the voltage source
        self.inductor_index = node_counter
        node_dict[self.name] = self.inductor_index
        node_counter +=1
        self.aux_index = node_counter
        node_dict['Ind_Aux'] = self.aux_index
        node_counter +=1
        print(node_counter)
        return(node_counter)
        

    def stamp_sparse(self,):
        pass

    def stamp_dense(self,Y,J,delta_t,Vbefore):


#measuring the voltgae across the inductor instead of the node voltgae at the inductor terminal
#useful when running the three phase json file
        if self.to_node != 'gnd':
            vt = Vbefore[self.from_node_idx]-Vbefore[self.to_node_idx]
        else:
            vt = Vbefore[self.from_node_idx]

        G = delta_t/(2*self.l)
        I = Vbefore[self.aux_index]+G*vt


    
    #stamp conductance
        Y[self.inductor_index, self.inductor_index] += G

        if self.to_node != "gnd": 
            Y[self.inductor_index, self.to_node_idx] += -G
            Y[self.to_node_idx, self.inductor_index] += -G
            Y[self.to_node_idx, self.to_node_idx] += G
        
        #stamping current thru the aux voltage source

        J[self.inductor_index] =  -I
        if self.to_node != "gnd":
            J[self.to_node_idx] =  I
  

      #stamp aux voltage source
#aux = vs , vp = from , vn = self inductor

       
        Y[self.aux_index, self.from_node_idx] += 1
        Y[self.aux_index, self.inductor_index] += -1
        Y[self.from_node_idx, self.aux_index] += 1
        Y[self.inductor_index, self.aux_index] += -1

        J[self.aux_index,] = 0



        pass

    def stamp_short(self,):
        pass