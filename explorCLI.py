import os
import time


def get_folder_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if os.path.isfile(fp):
                total_size += os.path.getsize(fp)
    return total_size


def list_subfolders(path):
    return [
        name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))
    ]


def list_files(path, recursive=False):
    files = []
    if recursive:
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                files.append(os.path.join(dirpath, f))
    else:
        for f in os.listdir(path):
            if os.path.isfile(os.path.join(path, f)):
                files.append(f)
    return files


def menu():
    print("\nBIENVENIDO")
    print("1. Ver tamaño")
    print("2. Ver subcarpetas")
    print("2.1 Ver archivos de subcarpetas")
    print("3. Ver archivos de la carpeta en general")
    print("4. Salir")


def main():
    path = input("Ingresa el directorio a analizar: ")

    if not os.path.exists(path):
        print("Directorio no existe")
        return

    while True:
        menu()
        opcion = input("Seleccione opción: ")

        if opcion == "1":
            size = get_folder_size(path)
            print(f"Tamaño total: {size / (1024*1024):.2f} MB")

        elif opcion == "2":
            subfolders = list_subfolders(path)
            print("Subcarpetas:", subfolders)

        elif opcion == "2.1":
            files = list_files(path, recursive=True)
            print("Archivos en subcarpetas:", files)

        elif opcion == "3":
            files = list_files(path, recursive=False)
            print("Archivos en la carpeta:", files)

        elif opcion == "4":
            time.sleep(1)
            print("Saliendo...")
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()
