import minecraft_launcher_lib
import subprocess
import sys
import os
from pathlib import Path

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

minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()

callback = {
    "setStatus": set_status,
    "setProgress": set_progress,
    "setMax": set_max
}

# Ruta de los archivos de Minecraft
if os.name == "nt":
    minecraft_directorio = str(os.getenv("APPDATA")+".lox_launcher")
elif os.name == "posix":
    minecraft_directorio = str(Path.home())+("/.lox_launcher")

# Instalación de Minecraft
def install_minecraft():
    minecraft_version = input("Versión de Minecraft: ")
    minecraft = minecraft_launcher_lib.install.install_minecraft_version(
        minecraft_version, minecraft_directorio, callback=callback)
    print(f"Versión instalada: {minecraft_version}")

# Instalación de Forge
def install_forge():
    forge_version = input("Versión de Forge: ")
    forge = minecraft_launcher_lib.forge.find_forge_version(forge_version)
    print(forge)
    minecraft_launcher_lib.forge.install_forge_version(
        forge, minecraft_directorio, callback=callback)
    print(f"Versión instalada: {forge_version}")

# Instalación de Fabric
def install_fabric():
    fabric_version = input("Versión de Fabric: ")
    fabric = minecraft_launcher_lib.fabric.install_fabric(fabric_version, minecraft_directorio, callback=callback)
    print(f"Versión instalada: {fabric_version}")

# Versiones de Minecraft instaladas
def ejecuta_mine(mine_user):
    forts = minecraft_launcher_lib.utils.get_installed_versions(
        minecraft_directorio)
    for fort in forts:
        print(fort["id"])
    version = input("Versión: ")

    options = {
        "username": mine_user,
        "uuid": "",
        "token": "",

        "jvmArguments": ["-Xmx1024M", "-Xms1024M"],  # The jvmArguments
        "launcherVersion": "1.1",
    }

    # Ejecutar Minecraft
    minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(
        version, minecraft_directorio, options)
    subprocess.run(minecraft_command)

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
    
    mine_user = input("Digite su nombre de usuario: ")
    print("\n")
    
    print("Opciones \n",
          "1- Instalar Minecraft \n", 
          "2- Instalar Forge \n",
          "3- Instalar Fabric \n",
          "4- Ejecutar Minecraft \n", 
          "5- Acerca de \n", 
          "6- Salir \n")
    
    formulario = input(f"{mine_user} selecciona una opción: ")
    if formulario == "1":
        install_minecraft()
        
    if formulario == "2":
        install_forge()
        
    if formulario == "3":
        install_fabric()
        
    if formulario == "4":
        ejecuta_mine(mine_user)
        
    if formulario == "5":
        print("LOX LAUNCHER: \n",
              "1.1 \n",
              " \n",
              "DIRECTORIO: \n",
              minecraft_directorio, "\n",
              " \n",
              "CREADOR: \n",
              "Cheremi Checo Dominguez \n",
              " \n",
              "COLABORADORES: \n",
              "Anderson Guzman Abreu \n",
              " \n",
              "LICENCIA: \n",
              "MIT - https://github.com/arcanus47/Lox-Launcher/blob/main/LICENSE \n")
        print(input())
    
    if formulario == "6":
        exit()

if __name__ == "__main__":
    menu()
