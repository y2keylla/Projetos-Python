import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    matriz = np.array(list).reshape(3, 3)
    
    calculations = {
        # Axis = 0 => Calcula a coluna
        # Axis = 1 => Calcula a linha
        # Não usar o axis calcula todos os elementos da matriz 
 
        'mean': [
            np.mean(matriz, axis=0).tolist(),  # Média coluna
            np.mean(matriz, axis=1).tolist(),  # Média linha
            np.mean(matriz).tolist()          # Média total
        ],
        'variance': [
            np.var(matriz, axis=0).tolist(),  # Variância coluna
            np.var(matriz, axis=1).tolist(),  # Variância linha
            np.var(matriz).tolist()          # Variância total
        ],
        'standard deviation': [
            np.std(matriz, axis=0).tolist(),  # Desvio padrão coluna
            np.std(matriz, axis=1).tolist(),  # Desvio padrão linha
            np.std(matriz).tolist()          # Desvio padrão total
        ],
        'max': [
            np.max(matriz, axis=0).tolist(),  # Máximo coluna
            np.max(matriz, axis=1).tolist(),  # Máximo linha
            np.max(matriz).tolist()          # Máximo total
        ],
        'min': [
            np.min(matriz, axis=0).tolist(),  # Mínimo coluna
            np.min(matriz, axis=1).tolist(),  # Mínimo linha
            np.min(matriz).tolist()          # Mínimo total
        ],
        'sum': [
            np.sum(matriz, axis=0).tolist(),  # Soma coluna
            np.sum(matriz, axis=1).tolist(),  # Soma linha
            np.sum(matriz).tolist()          # Soma total
        ]
    }

    return calculations
