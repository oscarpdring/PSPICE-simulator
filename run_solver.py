from solve import *

# path to the grid network RAW file

casename ='code/testcases/RL_circuit.json'

#casename = 'code/testcases/single_phase_RL_circuit.json'

#casename = 'code/testcases/single_phase_R_circuit.json'

#casename = 'code/testcases/single_phase_RC_circuit.json'

#single_phase_

# the settings for the solver
settings = {
	"Tolerance": 1E-05, # Tolerance for Newton-Raphson
	"Max Iters": 5, # Maximum number of newton iterations for non-linear loop at given time step
    "Delta_t": 1E-04, # step time for the simulations
    "Simulation Time": 0.2, # Total time to simulate: [0, tf]
    "Sparse": False # Use sparse matrix formulation
}

# run the solver
solve(casename, settings)