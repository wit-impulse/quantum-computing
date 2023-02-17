# Necessary imports
import math

# Define a function to create a single qubit
def create_qubit():
    return [0, 1] # represents the |0> state

# Define a function to apply a NOT gate to a qubit
def apply_not(qubit):
    return [qubit[1], qubit[0]] # returns the |1> state

# Define a function to apply a Hadamard gate to a qubit
def apply_hadamard(qubit):
    return [(qubit[0] + qubit[1]) / math.sqrt(2), (qubit[0] - qubit[1]) / math.sqrt(2)]