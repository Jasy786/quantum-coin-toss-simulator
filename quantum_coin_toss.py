from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

qc = QuantumCircuit(1, 1)

qc.h(0)
qc.measure(0, 0)

simulator = AerSimulator()
result = simulator.run(qc, shots=1000).result()

counts = result.get_counts()

print("Quantum Coin Toss Result:")
print(counts)

fig = plot_histogram(counts)
plt.show(block=True)