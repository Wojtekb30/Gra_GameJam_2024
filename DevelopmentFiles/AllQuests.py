import tkinter as tk
from tkinter import messagebox
import random
import pygame
import sys
import math

# --- quest1 ---
def quest1(tip: int):
    def ShowTips():
        line = ""
        all_tips = []
        with open("messages.txt", "r") as f:
            line = f.readline().strip()
            while line != "":
                all_tips.append(line)
                line = f.readline().strip()
        messagebox.showinfo("Brawo!", f"Twoja wskazówka {all_tips[tip]}")

    def on_button_click():
        user_input = entry.get()
        data = str(user_input.strip())

        if not data.isdigit():
            message_label.config(text=f"Nie rób sobie jaj!")
        else:
            if int(data) == 52 or int(data) == 25:
                message_label.config(text=f"DOBRZE!")
                ShowTips()
                with open("AnswerCorrect.txt", 'w') as f:
                    f.write("1")
            else:
                message_label.config(text=f"Glupi , glupi!")
                with open("AnswerCorrect.txt", 'w') as f:
                    f.write("0")
        entry.delete(0, tk.END)
        root.after(1000, root.destroy)  # Close window after 1 second

    def on_entry_return(event):
        on_button_click()

    root = tk.Tk()
    root.title("Zgadnij liczbe")
    root.geometry("400x200")

    title_label = tk.Label(root, text="Dwie cyfry , suma 7 różnica 3", font=("Arial", 16))
    title_label.pack(pady=10)

    entry = tk.Entry(root, font=("Arial", 14))
    entry.pack(pady=10)

    submit_button = tk.Button(root, text="Check", font=("Arial", 12), command=on_button_click)
    submit_button.pack(pady=5)

    message_label = tk.Label(root, text="", font=("Arial", 14), fg="blue")
    message_label.pack(pady=10)

    entry.bind("<Return>", on_entry_return)

    root.mainloop()

#----quest 2-----
def quest2(tip: int):
    import tkinter as tk
    from tkinter import messagebox

    def ShowTips():
        line = ""
        all_tips = []
        with open("messages.txt", "r") as f:
            line = f.readline().strip()
            while line != "":
                all_tips.append(line)
                line = f.readline().strip()
        messagebox.showinfo("Brawo!", f"Twoja wskazówka: {all_tips[tip]}")

    class MatchingButtonsApp:
        def __init__(self, master):
            self.master = master
            master.title("Dopasuj przycisk")
            master.geometry("400x200")

            # Instrukcja
            self.label = tk.Label(master, text="Które ze zwierząt nie pasuje?", font=("Arial", 12))
            self.label.pack(pady=10)

            # Tworzenie przycisków
            self.target_button = tk.Button(master, text="Panda", bg="red", fg="white", command=self.wrong_choice)
            self.target_button.pack(pady=5)

            self.wrong_button_1 = tk.Button(master, text="Leniwiec", bg="green", fg="white", command=self.wrong_choice)
            self.wrong_button_1.pack(pady=5)

            self.wrong_button_2 = tk.Button(master, text="Lemur", bg="blue", fg="white", command=self.correct_choice)
            self.wrong_button_2.pack(pady=5)

        def correct_choice(self):
            """Zakończ program, gdy gracz kliknie właściwy przycisk."""
            ShowTips()
            with open("AnswerCorrect.txt", 'w') as f:
                f.write("1")
            self.master.after(1000, self.master.destroy)  # Close window after 1 second

        def wrong_choice(self):
            """Wyświetl komunikat o błędzie, gdy gracz kliknie niewłaściwy przycisk."""
            with open("AnswerCorrect.txt", 'w') as f:
                f.write("0")
            messagebox.showwarning("Błąd", "To nie jest właściwy wybór!")
            self.master.after(1000, self.master.destroy)  # Close window after 1 second

    # Uruchomienie aplikacji
    root = tk.Tk()
    app = MatchingButtonsApp(root)
    root.mainloop()


# --- quest3 ---
def quest3(tip: int):
    def ShowTips():
        line = ""
        all_tips = []
        with open("messages.txt", "r") as f:
            line = f.readline().strip()
            while line != "":
                all_tips.append(line)
                line = f.readline().strip()
        messagebox.showinfo("Brawo!", f"Twoja wskazówka: {all_tips[tip]}")

    class QuestApp:
        def __init__(self, master):
            self.master = master
            master.title("Zagadka dla inteligentych")
            master.geometry("400x200")

            self.label = tk.Label(master, text="2 + 2 × 2 =", font=("Arial", 16))
            self.label.pack(pady=20)

            self.entry = tk.Entry(master, font=("Arial", 14))
            self.entry.pack(pady=10)

            self.submit = tk.Button(master, text="Odpowiedz", bg="lightblue", font=("Arial", 14), command=self.check)
            self.submit.pack(pady=10)

        def check(self):
            user_input = self.entry.get().strip()

            try:
                answer = int(user_input)
            except ValueError:
                messagebox.showerror("Błąd", "Proszę wprowadzić liczbę.")
                return

            if answer == 6:
                message = "Gracz jest nudny"
                score = 0
            elif answer == 8:
                message = "Gratuluję za commonsense"
                ShowTips()
                score = 1
            else:
                message = "Womp Womp"
                score = 0

            messagebox.showinfo("Wynik", message)

            try:
                with open("AnswerCorrect.txt", "w") as file:
                    file.write(str(score))
            except IOError as e:
                messagebox.showerror("Błąd", f"Nie można zapisać pliku: {e}")
                return

            self.master.after(1000, self.master.destroy)  # Close window after 1 second

    root = tk.Tk()
    app = QuestApp(root)
    root.mainloop()

