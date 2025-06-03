import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from dd2 import dct_2D, idct_2D


def imageCompression(filepath):
    img = Image.open(filepath).convert("L")
    img_array = np.array(img)

    F=simpledialog.askinteger("Blocco DCT", "Inserisci F (min: 1 , max:128):", minvalue=1,maxvalue=128)
    if F is None:
        return
    
    max_d =2*F-2
    d = simpledialog.askinteger("Soglia Frequenze", f"inserisci d (min: 0 max: {max_d}):", minvalue=0, maxvalue=max_d)
    if d is None:
        return
    
    h, w =img_array.shape
    H = h- (h%F)
    W = w- (w%F)
    img_crop= img_array[:H,:W]
    result = np.zeros_like(img_crop, dtype=np.float32)

    for i in range(0,H,F):
        for j in range(0,W,F):
            block=img_crop[i:i+F,j:j+F]
            c=dct_2D(block)
            for k in range(F):
                for l in range(F):
                    if k+l >= d:
                        c[k,l]=0
            f_recon = idct_2D(c)
            f_recon = np.rint(f_recon).clip(0, 255)
            result[i:i+F, j:j+F] = f_recon
    
    fig, axs = plt.subplots(1,2,figsize=(10,5))
    axs[0].imshow(img_array, cmap="gray")
    axs[0].set_title("Originale")
    axs[0].axis("off")
    axs[1].imshow(result.astype(np.uint8), cmap="gray")
    axs[1].set_title(f"Modificata (F={F}, d={d})")
    axs[1].axis("off")
    plt.tight_layout()
    plt.show()