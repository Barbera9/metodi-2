import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import compressione
import sys

def scegli_img(msg="base"):
    msg1= "Seleziona un'immagine BMP in toni di grigio"
    acc_filetypes=[("Bitmap Image","*.bmp")]
    filepath=filedialog.askopenfilename(title=msg1,filetypes=acc_filetypes)
    if not filepath:
        return
    
    try:
        with Image.open(filepath) as img:
            if img.mode != "L":
                messagebox.showinfo("Attenzione",f"Immagine \n{filepath} non in toni di grigio (modalità L), verrà convertita")
                if(msg == "base"):
                    compressione.imageCompression(filepath)
                else:
                    compressione.imageCompression(filepath,msg)
            else:
                messagebox.showinfo("Selezione andata a buon fine",f"Hai selezionato: \n{filepath}")
                ##call script principale
                if(msg == "base"):
                    compressione.imageCompression(filepath)
                else:
                    compressione.imageCompression(filepath,msg)

    except Exception as e:
        messagebox.showerror("Errore", f"Impossibile aprire il file: \n{e}")

if len(sys.argv)>1:
    msg = sys.argv[1]
else:
    msg = "base"

root = tk.Tk()
root.title("Selezione Immagine BMP")
root.geometry("400x150") #dimensione iniziale della finestra in pixel

#pulsanti di controllo dimesioni finestra e simili
root.resizable(True,True)
frame = tk.Frame(root)

frame.pack(pady=10,expand=True)


btn=tk.Button(frame, text="Scegli un immagine .bmp", command=lambda: scegli_img(msg))
btn.grid(row=0,column=0,padx=10)

root.mainloop() #avvia ciclo principale per interfaccia grafica