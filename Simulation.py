import simpy
import random
import numpy as np

# Configuración del entorno de simulación
env = simpy.Environment()
ram = simpy.Container(env, init = 100, capacity = 100)
cpu = simpy.Resource(env, capacity = 1)
random.seed(40)
cant_Procesos = 25
tiempos = []

class Simulation:

    # Constructor de un proceso
    def __init__(self, id, cant_Ram, cant_Instrucciones):
        self.id =id
        self.cant_Ram = cant_Ram
        self.cant_Instrucciones = cant_Instrucciones

# Funcion que crea los procesos 
def crear_Procesos():
    for i in range(cant_Procesos):
        intervalo = 10
        yield env.timeout(random.expovariate(1.0 / intervalo))
        proceso = Simulation(i, random.randint(1, 10), random.randint(1, 10))
        env.process(new(proceso))

# El proceso llega al sistema operativo pero debe esperar que se le asigne memoria RAM
def new(proceso_actual):
    with ram.get(proceso_actual.cant_Ram) as req:
        yield req
        yield ram.get(proceso_actual.cant_Ram)
        while proceso_actual.cant_Instrucciones > 0:
            yield from ready(proceso_actual)
            numeroAleatorio = random.randint(1, 2)
            if(numeroAleatorio == 1):
                #Cola Esperando
                yield env.timeout(2)
            ram.put(proceso_actual.cant_Ram) 

# El proceso está listo para correr pero debe esperar que lo atienda el CPU
def ready(proceso_actual):
    with cpu.request() as req:
        yield req  
        #Dirigirse a la etapa Running
        yield from running(proceso_actual)  

# El CPU atiende al proceso por un tiempo limitado, suficiente para realizar solamente 3 instrucciones
def running(proceso_actual):
    yield env.timeout(1)
    numero_intrucciones = 3
    # Actualizar el contador de instrucciones del proceso
    proceso_actual.cant_Instrucciones -= numero_intrucciones
    if proceso_actual.cant_Instrucciones <= 0:
        print(f"Proceso {proceso_actual.id} completado. En el timepo: {env.now}")
        tiempos.append(env.now)

# Funcion que ejecuta la simulacion
def ejecutar():
    env.process(crear_Procesos())
    env.run()
    promedio = np.mean(tiempos) 
    des_vest = np.std(tiempos) 
    print(f"Tiempo promedio de finalización: {promedio}")
    print(f"Desviación estándar de los tiempos de finalización: {des_vest}")