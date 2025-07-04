import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.fftpack import dct
import dd2

def dct2_library(f_mat):
    return dct(dct(f_mat.T, norm='ortho').T, norm='ortho')

# def initialize():

Ns = [8, 16, 32, 64, 128, 256, 512]
times_homemade = []
times_library = []

for N in Ns:
    f = np.random.rand(N, N)

    # Tempo DCT fatta in casa
    start = time.perf_counter()
    A=dd2.dct_2D(f)
    end = time.perf_counter()
    homemadeTime=end-start
    times_homemade.append(homemadeTime)

    # Tempo DCT libreria
    start = time.perf_counter()
    B=dct2_library(f)
    end = time.perf_counter()
    libraryTime=end-start
    times_library.append(libraryTime)
    

    # Plot
plt.figure(figsize=(10, 6))
plt.semilogy(Ns, times_homemade, 'o-', label='DCT2 fatta in casa')
plt.semilogy(Ns, times_library, 's-', label='DCT2 libreria (scipy)')
plt.xlabel('Dimensione N')
plt.ylabel('Tempo di esecuzione (s)')
plt.title('Confronto tempi DCT2: fatta in casa vs. libreria')
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()

