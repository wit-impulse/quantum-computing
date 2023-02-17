# quantum-computing

## Shor's Algorithm
The `Shor` class implements Shor's algorithm, a quantum algorithm for finding the prime factors of an integer in polynomial time. The class takes an integer `N` as its input and provides a method `run` that returns the prime factors of `N`, if they exist.

The `Shor` class uses the Qiskit framework to create a quantum circuit that performs the main part of the algorithm. The `run` method first chooses a random number `a` and computes the greatest common divisor of `a` and `N`. If the gcd is greater than 1, the algorithm has already found a factor of `N` and returns it. Otherwise, it creates a quantum circuit using `math.ceil(math.log2(N)) * 2` qubits and applies a series of gates to find the period of a certain function. The algorithm then measures the first register of the circuit and uses the results to find the period, which is the key to finding the prime factors of `N`. The `find_period` method is used to find the period from the results of the measurements.

If the algorithm successfully finds the prime factors of `N`, the `run` method returns them as a tuple. If the algorithm does not find the factors, it returns `None`.

To use the `Shor` class, create an instance of the class with the integer `N` as its input and call the `run` method. The method returns the prime factors of `N`, if they exist.
## Grovers Algorithm


