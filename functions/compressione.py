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