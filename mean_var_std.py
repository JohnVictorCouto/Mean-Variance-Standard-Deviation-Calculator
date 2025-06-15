# Importa a biblioteca numpy para manipulação de arrays numéricos
import numpy as np

# Define a função 'calculate' que recebe uma lista como argumento
def calculate(list):
    
    # Verifica se a lista contém exatamente 9 elementos
    if len(list) != 9:
        # Se não tiver 9 elementos, levanta um erro informando ao usuário
        raise ValueError("List must contain nine numbers.")
    
    # Converte a lista em um array numpy com formato 3x3 (3 linhas x 3 colunas)
    arr = np.array(list).reshape(3,3)
    
    # Calcula a média de cada coluna (axis=0), e converte para lista
    mean_axis0 = arr.mean(axis=0).tolist()
    
    # Calcula a média de cada linha (axis=1), e converte para lista
    mean_axis1 = arr.mean(axis=1).tolist()
    
    # Calcula a média geral de todos os elementos (array "flattened")
    mean_flat = arr.mean().item()
    
    # Calcula a variância de cada coluna
    var_axis0 = arr.var(axis=0).tolist()
    
    # Calcula a variância de cada linha
    var_axis1 = arr.var(axis=1).tolist()
    
    # Calcula a variância total do array
    var_flat = arr.var().item()
    
    # Calcula o desvio padrão de cada coluna
    std_axis0 = arr.std(axis=0).tolist()
    
    # Calcula o desvio padrão de cada linha
    std_axis1 = arr.std(axis=1).tolist()
    
    # Calcula o desvio padrão total
    std_flat = arr.std().item()
    
    # Encontra o valor máximo de cada coluna
    max_axis0 = arr.max(axis=0).tolist()
    
    # Encontra o valor máximo de cada linha
    max_axis1 = arr.max(axis=1).tolist()
    
    # Encontra o valor máximo de todo o array
    max_flat = arr.max().item()
    
    # Encontra o valor mínimo de cada coluna
    min_axis0 = arr.min(axis=0).tolist()
    
    # Encontra o valor mínimo de cada linha
    min_axis1 = arr.min(axis=1).tolist()
    
    # Encontra o valor mínimo geral do array
    min_flat = arr.min().item()
    
    # Calcula a soma dos elementos de cada coluna
    sum_axis0 = arr.sum(axis=0).tolist()
    
    # Calcula a soma dos elementos de cada linha
    sum_axis1 = arr.sum(axis=1).tolist()
    
    # Calcula a soma total de todos os elementos do array
    sum_flat = arr.sum().item()
    
    # Cria um dicionário chamado 'calculations' que armazena todas as estatísticas
    calculations = {
        'mean': [mean_axis0, mean_axis1, mean_flat],
        'variance': [var_axis0, var_axis1, var_flat],
        'standard deviation': [std_axis0, std_axis1, std_flat],
        'max': [max_axis0, max_axis1, max_flat],
        'min': [min_axis0, min_axis1, min_flat],
        'sum': [sum_axis0, sum_axis1, sum_flat]
    }
    
    # Retorna o dicionário com os cálculos prontos
    return calculations
