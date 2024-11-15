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

def update_columns(sequence, canvas, canvas_width, canvas_height):
    # Calculeaza numarul de 1 si 2 in secventa
    count_1s = sequence.count(1)
    count_2s = sequence.count(2)
    total = len(sequence)

    # Curata canvas-ul
    canvas.delete("all")

    # Defineste proprietatile coloanelor
    column_width = 100
    spacing = 100
    text_offset = 20
    column_y_offset = 200

    # Calculeaza coordonata x de start pentru a centra coloanele
    total_width = 2 * column_width + spacing
    start_x = (canvas_width - total_width) / 2

    # Coloana rosie pentru numarul de 1
    red_height = (count_1s / total) * canvas_height + 100
    red_x1 = start_x
    red_x2 = red_x1 + column_width
    canvas.create_rectangle(
        red_x1, canvas_height - red_height - column_y_offset,
        red_x2, canvas_height - column_y_offset,
        fill="red", outline="black"
    )
    canvas.create_text(
        (red_x1 + red_x2) / 2, canvas_height - column_y_offset + text_offset,
        text=f"1s: {count_1s}", fill="black"
    )

    # Coloana albastra pentru numarul de 2
    blue_height = (count_2s / total) * canvas_height + 100
    blue_x1 = red_x2 + spacing
    blue_x2 = blue_x1 + column_width
    canvas.create_rectangle(
        blue_x1, canvas_height - blue_height - column_y_offset,
        blue_x2, canvas_height - column_y_offset,
        fill="blue", outline="black"
    )
    canvas.create_text(
        (blue_x1 + blue_x2) / 2, canvas_height - column_y_offset + text_offset,
        text=f"2s: {count_2s}", fill="black"
    )

    # Bara orizontala pentru distributia generala
    bar_height = 40
    bar_y1 = canvas_height - 100
    bar_y2 = bar_y1 + bar_height
    current_width = 0
    for value in sequence:
        color = "red" if value == 1 else "blue"
        width = (1 / total) * canvas_width
        canvas.create_rectangle(
            current_width, bar_y1, current_width + width, bar_y2,
            fill=color, outline="black"
        )
        current_width += width
    canvas.create_text(
        canvas_width / 2, bar_y2 + text_offset,
        text=f"Total: {total}", fill="black"
    )

def main():
    n = 200  # Numarul de termeni pe care dorim sa-i generam
    sequence = []

    # Configurarea interfetei grafice
    root = tk.Tk()
    root.title("Vizualizare Secventa Kolakoski")

    canvas_width, canvas_height = 1500, 700  # Reduce inaltimea canvas-ului pentru a comprima elementele
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
    canvas.pack()

    # Generarea si afisarea secventei pas cu pas
    for i in range(1, n + 1):
        sequence = Kolakoski_sequence(i)
        update_columns(sequence, canvas, canvas_width, canvas_height)
        root.update()

    root.mainloop()

if __name__ == "__main__":
    main()
