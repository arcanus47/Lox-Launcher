import minecraft_launcher_lib, subprocess, os, json
from pathlib import Path
import tkinter as tk
from tkinter import Tk, messagebox, Canvas, Entry, Button, PhotoImage
from Acerca_de import abrir_ventana_acerca_de

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#---------------------------------- CODIGOS DE FUNCIONAMIENTO -----------------------------------
"""
from pathlib import Path

# Ruta de los archivos de Minecraft linux
if os.name == "nt":
    minecraft_directorio = str(os.getenv("APPDATA")+".lox_launcher")
elif os.name == "posix":
    minecraft_directorio = str(Path.home())+("/.lox_launcher")
"""
# Ruta de los archivos de Minecraft
usuario_windows = os.environ["USERNAME"]
minecraft_directorio = f"C:/Users/{usuario_windows}/AppData/Roaming/.lox_launcher"

# Barra de Progreso
current_max = 0

def set_status(status: str):
    print(status)

def set_progress(progress: int):
    if current_max != 0:
        print(f"{progress}/{current_max}")

def set_max(new_max: int):
    global current_max
    current_max = new_max

callback = {
    "setStatus": set_status,
    "setProgress": set_progress,
    "setMax": set_max
}

# Función para guardar el usuario y la cantidad de RAM
def guardar_usuario_y_ram(usuario_minecraft, ram):
    datos = {
        "usuario": usuario_minecraft,
        "ram": ram
    }
    ruta_archivo_json = "datos_usuario_ram.json"
    with open(ruta_archivo_json, "w") as archivo_json:
        json.dump(datos, archivo_json, indent=4)

    print(f"Datos guardados en {ruta_archivo_json}")

# Función para cargar el usuario y la cantidad de RAM
def cargar_usuario_y_ram():
    ruta_archivo_json = "datos_usuario_ram.json"
    if os.path.exists(ruta_archivo_json):
        with open(ruta_archivo_json, "r") as archivo_json:
            datos = json.load(archivo_json)
            return datos.get("usuario", ""), datos.get("ram", "")
    return "", ""

# Función para instalar Minecraft
def instalar_minecraft(version_minecraft):
    minecraft_launcher_lib.install.install_minecraft_version(version_minecraft, minecraft_directorio, callback=callback)
    print(f"Versión instalada: {version_minecraft}")

# Función para instalar Forge
def instalar_forge(version):
    try:
        # Buscar la versión de Forge compatible
        forge = minecraft_launcher_lib.forge.find_forge_version(version)
        if forge is None:
            print(f"No se encontró la versión de Forge {version}.")
            return

        # Instalar Forge
        minecraft_launcher_lib.forge.install_forge_version(forge, minecraft_directorio, callback=callback)
        print(f"Forge versión {version} instalado correctamente.")

    except Exception as e:
        print(f"Error al instalar Forge: {e}")

# Función para instalar Fabric
def instalar_fabric(version_fabric):
    try:
        # Obtener la última versión del loader de Fabric para la versión especificada
        loader_version = minecraft_launcher_lib.fabric.get_latest_loader_version()

        # Instalar Fabric con la versión del loader obtenida
        minecraft_launcher_lib.fabric.install_fabric(version_fabric, loader_version, minecraft_directorio, callback=callback)
        print(f"Fabric versión {version_fabric} instalado correctamente.")

    except Exception as e:
        print(f"Error: {e}")

# Función para ejecutar Minecraft
def ejecutar_minecraft(usuario_minecraft, ram):
    versions = minecraft_launcher_lib.utils.get_installed_versions(minecraft_directorio)
    for version in versions:
        print(version["id"])
    version = input("Versión de Minecraft: ")

    opciones = {
        "username": usuario_minecraft,
        "uuid": "",
        "token": "",
        "jvmArguments": [f"-Xmx{ram}G", f"-Xms{ram}G"],
        "version_launcher": "1.3"
    }

    # Ejecutar Minecraft
    minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(version, minecraft_directorio, opciones)
    subprocess.run(minecraft_command)

    # Guardar el usuario y la cantidad de RAM
    guardar_usuario_y_ram(usuario_minecraft, ram)

# Shell del programa
def menu():
    print("------------------------------------------------------------------")
    print("------------------------------------------------------------------")
    print(" _                 _                            _                 ")
    print("| |               | |                          | |                ")
    print("| |     _____  __ | |     __ _ _   _ _ __   ___| |__   ___ _ __   ")
    print("| |    / _ \ \/ / | |    / _  | | | | '_ \ / __| '_ \ / _ \ '__|  ")
    print("| |___| (_) >  <  | |___| (_| | |_| | | | | (__| | | |  __/ |     ")
    print("|______\___/_/\_\ |______\__,_|\__,_|_| |_|\___|_| |_|\___|_|     ")
    print("------------------------------------------------------------------")
    print("------------------------------------------------------------------")
    print("\n")

# Cargar usuario y RAM guardados
usuario_predeterminado, ram_predeterminado = cargar_usuario_y_ram()

