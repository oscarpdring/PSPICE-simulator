import numpy as np

def run_time_domain_simulation(devices, V_init, size_Y, SETTINGS):
    V_waveform = np.copy(V_init)
    #need to state start time of simulation 
    t = 0
    Vbefore = np.copy(V_init)

#all the classes I would ever need
    nodes = devices['nodes']
    voltage_sources = devices['voltage_sources']
    resistors = devices['resistors']
    capacitors = devices['capacitors']
    inductors = devices['inductors']
    switches = devices['switches']
    induction_motors = devices['induction_motors']

    t_final = SETTINGS['Simulation Time']
    delta_t = SETTINGS['Delta_t'] # time steps 


    
    while t <= t_final:
        Y= np.zeros([size_Y,size_Y], dtype = float)
        J= np.zeros(((size_Y,1)), dtype = float)
        #make time happen by going forwards : )

        t += delta_t

            #bring on da parts bc its a party up in here

            #calling the resistors stamped
        for R in resistors: 
                R.stamp_dense(Y)
                
        #calling the voltage sources stamped
        for Vs in voltage_sources:
            Vs.stamp_dense(Y,J,t)

            
            
            #calling the inductors stamped
        for L in inductors:
            L.stamp_dense(Y,J,delta_t,Vbefore)


        #compute the exact solution of x, the well determined matrix, full rank, linear matrix equation ax=b
        run = np.linalg.solve(Y,J)
        #save the previous time step into memory
        Vbefore = np.copy(run)
        
        V_waveform = np.concatenate((V_waveform,run),axis = 1)

    
    return V_waveform
