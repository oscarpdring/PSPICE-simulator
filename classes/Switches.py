import numpy as np
from itertools import count
from classes.Nodes import Nodes
# from lib.stamping_functions import stamp_y_sparse, stamp_j_sparse
import pickle

class Switches:
    def __init__(self, name, from_node, to_node, t_open, t_close):
        self.name = name
        self.from_node = from_node
        self.to_node = to_node
        self.t_open = t_open
        self.t_close = t_close
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

        #going to need to do a case for when the switch is open
        #when switch is open, very very large resistor in its place?
        if self.from_node != "gnd":
            Y[self.from_node_idx, self.from_node_idx] += 1/self.r

        if self.to_node != "gnd": 
            Y[self.from_node_idx, self.to_node_idx] += -1/self.r
            Y[self.to_node_idx, self.from_node_idx] += -1/self.r
            Y[self.to_node_idx, self.to_node_idx] += 1/self.r



    # going to need to do a case for when the switch is close
    #when switch is closed very small resistor in its place?

    def stamp_open(self,):
        pass