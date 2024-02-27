import simpy
import random

env = simpy.Environment()
ram = simpy.Container(env, init=100, capacity=100)
cpu = simpy.Resource(env, capacity=1)
random.seed(40)
cantProcesos = 25

class Simulation:
    
    # Constructor de un proceso
    def __init__(self, id, cantRam, cantInstrucciones):
        self.id =id
        self.cantRam = cantRam
        self.cantInstrucciones = cantInstrucciones

