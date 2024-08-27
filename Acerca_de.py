import tkinter as tk
from tkinter import Canvas

#--------------------------------- CONFIGURACION DE LA VENTANA ----------------------------------
def abrir_ventana_acerca_de():
    ventana = tk.Toplevel()
    ventana.title("Lox Launcher")
    ventana.geometry("661x386")
    ventana.resizable(False, False)
    ventana.iconbitmap(r"assets/frame0/lox_launcher_icon.ico")
    ventana.configure(bg = "#242424")

    # Centralizar ventana
    wtotal = ventana.winfo_screenwidth()
    htotal = ventana.winfo_screenheight()

    wventana = 661
    hventana = 386

    pwidth = round(wtotal/2-wventana/2)
    pheight = round(htotal/2-hventana/2)
    ventana.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

#------------------------------------- DISEÑO VENTANA -------------------------------------------
    canvas = Canvas(ventana, bg = "#242424", height = 386, width = 661, bd = 0, highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)

    canvas.create_text(43.0, 55.0, anchor="nw", text="Creador", fill="#FFFFFF", font=("Minercraftory", 15 * -1))
    canvas.create_text(43.0, 86.0, anchor="nw", text="Cheremi Checo “arcanus47”", fill="#FFFFFF", font=("Simple", 20 * -1))

    canvas.create_text(43.0, 133.0, anchor="nw", text="Nombre", fill="#FFFFFF", font=("Minercraftory", 15 * -1))
    canvas.create_text(43.0, 164.0, anchor="nw", text="Lox Launcher", fill="#FFFFFF", font=("Simple", 20 * -1))

    canvas.create_text(43.0, 208.0, anchor="nw", text="Versión", fill="#FFFFFF", font=("Minercraftory", 15 * -1))
    canvas.create_text(43.0, 234.0, anchor="nw", text="1.4", fill="#FFFFFF", font=("Simple", 20 * -1))

    canvas.create_text(43.0, 278.0, anchor="nw", text="Licencia", fill="#FFFFFF", font=("Minercraftory", 15 * -1))
    canvas.create_text(43.0, 309.0, anchor="nw", text="MIT License", fill="#FFFFFF", font=("Simple", 20 * -1))

    canvas.create_rectangle(370.99999979935177, 25.0, 372.0, 364.0, fill="#FFFFFF", outline="")

    canvas.create_text(400.0, 50.0, anchor="nw", text="Colaboradores", fill="#FFFFFF", font=("Minercraftory", 15 * -1))
    canvas.create_text(400.0, 81.0, anchor="nw", text="Anderson Guzman Abreu", fill="#FFFFFF", font=("Simple", 20 * -1))

    ventana.mainloop()
