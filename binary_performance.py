import numpy as np
import time

def generate_random_numbers(count):
    # Calculează intervalul în funcție de dimensiunea listei
    interval = count * 10
    # Generare și sortare rapidă
    return np.sort(np.random.randint(0, interval, size=count))

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    operations = 0
    while low <= high:
        operations += 1
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid, operations
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, operations

def main():
    while True:
        try:
            # Introducere număr elemente
            x = int(input("Introduceți numărul de elemente (până la 100 milioane): "))
            if x <= 0:
                print("Introduceți un număr pozitiv.")
                continue

            # Generare rapidă
            print("Generarea și sortarea șirului...")
            start_time = time.time()
            numbers = generate_random_numbers(x)
            elapsed_time = time.time() - start_time
            print(f"Generare completă. Timp: {elapsed_time:.2f} secunde.")

            # Afișează primele și ultimele 10 numere
            if x <= 100:
                print("Numerele generate:")
                print(numbers)
            else:
                print("Primele 10 numere generate:")
                print(numbers[:10])  # Primele 10
                print("Ultimele 10 numere generate:")
                print(numbers[-10:])  # Ultimele 10

            # Introducere număr de căutat
            target = int(input("Introduceți numărul pe care doriți să-l căutați: "))
            print("Căutare în progres...")
            start_time = time.time()
            position, operations = binary_search(numbers, target)
            search_time = time.time() - start_time

            # Rezultatul căutării
            if position != -1:
                print(f"Numărul {target} a fost găsit la poziția {position}.")
            else:
                print(f"Numărul {target} nu a fost găsit în șir.")
            print(f"Numărul de operații efectuate: {operations}.")
            print(f"Timpul de căutare: {search_time:.6f} secunde.")

            # Continuare sau ieșire
            choice = input("Doriți să continuați? (1 = Da, 2 = Nu): ")
            if choice.strip() == '2':
                print("Program încheiat.")
                break
        except ValueError:
            print("Valoare invalidă. Încercați din nou.")

if __name__ == "__main__":
    main()
