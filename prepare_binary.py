import os
import subprocess
import sys

def chequea_nuitka_instalado():
    try:
        # Intenta obtener la versión de Nuitka, asi se ve si esta en el sistema
        result =  subprocess.run([sys.executable, "-m", "nuitka","--version"], check=True, text=True)
        print("Nuitka está instalado")
    except subprocess.CalledProcessError:
        # Captura la excepción si el comando falla
        print("Nuitka no está instalado en el sistema.")
        install_nuitka()

def install_nuitka():
    try:
        # Intenta instalar Nuitka usando pip
        subprocess.run([sys.executable, "-m", "pip", "install", "nuitka"], check=True)
        print("Nuitka se ha instalado correctamente.")
    except subprocess.CalledProcessError as e:
        # Captura la excepción si la instalación falla
        print(f"Error al instalar Nuitka: {e}")
        sys.exit(1)


def compilar_proyecto():
    # Compila el proyecto con Nuitka
    compile_command = "python -m nuitka --include-package-data=minecraft_launcher_lib --follow-imports --onefile './Lox Launcher.py'"
    os.system(compile_command)

    print(f"Lox-Launcher compilado")


if __name__ == "__main__":
    chequea_nuitka_instalado()
    compilar_proyecto()