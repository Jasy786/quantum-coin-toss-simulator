\# Quantum Coin Toss Simulator



\## Overview



This project demonstrates a basic quantum computing application using Qiskit. A single qubit is placed into a superposition state using the Hadamard gate and then measured repeatedly to simulate a fair quantum coin toss.



The project introduces fundamental quantum computing concepts including qubits, superposition, measurement, and quantum circuit simulation.



\---



\## Objective



The objective of this project is to:



\* Understand quantum bits (qubits)

\* Explore quantum superposition

\* Simulate a fair quantum coin toss

\* Learn Qiskit circuit creation and execution

\* Visualize quantum measurement outcomes



\---



\## Theory



In classical computing, a coin is either Heads or Tails.



In quantum computing, a qubit can exist in a superposition of both states simultaneously.



The Hadamard gate transforms the initial state into a superposition:



|0⟩ → (|0⟩ + |1⟩)/√2



When measured, the qubit collapses to:



\* 0 (Heads)

\* 1 (Tails)



with approximately equal probability.



\---



\## Quantum Circuit



The following circuit places a qubit into superposition using a Hadamard gate and then performs a measurement.



!\[Quantum Circuit](circuit.png)



\---



\## Implementation



\### Technologies Used



\* Python

\* Qiskit

\* Qiskit Aer

\* Matplotlib



\### Files



\* quantum\_coin\_toss.py — Main quantum coin toss simulator

\* draw\_circuit.py — Generates circuit visualization

\* circuit.png — Quantum circuit diagram

\* histogram.png — Measurement histogram

\* README.md — Project documentation



\---



\## Results



Sample execution (1000 shots):



Heads (0): 487



Tails (1): 513



The results demonstrate approximately 50% probability for each outcome, validating the quantum superposition principle.



\---



\## Sample Output



```python

Quantum Coin Toss Result:



{'0': 487, '1': 513}

```



\---



\## Measurement Histogram



Histogram representation of the measurement outcomes obtained from 1000 shots.



!\[Measurement Histogram](histogram.png)



The near-equal distribution of outcomes validates the probabilistic nature of quantum superposition and quantum measurement.



\---



\## Learning Outcomes



Through this project I learned:



\* Quantum circuit design

\* Qubit manipulation

\* Hadamard gate operations

\* Quantum measurement

\* Qiskit programming

\* Data visualization using Matplotlib

\* Git and GitHub workflow



\---



\## Future Work



Future enhancements include:



\* Quantum Random Number Generator

\* Bell State and Quantum Entanglement Simulator

\* Grover's Search Algorithm

\* Quantum Key Distribution (BB84)

\* Quantum Machine Learning Applications



\---



\## How to Run



\### Install Dependencies



```bash

pip install qiskit qiskit-aer matplotlib

```



\### Run the Simulator



```bash

python quantum\_coin\_toss.py

```



\### Generate Circuit Diagram



```bash

python draw\_circuit.py

```



\---



\## Author



\*\*Jasmine Sultana\*\*



M.Tech (Artificial Intelligence)



Vidyasagar University



Interested in Quantum Computing, Quantum Machine Learning, Artificial Intelligence, and Data Science.