# Menú de opciones
def menu_instalar_minecraft():
    while True:
        menu()
        instalar_minecraft()
        break
    print("\n")

def menu_instalar_forge():
    while True:
        menu()
        version_forge = input("Versión de Forge: ")
        instalar_forge(version_forge)
        break
    print("\n")

def menu_instalar_fabric():
    while True:
        menu()
        instalar_fabric()
        break
    print("\n")

def ajustes():
    while True:
        menu()
        print("Ruta de los archivo:", minecraft_directorio)
        break
    print("\n")

def menu_ejecutar_minecraft():
    while True:
        menu()
        # Solicitar inputs del usuario con valores predeterminados
        usuario_minecraft = input(f"Nombre de usuario [{usuario_predeterminado}]: ") or usuario_predeterminado
        ram = input(f"Cantidad de RAM (en GB) [{ram_predeterminado}]: ") or ram_predeterminado
        ejecutar_minecraft(usuario_minecraft, ram)
        break
    print("\n")

def mensaje_boton():
    messagebox.showinfo("Información", "Lo sentimos pero esta opción aún está en desarrollo")

#------------------------------------------- MINECRAFT -------------------------------------------
def abrir_ventana_minecraft():
    ventana = tk.Toplevel()
    ventana.title("Lox Launcher")
    ventana.geometry("368x245")
    ventana.resizable(False, False)
    ventana.iconbitmap(r"lox_launcher_icon.ico")
    ventana.configure(bg="#242424")

    # Centralizar ventana
    wtotal = ventana.winfo_screenwidth()
    htotal = ventana.winfo_screenheight()

    wventana = 368
    hventana = 245

    pwidth = round(wtotal / 2 - wventana / 2)
    pheight = round(htotal / 2 - hventana / 2)
    ventana.geometry(f"{wventana}x{hventana}+{pwidth}+{pheight}")

#------------------------------------- DISEÑO VENTANA -------------------------------------------
    canvas = Canvas(ventana, bg="#242424", height=245, width=368, bd=0, highlightthickness=0, relief="ridge")
    canvas.place(x=0, y=0)

    canvas.create_text(78.0, 53.0, anchor="nw", text="Versión de Minecraft", fill="#FFFFFF", font=("Minercraftory", 15 * -1))

    entry_version = PhotoImage(file=relative_to_assets("entry_version.png"))
    canvas.create_image(184.0, 97.5, image=entry_version)
    version_minecraft = Entry(ventana, bd=0, bg="#131313", fg="white", highlightthickness=0, font=("Simple", 17 * -1))
    version_minecraft.place(x=43.0, y=84.0, width=282.0, height=25.0)

    button_instalar = PhotoImage(file=relative_to_assets("button_instalar.png"))

    # Modificar el comando del botón para pasar el valor del Entry a la función
    instalar = Button(ventana, image=button_instalar, borderwidth=0, highlightthickness=0, command=lambda: instalar_minecraft(version_minecraft.get()), relief="flat")
    instalar.place(x=67.0, y=124.0, width=234.0, height=49.0)

    ventana.mainloop()

#--------------------------------------------- FORGE ---------------------------------------------
def abrir_ventana_forge():
    ventana = tk.Toplevel()
    ventana.title("Lox Launcher")
    ventana.geometry("368x245")
    ventana.resizable(False, False)
    ventana.iconbitmap(r"assets/frame0/lox_launcher_icon.ico")
    ventana.configure(bg="#242424")

    # Centralizar ventana
    wtotal = ventana.winfo_screenwidth()
    htotal = ventana.winfo_screenheight()

    wventana = 386
    hventana = 245

    pwidth = round(wtotal/2-wventana/2)
    pheight = round(htotal/2-hventana/2)
    ventana.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

#------------------------------------- DISEÑO VENTANA -------------------------------------------
    canvas = Canvas(ventana, bg="#242424", height=245, width=368, bd=0, highlightthickness=0, relief="ridge")
    canvas.place(x=0, y=0)

    canvas.create_text(100.0, 53.0, anchor="nw", text="Versión de Forge", fill="#FFFFFF", font=("Minercraftory", 15 * -1))

    entry_version = PhotoImage(file=relative_to_assets("entry_version.png"))
    canvas.create_image(184.0, 97.5, image=entry_version)
    version_forge = Entry(ventana, bd=0, bg="#131313", fg="white", highlightthickness=0, font=("Simple", 17 * -1))
    version_forge.place(x=43.0, y=84.0, width=282.0, height=25.0)

    button_instalar = PhotoImage(file=relative_to_assets("button_instalar.png"))

    # Usar lambda para capturar el valor del Entry y pasarlo a la función instalar_forge
    instalar = Button(ventana, image=button_instalar, borderwidth=0, highlightthickness=0, command=lambda: instalar_forge(version_forge.get()), relief="flat")
    instalar.place(x=67.0, y=124.0, width=234.0, height=49.0)

    ventana.mainloop()

