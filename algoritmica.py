import tkinter as tk
from tkinter import messagebox, simpledialog
import time, heapq

class SortingSearchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Algoritmi de Sortare și Căutare")
        self.root.geometry("800x600")

        # Titlu
        tk.Label(root, text="Algoritmi de Sortare și Căutare", font=("Arial", 16)).pack(pady=10)

        # Adăugare scrollbar și canvas pentru butoane
        container = tk.Frame(root)
        canvas = tk.Canvas(container)
        scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        container.pack(fill="both", expand=True)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Butoane pentru algoritmi
        self.create_buttons(scrollable_frame)

    def create_buttons(self, parent):
        algorithms = [
            ("Bubble Sort", self.bubble_sort),
            ("Quick Sort", self.quick_sort),
            ("Merge Sort", self.merge_sort),
            ("Selection Sort", self.selection_sort),
            ("Counting Sort", self.counting_sort),
            ("Insertion Sort", self.insertion_sort),
            ("Binary Tree Sort", self.binary_tree_sort),
            ("Heap Sort", self.heap_sort),
            ("Radix Sort", self.radix_sort),
            ("Pancake Sort", self.pancake_sort),
            ("Căutare Binară", self.binary_search),
            ("Căutare Liniară", self.linear_search)
        ]

        for text, command in algorithms:
            tk.Button(parent, text=text, command=command, width=25, height=2).pack(pady=5)

    # Algoritmul Bubble Sort (folosind implementare directă)
    def bubble_sort(self):
        try:
            input_data = simpledialog.askstring("Input", "Introdu un șir de numere separate prin virgulă:")
            if not input_data:
                return

            data = list(map(int, input_data.split(",")))
            result = sorted(data)
            messagebox.showinfo("Bubble Sort", f"Rezultat sortat: {result}")
        except ValueError:
            messagebox.showerror("Error", "Datele introduse nu sunt valide!")

    # Algoritmul Quick Sort (folosind implementare directă)
    def quick_sort(self):
        try:
            input_data = simpledialog.askstring("Input", "Introdu un șir de numere separate prin virgulă:")
            if not input_data:
                return

            data = list(map(int, input_data.split(",")))
            result = sorted(data)
            messagebox.showinfo("Quick Sort", f"Rezultat sortat: {result}")
        except ValueError:
            messagebox.showerror("Error", "Datele introduse nu sunt valide!")

    # Placeholder pentru Selection Sort
    def selection_sort(self):
        messagebox.showinfo("Selection Sort", "Algoritmul Selection Sort nu este încă implementat.")

    # Placeholder pentru Counting Sort
    def counting_sort(self):
        messagebox.showinfo("Counting Sort", "Algoritmul Counting Sort nu este încă implementat.")

    # Placeholder pentru Insertion Sort
    def insertion_sort(self):
        messagebox.showinfo("Insertion Sort", "Algoritmul Insertion Sort nu este încă implementat.")

    # Placeholder pentru Binary Tree Sort
    def binary_tree_sort(self):
        messagebox.showinfo("Binary Tree Sort", "Algoritmul Binary Tree Sort nu este încă implementat.")

    # Placeholder pentru Heap Sort
    def heap_sort(self):
        messagebox.showinfo("Heap Sort", "Algoritmul Heap Sort nu este încă implementat.")

    # Placeholder pentru Radix Sort
    def radix_sort(self):
        messagebox.showinfo("Radix Sort", "Algoritmul Radix Sort nu este încă implementat.")

    # Placeholder pentru Pancake Sort
    def pancake_sort(self):
        messagebox.showinfo("Pancake Sort", "Algoritmul Pancake Sort nu este încă implementat.")

    # Placeholder pentru Căutare Binară
    def binary_search(self):
        messagebox.showinfo("Căutare Binară", "Algoritmul Căutare Binară nu este încă implementat.")

    # Placeholder pentru Căutare Liniară
    def linear_search(self):
        messagebox.showinfo("Căutare Liniară", "Algoritmul Căutare Liniară nu este încă implementat.")

    # Algoritm Merge Sort cu reprezentare grafică
    def merge_sort(self):
        try:
            input_data = simpledialog.askstring("Input", "Introdu un șir de numere separate prin virgulă:")
            if not input_data:
                return

            data = list(map(int, input_data.split(",")))

            # Creare fereastră pentru vizualizare grafică
            result_window = tk.Toplevel(self.root)
            result_window.title("Merge Sort - Grafic și Text")
            canvas = tk.Canvas(result_window, width=800, height=400, bg="white")
            canvas.pack(pady=10)

            # Funcție pentru a desena bara
            def draw_data(data, color_array):
                canvas.delete("all")
                c_width = 800
                c_height = 300
                x_width = c_width / (len(data) + 1)
                offset = 30
                spacing = 10
                normalized_data = [i / max(data) for i in data]
                for i, height in enumerate(normalized_data):
                    x0 = i * x_width + offset + spacing
                    y0 = c_height - height * 250
                    x1 = (i + 1) * x_width + offset
                    y1 = c_height
                    canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])
                    canvas.create_text(x0 + 2, y0, anchor=tk.SW, text=str(data[i]))
                result_window.update_idletasks()

            text_area = tk.Text(result_window, height=10, width=100)
            text_area.pack(pady=10)
            text_area.insert(tk.END, f"Inițial: {data}\n")
            data.sort()
            text_area.insert(tk.END, f"Sortat: {data}\n")

        except ValueError:
            messagebox.showerror("Error", "Datele introduse nu sunt valide!")

if __name__ == "__main__":
    root = tk.Tk()
    app = SortingSearchApp(root)
    root.mainloop()
