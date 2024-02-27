import simpy
import random

env = simpy.Environment()
ram = simpy.Container(env, init = 100, capacity = 100)
cpu = simpy.Resource(env, capacity = 1)
random.seed(40)
cant_Procesos = 25

class Simulation:

    # Constructor de un proceso
    def initialize(self, id, cant_Ram, cant_Instrucciones):
        self.id = id
        self.cant_Ram = cant_Ram
        self.cant_Instrucciones = cant_Instrucciones

# Funcion que crea los procesos 
def crear_Procesos():
    for i in range(cant_Procesos):
        intervalo = 10
        yield env.timeout(random.expovariate(1.0 / intervalo))
        proceso = Simulation(i, random.randint(1, 10), random.randint(1, 10))
        env.process(new(proceso))