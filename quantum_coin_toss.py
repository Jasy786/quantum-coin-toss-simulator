from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Create a quantum circuit
qc = QuantumCircuit(1, 1)

# Put qubit into superposition
qc.h(0)

# Measure qubit
qc.measure(0, 0)

# Run simulation
simulator = AerSimulator()
job = simulator.run(qc, shots=1000)
result = job.result()

# Get result
counts = result.get_counts()

print("Quantum Coin Toss Result:")
print(counts)