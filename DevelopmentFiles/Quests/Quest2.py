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
            f.close()
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
                f.close()
            self.master.destroy()  # Zamknięcie okna

        def wrong_choice(self):
            """Wyświetl komunikat o błędzie, gdy gracz kliknie niewłaściwy przycisk."""
            with open("AnswerCorrect.txt", 'w') as f:
                f.write("0")
                f.close()

            messagebox.showwarning("Błąd", "To nie jest właściwy wybór!")
            self.master.destroy()

    # Uruchomienie aplikacji
    root = tk.Tk()
    app = MatchingButtonsApp(root)
    root.mainloop()

#quest2(1)
