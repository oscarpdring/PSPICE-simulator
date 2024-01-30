import matplotlib.pyplot as plt
import numpy as np


def process_results(V_waveform, devices,node_dict):

   # # # Unpack parsed device objects in case you need them # # #
    #create list of all the elements in the json file 
    nodes = devices['nodes']
    voltage_sources = devices['voltage_sources']
    resistors = devices['resistors']
    capacitors = devices['capacitors']
    inductors = devices['inductors']
    switches = devices['switches']
    induction_motors = devices['induction_motors']


   #grab all the rows from the dictionary relevent to the voltage i am seeking to plot 
    #create list of all the elements in the json file
    V2_a = V_waveform [node_dict["n3_a"],:]
    V2_b = V_waveform [node_dict["n3_b"],:]
    V2_c = V_waveform [node_dict["n3_c"],:]

    t = np.linspace(0,0.2,len(V2_a))


    plt.close('all')

#     # print(V_waveform)

    plt.title('Node Voltages Three Phase RL')
    plt.xlabel("Time")
    plt.ylabel("Voltage(V)")

    plt.plot(t,V2_a,color='blue', linewidth = 1,  label = 'V2_a')
    plt.plot(t,V2_b,color='red', linewidth = 1,  label = 'V2_b')
    plt.plot(t,V2_c,color='green', linewidth = 1,  label = 'V2_c')

    plt.legend(loc='upper right')
    plt.show()

# code for the current plots 

    plt.title('Node Currents Three Phase RL')

    plt.xlabel("Time")
    plt.ylabel("Current(A)")

#pulling the indexs of the inductors as they are added to the V_Waveform matrix so they can be plotted 
    i = 0
    while i < len(inductors):
        l1 = inductors[i]
        if l1.name == "l2_a":
            i1 = V_waveform[l1.aux_index,:]
            plt.plot(t,i1,color='blue', linewidth = 1,  label = 'I2_a')
        elif l1.name == "l2_b":
            i2 = V_waveform[l1.aux_index,:]
            plt.plot(t,i2,color='red', linewidth = 1,  label = 'I2_b')
        elif l1.name == "l2_c":
            i3 = V_waveform[l1.aux_index,:]
            plt.plot(t,i3,color='green', linewidth = 1,  label = 'I2_c')
        i += 1

    plt.legend()
    plt.show()






# plotting code for the RL single phase circuit
    
    # current_row = V_waveform[2,:]
    # plt.subplot(3,1,1)
    # first_row = V_waveform [0,:]
    # second_row = V_waveform [1,:]

    # t = np.linspace(0,0.2,len(first_row))

    # plt.plot(t, first_row)
    # plt.title('Node V1 Voltage')
    # plt.xlabel("Time")
    # plt.ylabel("Voltage")

    # plt.subplot(3,1,2)

    # plt.plot(t, second_row)
    # plt.title('Node V2 Voltage')
    # plt.xlabel("Time")
    # plt.ylabel("Voltage2")


    # plt.subplot(3,1,3)
    # plt.plot(t, current_row)
    # plt.title('Node V2 Current')
    # plt.xlabel("Time")
    # plt.ylabel("Current")

    # plt.show()


    ##show code for single phase R 


    # plt.plot(t,first_row,label = "Node 1 (V)")
    # plt.plot(t,second_row,label = "Node 2 (V)")
    # plt.plot(t, current_row, label = "Current at node 1 (A)")
    # plt.ylabel("Magnitude")
    # plt.xlabel("Time")
    # plt.legend()