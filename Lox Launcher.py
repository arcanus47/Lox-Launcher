import minecraft_launcher_lib
import subprocess
import os
import json

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
def instalar_minecraft():
    minecraft_version = input("Versión de Minecraft: ")
    minecraft_launcher_lib.install.install_minecraft_version(minecraft_version, minecraft_directorio, callback=callback)
    print(f"Versión instalada: {minecraft_version}")

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
def instalar_fabric():
    version_fabric = input("Versión de Fabric: ")
    
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
        "version_launcher": "1.2"
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
    print("| |    / _ \ \/ / | |    / _` | | | | '_ \ / __| '_ \ / _ \ '__|  ")
    print("| |___| (_) >  <  | |___| (_| | |_| | | | | (__| | | |  __/ |     ")
    print("|______\___/_/\_\ |______\__,_|\__,_|_| |_|\___|_| |_|\___|_|     ")
    print("------------------------------------------------------------------")
    print("------------------------------------------------------------------")
    print("\n")
    print("--- Menú de Opciones ---")
    print("1. Instalar Minecraft")
    print("2. Instalar Forge")
    print("3. Instalar Fabric")
    print("4. Ejecutar Minecraft")
    print("5. Acerca de")
    print("6. Salir")
    print("\n")

# Cargar usuario y RAM guardados
usuario_predeterminado, ram_predeterminado = cargar_usuario_y_ram()

# Menú de opciones
while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        instalar_minecraft()
        
    elif opcion == "2":
        version_forge = input("Versión de Forge: ")
        instalar_forge(version_forge)
        
    elif opcion == "3":
        instalar_fabric()
        
    elif opcion == "4":
        # Solicitar inputs del usuario con valores predeterminados
        usuario_minecraft = input(f"Nombre de usuario [{usuario_predeterminado}]: ") or usuario_predeterminado
        ram = input(f"Cantidad de RAM (en GB) [{ram_predeterminado}]: ") or ram_predeterminado
        ejecutar_minecraft(usuario_minecraft, ram)
        
    elif opcion == "5":
        print("CREADOR: \n",
              "Cheremi Checo Dominguez \n",
              " \n",
              "NOMBRE DEL PROGRAMA: \n",
              "Lox Launcher \n",
              " \n",
              "VERSIÓN: \n",
              "1.2 \n",
              " \n",
              "RUTA DE LOS ARCHIVOS: \n",
              minecraft_directorio, "\n",
              " \n",
              "COLABORADORES: \n",
              "Anderson Guzman Abreu \n",
              " \n",
              "LICENCIA: \n",
              "MIT - https://github.com/arcanus47/Lox-Launcher/blob/main/LICENSE \n")
        input("Presione Enter para continuar...")
        
    elif opcion == "6":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")
