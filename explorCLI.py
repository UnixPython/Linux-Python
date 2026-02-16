import argparse
import os
import time


def scan_directory(path):
    results = []

    for root, dirs, files in os.walk(path):
        for file in files:
            full_path = os.path.join(root, file)
            try:
                size = os.path.getsize(full_path)
                results.append((file, size))
            except PermissionError:
                continue

    return results


def sort_results(results, reverse=True):
    return sorted(results, key=lambda x: x[1], reverse=reverse)


def show_results(results, top):
    print("\nTop archivos:\n")
    for name, size in results[:top]:
        print(f"{name} -> {size / (1024*1024):.2f} MB")


def main():
    parser = argparse.ArgumentParser(description="Analizador de archivos por tamaño")

    parser.add_argument("path", help="Ruta del directorio a Analizar")

    parser.add_argument(
        "-t",
        "--top",
        type=int,
        default=10,
        help="Cantidad de archivos a mostar (default=10)",
    )

    parser.add_argument(
        "-r", "--reverse", action="store_true", help="Mostrar de menor a mayor tamaño"
    )

    args = parser.parse_args()

    if not os.path.exits(args.path):
        print("Ruta no valida.")
        return

    results = scan_directory(args.path)
    sort_results = sort_results(results, reverse=args.reverse)
    show_results(sorted_results, args.top)


if __name__ == "__main__":
    main()