# --- quest4 ---
def quest4(tip: int):
    # Initialize Pygame
    pygame.init()

    # Window settings
    WIDTH, HEIGHT = 800, 600
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Spróbuj swoich szans")

    # Color definitions
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (220, 20, 60)
    GREEN = (34, 139, 34)
    BLUE = (30, 144, 255)
    YELLOW = (255, 215, 0)
    ORANGE = (255, 165, 0)
    PURPLE = (128, 0, 128)

    COLORS = [RED, BLACK, GREEN, BLUE, YELLOW, ORANGE, PURPLE]
    CENTER = (WIDTH // 2, HEIGHT // 2)
    RADIUS = 250
    NUM_SECTORS = 12
    ANGLE_PER_SECTOR = 360 / NUM_SECTORS

    WINNING_SECTORS = [2, 5, 8, 11]  # Indices of winning sectors (1/3 probability)
    clock = pygame.time.Clock()

    def ShowTips():
        line = ""
        all_tips = []
        with open("messages.txt", "r") as f:
            line = f.readline().strip()
            while line != "":
                all_tips.append(line)
                line = f.readline().strip()
        messagebox.showinfo("Brawo!", f"Twoja wskazówka: {all_tips[tip]}")

    def draw_wheel(surface, center, radius, sectors, angle):
        start_angle = math.radians(angle)
        font = pygame.font.SysFont(None, 24)
        for i in range(sectors):
            end_angle = start_angle + math.radians(ANGLE_PER_SECTOR)
            color = COLORS[i % len(COLORS)]
            pygame.draw.polygon(
                surface,
                color,
                [
                    center,
                    (
                        center[0] + radius * math.cos(start_angle),
                        center[1] + radius * math.sin(start_angle)
                    ),
                    (
                        center[0] + radius * math.cos(end_angle),
                        center[1] + radius * math.sin(end_angle)
                    )
                ]
            )
            pygame.draw.line(surface, BLACK, center,
                             (
                                 center[0] + radius * math.cos(start_angle),
                                 center[1] + radius * math.sin(start_angle)
                             ), 2)
            start_angle = end_angle

    def rotate_wheel():
        global angle, spin_speed, spinning
        if spinning:
            angle += spin_speed
            spin_speed *= 0.99
            if spin_speed < 0.1:
                spinning = False
                result_index = int((angle / 360) % NUM_SECTORS)
                if result_index in WINNING_SECTORS:
                    ShowTips()
                    with open("AnswerCorrect.txt", "w") as f:
                        f.write("1")
                else:
                    with open("AnswerCorrect.txt", "w") as f:
                        f.write("0")

    running = True
    angle = 0
    spin_speed = 5
    spinning = True
    while running:
        WINDOW.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_wheel(WINDOW, CENTER, RADIUS, NUM_SECTORS, angle)
        rotate_wheel()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

# --- quest5 ---
def quest5(tip: int):
    def ShowTips():
        line = ""
        all_tips = []
        with open("messages.txt", "r") as f:
            line = f.readline().strip()
            while line != "":
                all_tips.append(line)
                line = f.readline().strip()
        messagebox.showinfo("Brawo!", f"Twoja wskazówka: {all_tips[tip]}")

    def on_button_click():
        try:
            guess = int(entry.get())
            if guess < 1 or guess > 10:
                message_label.config(text="Proszę podać liczbę między 1 a 10.")
                return
        except ValueError:
            message_label.config(text="Proszę podać prawidłową liczbę.")
            return
        
        if guess == target_number:
            message_label.config(text="Brawo! Zgadłeś liczbę!")
            ShowTips()
            with open("AnswerCorrect.txt", 'w') as f:
                f.write("1")
        else:
            message_label.config(text="Niestety, spróbuj ponownie!")
            with open("AnswerCorrect.txt", 'w') as f:
                f.write("0")
        
        root.after(1000, root.destroy)  # Close window after 1 second

    def on_entry_return(event):
        on_button_click()

    target_number = random.randint(1, 10)  # Random number between 1 and 10

    root = tk.Tk()
    root.title("Zgadnij liczbę")
    root.geometry("400x200")

    title_label = tk.Label(root, text="Zgadnij liczbę od 1 do 10", font=("Arial", 16))
    title_label.pack(pady=10)

    entry = tk.Entry(root, font=("Arial", 14))
    entry.pack(pady=10)

    submit_button = tk.Button(root, text="Sprawdź", font=("Arial", 12), command=on_button_click)
    submit_button.pack(pady=5)

    message_label = tk.Label(root, text="", font=("Arial", 14), fg="blue")
    message_label.pack(pady=10)

    entry.bind("<Return>", on_entry_return)

    root.mainloop()
