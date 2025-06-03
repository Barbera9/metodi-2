import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def _compute_D(N):
    # Calcola la matrice D della DCT tipo II (non normalizzata)
    D = np.zeros((N, N))
    for k in range(N):
        for n in range(N):
            D[k, n] = np.cos(np.pi * k * (2 * n + 1) / (2 * N))
    D[0, :] *= 1 / np.sqrt(N)
    D[1:, :] *= np.sqrt(2 / N)
    return D

def dct_2D(f_mat, plot=False): # f_mat è matrice quadrata N x N
    N = f_mat.shape[0]
    D = _compute_D(N)
    
    c_mat = f_mat.copy()
    
    # DCT per colonne
    for j in range(N):
        c_mat[:, j] = D @ c_mat[:, j]
        
    # DCT per righe
    for i in range(N):
        c_mat[i, :] = (D @ c_mat[i, :].T).T
    
    if plot:
    # Plot tipo bar3
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
    
        x, y = np.meshgrid(range(N), range(N))
        x = x.flatten()
        y = y.flatten()
        z = np.zeros_like(x)
        dx = dy = 0.5 * np.ones_like(x)
        dz = c_mat.flatten()
    
        ax.bar3d(x, y, z, dx, dy, dz, shade=True)
        plt.show()
    
    return c_mat


def idct_2D(c_mat):
    N = c_mat.shape[0]
    D= _compute_D(N)
    f_mat=c_mat.copy()

    #righe
    for i in range(N):
        f_mat[i, :] = (D.T @ f_mat[i, :].T).T
    #colonne
    for j in range(N):
        f_mat[:, j] = D.T @ f_mat[:, j]

    return f_mat