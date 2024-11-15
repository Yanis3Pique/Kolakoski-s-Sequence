import tkinter as tk
import time

def Kolakoski_sequence(n):
    sequence = [1, 2, 2]
    index = 2
    while len(sequence) < n:
        next_value = 1 if sequence[-1] == 2 else 2
        sequence.extend([next_value] * sequence[index])
        index += 1
    return sequence[:n]

def update_sequence_display(sequence, label):
    # Actualizeaza afisarea secventei in interfata
    label.config(text=' '.join(map(str, sequence)))
    label.update()

def main():
    n = 20  # Numarul de termeni pe care dorim sa-i generam
    sequence = []

    # Configurarea interfetei grafice
    root = tk.Tk()
    root.title("Secventa Kolakoski")
    label = tk.Label(root, text='', font=('Helvetica', 16), padx=20, pady=20)
    label.pack()

    # Generarea si afisarea secventei pas cu pas
    for i in range(1, n + 1):
        sequence = Kolakoski_sequence(i)
        update_sequence_display(sequence, label)
        root.update()
        time.sleep(0.5)

    root.mainloop()

if __name__ == "__main__":
    main()