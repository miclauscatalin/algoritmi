"requirement pip install termcolor"
import time
from termcolor import colored

def print_array(arr, highlight_idx=None, phase=None):
    """Afișează tabloul cu indecși și evidențiere vizuală."""
    # Afișăm indecșii
    print("Indecși:  ", end=" ")
    for i in range(len(arr)):
        print(f"{i:^3}", end=" ")
    print()

    # Afișăm valorile
    print("Valori:   ", end=" ")
    for i in range(len(arr)):
        if highlight_idx is not None and i in highlight_idx:  # Evidențiere verde pentru elementele analizate
            print(colored(f"{arr[i]:^3}", 'green'), end=" ")
        else:
            print(f"{arr[i]:^3}", end=" ")
    print()

    if phase:
        print(f"Faza: {phase}\n")
    else:
        print()

def print_buckets(buckets):
    """Afișează conținutul fiecărui tablou/bucket într-un mod vizual."""
    print("Tablou :")
    for i in range(10):
        bucket_str = " ".join(str(x) for x in buckets[i])
        print(f"{i}: {bucket_str}")
    print()

def radix_sort(arr):
    """Algoritmul Radix Sort """
    max_num = max(arr)  # Găsim valoarea maximă pentru a ști câte cifre are
    exp = 1  # Inițiem la unități (1, 10, 100 etc.)
    step = 1  # Pașii

    while max_num // exp > 0:  # Repetăm pentru fiecare poziție zecimală
        print(f"Pasul {step}: Sortăm după cifra la poziția {exp} (exp={exp}).")
        print_array(arr, phase=f"Sortăm după cifra {(exp)}")
        time.sleep(5)

        # Cream 10 "valori in tablou" pentru cifrele de la 0 la 9
        buckets = [[] for _ in range(10)]

        # Distribuim elementele în tablouri/buckets
        for num in arr:
            index = (num // exp) % 10
            buckets[index].append(num)

        print_buckets(buckets)
        time.sleep(5)

        # Reconstruim lista din tablou/buckets
        idx = 0
        for i in range(10):
            for num in buckets[i]:
                arr[idx] = num
                idx += 1

        print(f"Rezultatul după sortarea cifrei la poziția {exp}:")
        print_array(arr)
        time.sleep(5)

        # Trecem la următoarea poziție zecimală
        exp *= 10
        step += 1

    # Final - Tabloul sortat
    print("Tabloul sortat final:")
    print_array(arr)

# Introducerea tabloului
input_str = input("Introdu numere separate prin spațiu: ")
arr = list(map(int, input_str.split()))

# Executarea algoritmului
radix_sort(arr)
