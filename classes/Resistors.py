import numpy as np
from itertools import count
from classes.Nodes import Nodes
#from lib.stamping_functions import stamp_y_sparse, stamp_j_sparse


class Resistors:
    def __init__(self, name, from_node, to_node, r):
        self.name = name
        self.from_node = from_node
        self.to_node = to_node
        self.r = r

        # You are welcome to / may be required to add additional class variables   

    # Some suggested functions to implement, 
    def assign_node_indexes(self,node_dict):
        if self.from_node != "gnd":
            self.from_node_idx = node_dict[self.from_node]
        if self.to_node != "gnd":
            self.to_node_idx = node_dict[self.to_node]
            
    def stamp_sparse(self,):
        pass

    def stamp_dense(self,Y):
        if self.from_node != "gnd":
            Y[self.from_node_idx, self.from_node_idx] += 1/self.r

        if self.to_node != "gnd": 
            Y[self.from_node_idx, self.to_node_idx] += -1/self.r
            Y[self.to_node_idx, self.from_node_idx] += -1/self.r
            Y[self.to_node_idx, self.to_node_idx] += 1/self.r
        
        pass