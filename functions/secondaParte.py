import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def scegli_img():
    msg1= "Seleziona un'immagine BMP in toni di grigio"
    acc_filetypes=[("Bitmap Image","*.bmp")]
    filepath=filedialog.askopenfilename(title=msg1,filetypes=acc_filetypes)
    if not filepath:
        return
    
    try:
        with Image.open(filepath) as img:
            if img.mode != "L":
                messagebox.showerror("Errore","Immagine non in toni di grigio (modalità L).")
            else:
                messagebox.showinfo("Selezione andata a buon fine",f"Hai selezionato: \n{filepath}")
                ##call script principale

    except Exception as e:
        messagebox.showerror("Errore", "Impossibile aprire il file: \n{e}")

root = tk.Tk()
root.title("Selezione Immagine BMP")
root.geometry("400x150") #dimensione iniziale della finestra in pixel

#pulsanti di controllo dimesioni finestra e simili
root.resizable(True,True)
frame = tk.Frame(root)

frame.pack(pady=10,expand=True)


btn=tk.Button(frame, text="Scegli un immagine .bmp", command=scegli_img)
btn.grid(row=0,column=0,padx=10)

#btn_max = tk.Button(frame, text="Maximizza", command=lambda: root.state("zoomed"))
#btn_max.grid(row=0, column=1, padx=10)

#btn_min = tk.Button(frame, text="Minimizza", command=lambda: root.iconify())
#btn_min.grid(row=0, column=2, padx=10)

root.mainloop() #avvia ciclo principale per interfaccia grafica