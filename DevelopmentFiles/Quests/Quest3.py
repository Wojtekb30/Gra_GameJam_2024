def quest3(tip: int):
    import tkinter as tk
    from tkinter import messagebox
    import os

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

            self.master.destroy()

    root = tk.Tk()
    app = QuestApp(root)
    root.mainloop()
