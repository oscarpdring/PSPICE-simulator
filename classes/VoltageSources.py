import numpy as np
from itertools import count
from classes.Nodes import Nodes
# from lib.stamping_functions import stamp_y_sparse, stamp_j_sparse

class VoltageSources:
    def __init__(self, name, vp_node, vn_node, amp_ph_ph_rms, phase_deg, frequency_hz):
        self.name = name
        self.vp_node = vp_node
        self.vn_node = vn_node
        self.amp_ph_ph_rms = amp_ph_ph_rms
        self.phase_deg = phase_deg
        self.frequency_hz = frequency_hz
        # You are welcome to / may be required to add additional class variables   

    # Some suggested functions to implement, 
    def assign_node_indexes(self, node_counter, node_dict):
        self.vs_index = node_counter
        node_dict[self.name] = self.vs_index
        
    #from recitation
        if self.vp_node != "gnd":
            self.vp_node_index = node_dict[self.vp_node] # positive
        if self.vn_node != "gnd":
            self.vn_node_index = node_dict[self.vn_node] #negative 

        node_counter +=1
        return(node_counter)

        
        
    def stamp_sparse(self,):
        pass

    def stamp_dense(self,Y,J,t):

        #figure out time (vt)
        #declare my voltage source amplitude frquency and phase
        vt = np.cos(2*3.14*self.frequency_hz*t-self.phase_deg*180/3.14)*self.amp_ph_ph_rms*0.8165

        
        #ALWAYS USE +=!!!
        Y[self.vs_index, self.vp_node_index] += 1
        if self.vn_node != "gnd":
            Y[self.vs_index, self.vn_node_index] += 1

        J[self.vs_index] = vt

        Y[self.vp_node_index, self.vs_index] += 1
        if self.vn_node != "gnd":
            Y[self.vn_node_index, self.vs_index] +=1

    def stamp_open(self,):
        pass
        
