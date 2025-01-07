

#def secvential(arr, x):
#    for i in arr:
#        if i == x:
#            print(f"Elementul {x} a fost găsit. la pozitia ")
#            return
#    print(f"Elementul {x} nu a fost găsit.")

#print("Introdu sirul de numere separat prin spațiu:")
#arr = list(map(int, input().split()))  # Citire și conversie într-o listă de întregi
#x = int(input("Introdu elementul de căutat: "))
#secvential(arr, x)
def secvential(arr, x):
    for index, value in enumerate(arr):  # enumerate pentru a obține atât indexul, cât și valoarea
        if value == x:
            print(f"Elementul {x} a fost găsit la poziția {index+1}.")
            return  # Ieșim din funcție după ce găsim prima apariție
    print(f"Elementul {x} nu a fost găsit.")

# Citim lista de numere și elementul căutat
print("Introdu sirul de numere separat prin spațiu:")
arr = list(map(int, input().split()))  # Conversie într-o listă de numere întregi
x = int(input("Introdu elementul de căutat: "))
secvential(arr, x)
