import csv


def analyze_log(file):
    if '.csv' not in file:
        raise FileNotFoundError(f"Extensão inválida: '{file}'")

    try:
        with open(file) as file_csv:
            return csv.reader(file_csv)
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{file}'")
