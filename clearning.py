#!/usr/bin/env python3
# limpieza de Arch Linux
import os
import shutil
import subprocess
import sys
import time

print("=== WELCOME === ")


def espace_verificate():
    print(f"=== ESPACIO EN TOTAL ===")
    time.sleep(5)
    print("Viendo el espacio en total...")
    # df -h
    espace = subprocess.run(["df", "-h"], capture_output=True, text=True)
    print(espace.stdout)


def verifivate_pacman_cache():
    time.sleep(5)
    print("Verificando espacio en caché de pacman...")
    veryf = subprocess.run(
        ["du", "-sh", "/var/cache/pacman/pkg"], capture_output=True, text=True
    )
    print(veryf.stdout)


def paccache_verifi():
    op = input("¿Tiene paccache instalado?").lower().strip()
    if op == "si":
        time.sleep(5)
        print("Borrando caché...")
        paccache = subprocess.run(["sudo", "paccache", "-r"])
        paccache = subprocess.run(["sudo", "paccache", "-rk1"])
        paccache = subprocess.run(["sudo", "paccache", "-ruk0"])

    elif op == "no":
        print("Instalando pacman contrib...")
        os.system("sudo pacman -S pacman-contrib --noconfirm")
        print("pacman-contrib instalado exitosamente.")
        time.sleep(10)
        print(f"limpiando caché...")
        paccache = subprocess.run(["sudo", "paccache", "-r"])
        paccache = subprocess.run(["sudo", "paccache", "-rk1"])
        paccache = subprocess.run(["sudo", "paccache", "-ruk0"])
        exit()
    else:
        print("Error.")


def pacmanclear():
    scc = subprocess.run(["sudo", "pacman", "-Scc"])
    scc = subprocess.run(["sudo", "pacman", "-Rns", "$(pacman -Qtdq)"], shell=True)
    print("Pacman limpio!")


def clearlogs():
    clear = subprocess.run(["sudo", "journalctl", "--vacuum-time=2weeks"])
    clear = subprocess.run(["sudo", "journalctl", "--vacuum-size=100M"])
    clear = subprocess.run(["sudo", "rm", "-rf", "/var/log/journal/*"])
    print("logs limpios.")


def thumbnails():
    thumb = subprocess.run(["sudo", "rm", "-rf", "~/.thumbnails"], shell=True)
    thumb = subprocess.run(["sudo", "rm", "-rf", "~/.cache/thumbnails/*"], shell=True)
    print("Thumb nails limpio")


def delete_bashrc():
    os.system("rm -rf ~/.bash_history")
    print("Historial de bash limpio.")


def temporal_archives():
    os.system("sudo find /tmp -type f -atime +7 -delete")
    os.system("sudo find /var/tmp -type f -atime +7 -delete")
    print(f"Limpieza de archivos temporales terminada.")
