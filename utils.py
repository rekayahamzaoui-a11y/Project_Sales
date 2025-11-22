# utils.py
import numpy as np

def generate_random_sales(min_val, max_val, size):
    """
    Génère un tableau de ventes aléatoires entre min_val et max_val de taille size.
    """
    return np.random.randint(min_val, max_val, size)
