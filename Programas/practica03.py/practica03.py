import numpy as np
entradas = np.array([[0,0,1],
                    [1,1,1],
                    [1,0,1],
                    [0,1,1]])
salida_esperada = np.array([[0],
                            [1],
                            [1],
                            [0]])

def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def sigmoid_gradiente(x):
    return x * (1-x)
np.random.seed(42)
pesos=np.random.rand(3,1)
tasa_aprendizaje=0.01
num_iteraciones = 5000
for iteracion in range(num_iteraciones):
    entrada_ponderada=np.dot(entradas,pesos)
    salida_obtenida=sigmoid(entrada_ponderada)
    error=salida_esperada-salida_obtenida
    ajustes=error*sigmoid_gradiente(salida_obtenida)
    pesos+=np.dot(entradas.T,ajustes) * tasa_aprendizaje
print("Salida obtenida despues del entrenamiento:")
print(salida_obtenida)
print("\nPesos despues del entrenamiento")
print(pesos)