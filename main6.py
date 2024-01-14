import tkinter as tk
from tkinter import messagebox

# global super arrays
super_array_x = [0, 0, 0, 0, 0, 0, 0, 0, 0]
super_array_o = [0, 0, 0, 0, 0, 0, 0, 0, 0]
valid_cell = None
movecount = 0

def super_check(a):
    # a = self.array
    sums = []
    for i in range(3):
        sums.append(a[i] + a[i + 1] + a[i + 2])
        sums.append(a[i] + a[i + 3] + a[i + 6])
    sums.append(a[0] + a[4] + a[8])
    sums.append(a[2] + a[4] + a[6])

    if 3 in sums or -3 in sums:
        return True
    else:
        return False


class ttbox:
    def __init__(self, root, index):
        self.index = index
        self.array = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.winner = None

        self.frame = tk.Frame(root, highlightthickness=2,
                              highlightbackground="black", highlightcolor="black")
        self.frame.grid(row=index // 3, column=index % 3, padx=5, pady=5)

        self.buttons = []
        self.create_buttons()

    def check(self):
        a = self.array
        sums = []
        for i in range(3):
            sums.append(a[i] + a[i + 1] + a[i + 2])
            sums.append(a[i] + a[i + 3] + a[i + 6])
        sums.append(a[0] + a[4] + a[8])
        sums.append(a[2] + a[4] + a[6])

        if 3 in sums:
            return True
        else:
            return False

    def make_entry(self, pos):
        global who, super_array_x, super_array_o, valid_cell, movecount
        movecount += 1
        print(valid_cell)

        if movecount == 1:
            a = self.array
            if a[pos] == 0:
                a[pos] = 1 if who else -1
                self.update_buttons()
                if self.check():
                    if who:
                        super_array_x[self.index] = 1
                    else:
                        super_array_o[self.index] = 1
                    if super_check(super_array_x) or super_check(super_array_o):
                        winner = "X" if who else "O"
                        messagebox.showinfo("Congratulations!",
                                            f"{winner} has won!!")

                who = not who
                valid_cell = pos
        elif self.index == valid_cell and movecount != 0:
            a = self.array
            if a[pos] == 0:
                a[pos] = 1 if who else -1
                self.update_buttons()
                if self.check():
                    if who:
                        super_array_x[self.index] = 1
                    else:
                        super_array_o[self.index] = 1
                    if super_check(super_array_x) or super_check(super_array_o):
                        winner = "X" if who else "O"
                        messagebox.showinfo("Congratulations!",
                                            f"{winner} has won!!")

                who = not who
                valid_cell = pos

        else:
            messagebox.showerror("Use proper box")

    def create_buttons(self):
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.frame, text=str(""),
                                   command=lambda x=i * 3 + j: self.make_entry(x), height=2, width=4)
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

        self.super_array_label_x = tk.Label(
            self.frame, text="Super Array X: " + str(super_array_x))
        self.super_array_label_x.grid(row=3, columnspan=3)
        self.super_array_label_y = tk.Label(
            self.frame, text="Super Array O: " + str(super_array_o))
        self.super_array_label_y.grid(row=4, columnspan=3)

    def update_buttons(self):
        for i in range(3):
            for j in range(3):
                val = self.array[i * 3 + j]
                if val == 1:
                    self.buttons[i][j].config(text="X")
                elif val == -1:
                    self.buttons[i][j].config(text="O")
                else:
                    self.buttons[i][j].config(text="")

        self.super_array_label_x.config(
            text="Super Array X: " + str(super_array_x))
        self.super_array_label_y.config(
            text="Super Array O: " + str(super_array_o))


root = tk.Tk()
root.title("Tic Tac Toe")
who = True

tt_boxes = []
for i in range(9):
    tt = ttbox(root, i)
    tt_boxes.append(tt)

root.mainloop()