#-------------------------------------------- FABRIC --------------------------------------------
def abrir_ventana_fabric():
    ventana = tk.Toplevel()
    ventana.title("Lox Launcher")
    ventana.geometry("368x245")
    ventana.resizable(False, False)
    ventana.iconbitmap(r"assets/frame0/lox_launcher_icon.ico")
    ventana.configure(bg="#242424")

    # Centralizar ventana
    wtotal = ventana.winfo_screenwidth()
    htotal = ventana.winfo_screenheight()

    wventana = 386
    hventana = 245

    pwidth = round(wtotal/2-wventana/2)
    pheight = round(htotal/2-hventana/2)
    ventana.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

#------------------------------------- DISEÑO VENTANA -------------------------------------------
    canvas = Canvas(ventana, bg="#242424", height=245, width=368, bd=0, highlightthickness=0, relief="ridge")
    canvas.place(x=0, y=0)

    canvas.create_text(98.0, 53.0, anchor="nw", text="Versión de Fabric", fill="#FFFFFF", font=("Minercraftory", 15 * -1))

    entry_version = PhotoImage(file=relative_to_assets("entry_version.png"))
    canvas.create_image(184.0, 97.5, image=entry_version)
    version_fabric = Entry(ventana, bd=0, bg="#131313", fg="white", highlightthickness=0, font=("Simple", 17 * -1))
    version_fabric.place(x=43.0, y=84.0, width=282.0, height=25.0)

    button_instalar = PhotoImage(file=relative_to_assets("button_instalar.png"))
    instalar = Button(ventana, image=button_instalar, borderwidth=0, highlightthickness=0, command=lambda: instalar_fabric(version_fabric.get()), relief="flat")
    instalar.place(x=67.0, y=124.0, width=234.0, height=49.0)

    ventana.mainloop()

#--------------------------------- CONFIGURACION DE LA VENTANA ----------------------------------
ventana = Tk()
ventana.title("Lox Launcher")
ventana.geometry("800x500")
ventana.resizable(False, False)
ventana.iconbitmap(r"assets/frame0/lox_launcher_icon.ico")
ventana.configure(bg="#242424")

# Centralizar ventana
wtotal = ventana.winfo_screenwidth()
htotal = ventana.winfo_screenheight()

wventana = 800
hventana = 500

pwidth = round(wtotal/2-wventana/2)
pheight = round(htotal/2-hventana/2)
ventana.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

#----------------------------------- DISEÑO VENTANA PRINCIPAL -----------------------------------
canvas = Canvas(ventana, bg = "#242424", height = 500, width = 800, bd = 0, highlightthickness = 0, relief = "ridge")
canvas.place(x = 0, y = 0)

canvas.create_rectangle( 0.0, 0.0, 800.0, 50.0, fill="#1E1E1E", outline="")

button_noticias = PhotoImage(file=relative_to_assets("button_noticias.png"))
noticias = Button(image=button_noticias,borderwidth=0, highlightthickness=0, command=mensaje_boton, relief="flat")
noticias.place(x=53.0, y=8.0, width=113.0, height=41.0)

button_minecraft = PhotoImage(file=relative_to_assets("button_minecraft.png"))
minecraft = Button(image=button_minecraft, borderwidth=0, highlightthickness=0, command=abrir_ventana_minecraft, relief="flat")
minecraft.place( x=167.0, y=8.0, width=113.0, height=41.0)

button_forge = PhotoImage(file=relative_to_assets("button_forge.png"))
forge = Button( image=button_forge, borderwidth=0, highlightthickness=0, command=abrir_ventana_forge, relief="flat")
forge.place(x=281.0, y=8.0, width=113.0, height=41.0)

button_fabric = PhotoImage(file=relative_to_assets("button_fabric.png"))
fabric = Button(image=button_fabric, borderwidth=0, highlightthickness=0, command=abrir_ventana_fabric, relief="flat")
fabric.place(x=395.0, y=8.0, width=113.0, height=41.0)

button_ajustes = PhotoImage(file=relative_to_assets("button_ajustes.png"))
ajustes = Button(image=button_ajustes, borderwidth=0, highlightthickness=0, command=ajustes, relief="flat")
ajustes.place(x=509.0, y=8.0, width=121.0, height=41.0)

button_acerca_de = PhotoImage(file=relative_to_assets("button_acerca_de.png"))
acerca_de = Button(image=button_acerca_de, borderwidth=0, highlightthickness=0, command=abrir_ventana_acerca_de, relief="flat")
acerca_de.place(x=631.0, y=8.0, width=113.0, height=41.0)

image_fondo = PhotoImage(file=relative_to_assets("fondo.png"))
fondo = canvas.create_image(399.0, 253.0, image=image_fondo)

button_jugar = PhotoImage(file=relative_to_assets("button_jugar.png"))
jugar = Button(image=button_jugar, borderwidth=0, highlightthickness=0, command=menu_ejecutar_minecraft, relief="flat")
jugar.place(x=290.0,y=431.0, width=220.0, height=50.0)

ventana.mainloop()
