import numpy as np
entrada1 = np.array ([1,-1,-1,1])
entrada2 = np.array ([1,-1,-1,1])

W = np.outer(entrada1,entrada2) + np.outer(entrada2,entrada2)
np.fill_diagonal(W,0)

imagen = np.array([1,1,-1,-1])
def normalizer(x):
        return 1 if x > 0 else -1
for _ in range (100):
        nueva_imagen = np.array([normalizer(np.dot(W[i],imagen)) for i in range(4)])
        if np.all(imagen == nueva_imagen):
                break
        imagen = nueva_imagen
print(imagen)