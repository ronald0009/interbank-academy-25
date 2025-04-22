import csv
import argparse
import unicodedata

# Función para eliminar acentos y tildes de un texto (útil para comparaciones robustas)
def strip_accents(text):
    return ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'
    )

# Función principal que procesa el archivo CSV
def process_csv(file_path):
    final_balance = 0
    max_transaction = {"monto": float('-inf'), "row": None}
    credit_count = 0
    debit_count = 0

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            amount = float(row["monto"])
            txn_type = strip_accents(row["tipo"].lower())  # normalize

            # Si es un crédito, sumamos y actualizamos el máximo si corresponde
            if txn_type == "credito":
                final_balance += amount
                credit_count += 1

                if amount > max_transaction["monto"]:
                    max_transaction = {"monto": amount, "row": row}

            # Si es un débito, restamos y contamos (no se considera para el máximo)
            elif txn_type == "debito":
                final_balance -= amount
                debit_count += 1

    return final_balance, max_transaction["row"], credit_count, debit_count

# Función principal que se ejecuta desde la línea de comandos
def main():
    parser = argparse.ArgumentParser(description="Procesa un archivo CSV con transacciones financieras.")
    parser.add_argument("file", help="Ruta al archivo CSV")
    args = parser.parse_args()

    balance, max_txn, credits, debits = process_csv(args.file)

    print(f"\nReporte de Transacciones")
    print(f"\n------------------------------------------------------")
    print(f"\n📊 Balance Final: {balance:.2f}")
    print(f"💰 Transacción de Mayor Monto: ID {max_txn['id']} ({max_txn['tipo']}, {max_txn['monto']})")
    print(f"Conteo de Transacciones. 📈 Créditos: {credits} 📉 Débitos: {debits}\n")

# Ejecutamos la función principal si el script es ejecutado directamente
if __name__ == "__main__":
    main()
