import time
from termcolor import colored

def print_array(arr, current_idx=None, sorted_idx=None):
    """Afișează tabloul cu evidențierea termenilor comparați și sortați."""
    for i in range(len(arr)):
        if current_idx is not None and (i == current_idx or i == current_idx + 1):
            # Evidențiere verde pentru comparație
            print(colored(arr[i], 'green'), end=' ')
        elif sorted_idx is not None and i >= sorted_idx:
            # Evidențiere galbenă pentru elemente sortate
            print(colored(arr[i], 'yellow'), end=' ')
        else:
            # Termeni obișnuiți
            print(arr[i], end=' ')
    print()  # Linie nouă

def bubble_sort(arr):
    n = len(arr)
    step = 1  # Inițializarea pașilor
    for i in range(n):
        # Parcurgem lista de la început, excluzând ultimele i elemente deja sortate
        for j in range(n - i - 1):
            # Afișează explicația despre ce comparăm
            print(f"Pasul {step}: Compar {arr[j]} cu {arr[j + 1]}")

            # Evidențierea tabloului actual
            print_array(arr, current_idx=j, sorted_idx=n - i)
            time.sleep(5)  # Pauză de 5 secunde

            # Verificăm dacă trebuie să schimbăm elementele
            if arr[j] > arr[j + 1]:
                # Explicăm de ce schimbăm
                print(f"Schimb {arr[j]} cu {arr[j + 1]} deoarece {arr[j]} > {arr[j + 1]}")
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            else:
                # Explicăm de ce NU schimbăm
                print(f"Nu schimb {arr[j]} cu {arr[j + 1]} deoarece sunt deja în ordine.")

            step += 1  # Incrementarea pasului

        # Explicăm că cel mai mare element a fost mutat în poziția finală
        print(f"Elementul {arr[n-i-1]} este acum în poziția corectă și nu mai este comparat.\n")

    # Afișare finală fără parametri extra
    print("Tabloul sortat final:")
    print_array(arr)

# Introducerea tabloului
input_str = input("Introdu numere separate prin spațiu: ")
arr = list(map(int, input_str.split()))

# Executarea algoritmului
bubble_sort(arr)
