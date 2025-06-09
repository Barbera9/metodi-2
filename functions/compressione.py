import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from dd2 import dct_2D, idct_2D


def imageCompression(filepath):
    img = Image.open(filepath).convert("L") #converte l'immagine in bianco  nero
    img_array = np.array(img) # è una matrice np con valori da 0 a 255, prende come input l'imm BW

    F=simpledialog.askinteger("Blocco DCT", "Inserisci F (min: 1 , max:128):", minvalue=1,maxvalue=128)
    if F is None:
        return
    
    max_d =2*F-2
    d = simpledialog.askinteger("Soglia Frequenze", f"inserisci d (min: 0 max: {max_d}):", minvalue=0, maxvalue=max_d)
    if d is None:
        return
    #ritaglio immagine in multiplidi F
    h, w =img_array.shape #altezza,larghezza immagine convertita
    #arrotondano pr difetto altezza e larghezza al multiplo piu vicino ad F = valore - modulo(valore,F)
    H = h- (h%F) 
    W = w- (w%F)
    img_crop= img_array[:H,:W] # crea nuova immagine senza i pixel extra nei bordi
    #inizializzazione imm risultante con una matrice vuota
    result = np.zeros_like(img_crop, dtype=np.float32) 

    #applicazione dct2 ed idct2 per blocchi
    for i in range(0,H,F):
        for j in range(0,W,F):
            block=img_crop[i:i+F,j:j+F]  # divisione in blocchi FxF
            c=dct_2D(block)
            #eliminazione frequenze con k+l >= d
            for k in range(F):
                for l in range(F):
                    if k+l >= d:
                        c[k,l]=0 #eliminazione di frequenze k+l >=d
            f_recon = idct_2D(c) #ricostruzione blocco vi idct
            f_recon = np.rint(f_recon).clip(0, 255) #blocco ricostruito ed arrotondato e normalizzato 0,255
            result[i:i+F, j:j+F] = f_recon # inserimento nell' immagine finale
    
    #mostr risultato
    fig, axs = plt.subplots(1,2,figsize=(10,5)) 
    #fig è necessario anche se non usato: è per definire i due sotto-plot axs
    axs[0].imshow(img_array, cmap="gray")
    axs[0].set_title("Originale")
    axs[0].axis("off")
    axs[1].imshow(result.astype(np.uint8), cmap="gray")
    axs[1].set_title(f"Modificata (F={F}, d={d})")
    axs[1].axis("off")
    plt.tight_layout()
    plt.show()