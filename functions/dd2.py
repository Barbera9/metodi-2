import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def compute_D(N):
    # Calcola la matrice D della DCT tipo II (non normalizzata)
    D = np.zeros((N, N))
    alpha_vect = np.zeros(N)
    alpha_vect[0]= N** -0.5 # N ^ -0.5
    alpha_vect[1:] = (N** -0.5)*np.sqrt(2)

    for k in range(N):
        for n in range(N):
            D[k, n] = alpha_vect[k] * np.cos(k * np.pi * (2 * n + 1) / (2 * N)) # formula leggermente diversa per il cambio base, python è zero-based

    return D

def dct_2D(f_mat): # f_mat è matrice quadrata N x N
    N = f_mat.shape[0]
    D = compute_D(N)
    
    c_mat = f_mat.copy()
    
    # DCT per colonne
    for j in range(N):
        c_mat[:, j] = D @ c_mat[:, j]
        
    # DCT per righe
    for i in range(N):
        c_mat[i, :] = (D @ c_mat[i, :].T).T 
    
    return c_mat


def idct_2D(c_mat):
    N = c_mat.shape[0]
    D= compute_D(N)
    f_mat=c_mat.copy()

    #righe
    for i in range(N):
        f_mat[i, :] = (D.T @ f_mat[i, :].T).T
    #colonne
    for j in range(N):
        f_mat[:, j] = D.T @ f_mat[:, j]

    return f_mat