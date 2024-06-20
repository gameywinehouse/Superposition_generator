import math
import time
import threading

class CustomPRNG:
    def __init__(self):
        self.seed = int(time.time())
        self.active = True

    def generate_random(self):
        if not self.active:
            raise RuntimeError("The PRNG has been deactivated.")
        
        self.seed = (self.seed * 22695477 + 1) & 0xFFFFFFFF
        return (math.sin(self.seed) + math.tan(self.seed) + math.exp(math.sin(self.seed))) % 1.0

    def deactivate(self):
        self.active = False

def emulate_qubit(prng):
    random_value = prng.generate_random()
    if random_value < 0.5:
        return random_value, "0"
    else:
        return random_value, "1"

def execute_simulation(prng):
    try:
        while prng.active:
            random_value, qubit_state = emulate_qubit(prng)
            print(f"Random value: {random_value:.6f}, Qubit state: |{qubit_state}>")
            time.sleep(1)  # Pause for a second to make the output readable
    except RuntimeError as error:
        print(error)

def await_termination(prng):
    input("Press Enter to terminate the simulation.\n")
    prng.deactivate()

# Example usage
prng = CustomPRNG()

# Create and start the simulation thread
simulation_thread = threading.Thread(target=execute_simulation, args=(prng,))
simulation_thread.start()

# Wait for user input to stop the simulation
await_termination(prng)

# Wait for the simulation thread to finish
simulation_thread.join()

print("Simulation terminated.")


