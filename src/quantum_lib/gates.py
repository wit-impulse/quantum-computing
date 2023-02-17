# Necessary imports
import numpy as np

# Define a function to create a CNOT gate
def create_cnot():
    return [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]

# Define a function to create a SWAP gate
def create_swap():
    return [[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]]

# Define a function to apply a gate to a set of qubits
def apply_gate(gate, qubits):
    return np.dot(gate, qubits)
