import time
from termcolor import colored

def print_array(arr, current_idx=None, insert_idx=None, sorted_idx=None, temp=None):
    """Afișează tabloul cu indecși și evidențierea vizuală a elementelor."""
    # Afișăm indecșii
    print("Indecși:  ", end=" ")
    for i in range(len(arr)):
        print(f"{i:^3}", end=" ")
    print()  # Linie nouă

    # Afișăm elementele din tabloul actual
    print("Valori:   ", end=" ")
    for i in range(len(arr)):
        if i == current_idx:  # Elementul curent (verde)
            print(colored(f"{arr[i]:^3}", 'green'), end=" ")
        elif i == insert_idx:  # Poziția de inserare (cyan)
            print(colored(f"{arr[i]:^3}", 'cyan'), end=" ")
        elif sorted_idx is not None and i <= sorted_idx:  # Elemente deja sortate (galben)
            print(colored(f"{arr[i]:^3}", 'yellow'), end=" ")
        else:  # Restul elementelor
            print(f"{arr[i]:^3}", end=" ")
    print()  # Linie nouă

    # Afișăm valoarea temporară (temp)
    if temp is not None:
        print(f"TEMP: {colored(temp, 'red')}\n")
    else:
        print()

def insertion_sort(arr):
    step = 1  # Inițializarea pașilor
    for i in range(1, len(arr)):
        temp = arr[i]  # Elementul curent care trebuie inserat
        j = i - 1

        print(f"Pasul {step}: Inserăm elementul {temp}.")
        print_array(arr, current_idx=i, sorted_idx=i-1, temp=temp)
        time.sleep(5)  # Pauză de 5 secunde pentru vizualizare

        # Mutăm elementele mai mari decât temp cu o poziție în dreapta
        while j >= 0 and arr[j] > temp:
            print(f"Comparam {temp} cu {arr[j]} - {temp} este mai mic, deci mutăm {arr[j]} la dreapta.")
            arr[j + 1] = arr[j]  # Mutăm elementul în dreapta
            print_array(arr, current_idx=i, insert_idx=j + 1, sorted_idx=i-1, temp=temp)
            time.sleep(5)
            j -= 1

        # Inserăm elementul pe poziția corectă
        arr[j + 1] = temp
        print(f"Inserăm {temp} la poziția {j + 1}.")
        print_array(arr, sorted_idx=i)  # Evidențiem partea sortată
        time.sleep(5)

        step += 1  # Incrementarea pasului

    # Afișăm tabloul final sortat
    print("Tabloul sortat final:")
    print_array(arr)

# Introducerea tabloului
input_str = input("Introdu numere separate prin spațiu: ")
arr = list(map(int, input_str.split()))

# Executarea algoritmului
insertion_sort(arr)
import time
from termcolor import colored

def print_array(arr, current_idx=None, insert_idx=None, sorted_idx=None):
    """Afișează tabloul cu evidențierea elementului curent și a elementelor sortate."""
    for i in range(len(arr)):
        if i == current_idx:  # Elementul curent pe care îl inserăm
            print(colored(arr[i], 'green'), end=' ')
        elif i == insert_idx:  # Poziția în care încercăm să inserăm
            print(colored(arr[i], 'cyan'), end=' ')
        elif sorted_idx is not None and i <= sorted_idx:  # Elementele deja sortate
            print(colored(arr[i], 'yellow'), end=' ')
        else:  # Elementele nesortate
            print(arr[i], end=' ')
    print()  # Linie nouă

def insertion_sort(arr):
    step = 1  # Inițializarea pașilor
    for i in range(1, len(arr)):
        key = arr[i]  # Elementul curent care trebuie inserat
        j = i - 1
        
        print(f"Pasul {step}: Inserăm elementul {key}.")
        print_array(arr, current_idx=i, sorted_idx=i-1)
        time.sleep(5)  # Pauză de 5 secunde pentru vizualizare
        
        # Mutăm elementele mai mari decât key cu o poziție în dreapta
        while j >= 0 and arr[j] > key:
            print(f"Comparam {key} cu {arr[j]} - {key} este mai mic, deci mutăm {arr[j]} la dreapta.")
            arr[j + 1] = arr[j]  # Mutăm elementul în dreapta
            j -= 1
            print_array(arr, current_idx=i, insert_idx=j + 1, sorted_idx=i-1)
            time.sleep(5)

        # Inserăm elementul pe poziția corectă
        arr[j + 1] = key
        print(f"Inserăm {key} la poziția {j + 1}.")
        print_array(arr, sorted_idx=i)  # Evidențiem partea sortată
        time.sleep(5)
        
        step += 1  # Incrementarea pasului
    
    # Afișăm tabloul final sortat
    print("Tabloul sortat final:")
    print_array(arr)

# Introducerea tabloului
input_str = input("Introdu numere separate prin spațiu: ")
arr = list(map(int, input_str.split()))

# Executarea algoritmului
insertion_sort(arr)
