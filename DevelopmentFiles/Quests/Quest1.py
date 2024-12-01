def quest1(tip: int):
    import tkinter as tk
    from tkinter import messagebox
    import os
    import sys

    def ShowTips():
        line=""
        all_tips=[]
        with open("messages.txt","r") as f:
            line=f.readline().strip()
            while line!="":
                all_tips.append(line)
                line=f.readline().strip()
            f.close()
        messagebox.showinfo("Brawo!", f"Twoja wskazówka {all_tips[tip]}")

    def on_button_click():
        user_input = entry.get()
        data=str(user_input.strip())
        
        if not data.isdigit():
            message_label.config(text=f"Nie rób sobie jaj!")
        else:
            if int(data)==52 or int(data)==25:
                message_label.config(text=f"DOBRZE!")
                ShowTips()
                with open("AnswerCorrect.txt", 'w') as f:
                    f.write("1")
                    f.close()
                sys.exit()
            else:
                message_label.config(text=f"Glupi , glupi!")
                with open("AnswerCorrect.txt", 'w') as f:
                    f.write("0")
                    f.close()
        entry.delete(0, tk.END)

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
    
#quest1(1)
