def quest5(tip:int):
    import tkinter as tk
    from tkinter import messagebox
    import random
    def ShowTips():
        line=""
        all_tips=[]
        with open("messages.txt","r") as f:
            line=f.readline().strip()
            while line!="":
                all_tips.append(line)
                line=f.readline().strip()
            f.close()
        messagebox.showinfo("Brawo!", f"Twoja wskazówka: {all_tips[tip]}")

    class CableGame:
        def __init__(self, root):
            self.root = root
            self.root.title("Łączenie kolorowych kabli")
            self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
            self.canvas.pack()

            self.colors = ["red", "blue", "green", "pink"]
            self.points = {}
            self.connections = []
            self.start_point = None

            self.create_points()
            self.canvas.bind("<Button-1>", self.on_click)
            self.canvas.bind("<B1-Motion>", self.on_drag)
            self.canvas.bind("<ButtonRelease-1>", self.on_release)

        def create_points(self):
            for color in self.colors:
                x1, y1 = self.random_position()
                x2, y2 = self.random_position()
                self.points[(x1, y1)] = color
                self.points[(x2, y2)] = color

                self.canvas.create_oval(x1-10, y1-10, x1+10, y1+10, fill=color, outline=color)
                self.canvas.create_oval(x2-10, y2-10, x2+10, y2+10, fill=color, outline=color)

        def random_position(self):
            import random
            return random.randint(50, 550), random.randint(50, 350)

        def on_click(self, event):
            for (x, y), color in self.points.items():
                if (x-10 <= event.x <= x+10) and (y-10 <= event.y <= y+10):
                    self.start_point = (x, y)
                    return

        def on_drag(self, event):
            if self.start_point:
                self.canvas.delete("temp_line")
                self.canvas.create_line(self.start_point[0], self.start_point[1],
                                        event.x, event.y, fill=self.points[self.start_point], tags="temp_line")

        def on_release(self, event):
            if not self.start_point:
                return

            for (x, y), color in self.points.items():
                if (x-10 <= event.x <= x+10) and (y-10 <= event.y <= y+10):
                    if self.start_point != (x, y) and self.points[self.start_point] == color:
                        self.connections.append((self.start_point, (x, y)))
                        self.canvas.create_line(self.start_point[0], self.start_point[1],
                                                x, y, fill=color, width=3)
                        self.start_point = None
                        self.canvas.delete("temp_line")
                        self.check_win()
                        return

            self.start_point = None
            self.canvas.delete("temp_line")

        def check_win(self):
            random_result=random.choice([["Udało ci się połączyć wszystkie kable!","1"],["Doprowadziłeś do zwarcia","0"]])
            if len(self.connections) == len(self.colors):
                random_result=random.choice([["Udało ci się połączyć wszystkie kable!","1"],["Doprowadziłeś do zwarcia","0"]])
                messagebox.showinfo("Gratulacje!", random_result[0])
                ShowTips()
                with open("AnswerCorrect.txt",'w') as file:
                    file.write(random_result[1])
                    file.close()
                self.root.quit()

    root = tk.Tk()
    game = CableGame(root)
    root.mainloop()

#quest5(1)