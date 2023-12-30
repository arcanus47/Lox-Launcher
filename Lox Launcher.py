import minecraft_launcher_lib
import subprocess
import sys
import os
from pathlib import Path

# Chequea si se esta ejecutando en Linux o Windows y obtiene la ruta estandar de los archivos de minecraft
if os.name == "nt":
    minecraft_directorio = str(os.getenv("APPDATA")+".lox_launcher")
elif os.name == "posix":
    minecraft_directorio = str(Path.home()+".lox_launcher")

# Instalación de Minecraft
def install_minecraft():
    minecraft_version = input("Versión: ")
    minecraft_launcher_lib.install.install_minecraft_version(
        minecraft_version, minecraft_directorio)
    print(f"Versión instalada: {minecraft_version}")

# Instalación de Forge
def install_forge():
    forge_ver = input("Versión: ")
    forge = minecraft_launcher_lib.forge.find_forge_version(forge_ver)
    print(forge)
    minecraft_launcher_lib.forge.install_forge_version(
        forge, minecraft_directorio)
    print(f"Instalado Forge {forge}")

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
        "launcherVersion": "1.0",
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
          "3- Ejecutar Minecraft \n", 
          "4- Acerca de \n", 
          "5- Salir \n")
    
    formulario = input(f"{mine_user} selecciona una opción: ")
    if formulario == "1":
        install_minecraft()
        
    if formulario == "2":
        install_forge()
        
    if formulario == "3":
        ejecuta_mine(mine_user)
        
    if formulario == "4":
        print("Información: \n",
              "-NOMBRE: Lox Launcher \n",
              "-VERSIÓN: 1.0 \n",
              "-CREADOR: Cheremi Checo Dominguez \n",
              "-Porteador a Linux: Anderson Guzman Abreu")
        print(input())
    
    if formulario == "5":
        exit()

if __name__ == "__main__":
    menu()
