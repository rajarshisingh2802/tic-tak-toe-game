import tkinter as tk
from project import players
from project import Grid


root = tk.Tk()

win_width = 500
win_height = 500

screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()

center_x = int(screen_w/2 - win_width/2)
center_y = int(screen_h/2 - win_height/2)

root.geometry(f'{win_width}x{win_height}+{center_x}+{center_y}')
root.configure(bg="royalblue")

p1 = players()
p1.add(["player1","symbol",[]])
p2 = players()
p2.add(["player 2","symbol",[]])

chance1 = 1
game_over = False
def single_click(button,n,l,l2,l3):

    global tie
    global chance1
    global game_over
    sym = " "

    if game_over is True:
        return
    if chance1 == 1 :
        sym = "X"
        p1.records[2].append(Grid.magic_square[n])
        l.config(text="Player 2 Turn")

    else:
        sym = "O"
        p2.records[2].append(Grid.magic_square[n])
        l.config(text="Player 1 Turn")

    button.config(state="disabled",text=sym,bg="#D3D3D3")
    chance1 ^= 1

    if p1.won(p1.records[2]):
        tie = False
        l2.config(text=f"{p1.records[0]} Won !!!")
        l2.grid(row=0,column=0,sticky=tk.N,pady=8)
        game_over = True

    elif p2.won(p2.records[2]):
        l2.config(text=f"{p2.records[0]} Won !!!")
        l2.grid(row=0,column=0,sticky=tk.N,pady=8)
        tie = False
        game_over = True
    
    if len(p1.records[2]) == 5 and tie:
        l3.config(text="Its a tie")
        l3.grid(row=0,column=0,sticky=tk.N,pady=8)
        game_over = True


class fields(tk.Label):

    def __init__(self,parent,text):

        super().__init__(
            parent,
            bg="royalblue",
            text=text,
            width = 30,
            height = 5,
            font = ("Times New Roman",12,"bold"),
        )

class entry_fields(tk.Entry):

    def __init__(self,parent):
        super().__init__(
            parent,
            bg="#E799ED",
            highlightbackground="black",
            highlightthickness=2,
            fg="black",
            width=25,
            font = ("Times New Roman",10,"bold"),
        )
def start_screen():
    og_frame = tk.Frame(
        root,
        height = 500,
        width=500
    )
    og_frame.pack(fill="both", expand=True)

    frame = tk.Frame(
        og_frame,
        height =100,
        bg="royalblue",
    )
    frame.pack(fill="x",)
    frame.pack_propagate(False)
    head = tk.Label(
        frame,
        text = players.welcome(),
        justify="center",
        fg="#E799ED",
        bg="royalblue",
        font=("Times New Roman",18,"bold")
    )
    head.pack(fill="both",pady=10)

    frame1 = tk.Frame(
        og_frame,
        height=200,
        bg="royalblue",
    )
    frame1.pack(fill="x")
    frame1.pack_propagate(False)

    frame2 = tk.Frame(
        og_frame,
        height=200,
        bg="royalblue",
    )
    frame2.pack(fill="x",pady=0)
    frame2.pack_propagate(False)

    name_1 = fields(frame1,text="Enter your Name \nas player 1: ")
    name_1.pack(pady=10,side="left",padx=10)
    name_2 = fields(frame2,text="Enter your Name \nas player 2: ")
    name_2.pack(anchor="nw",side="left",padx=10)

    e1 = entry_fields(frame1)
    e1.pack(pady=10,side="right",padx=10)

    e2 = entry_fields(frame2)
    e2.pack(anchor="ne",padx=10,pady=40)

    next_b = tk.Button(
        frame2,
        text="NEXT",
        command=lambda: transition(og_frame,e1,e2),
        bg = "#E799ED",
        font=("Arial", 10, "bold"),
        width=15,
        height=2,
        highlightthickness=1,
        borderwidth=1,
    )
    next_b.pack(pady=20)
class Btn(tk.Button):
    def __init__(self,parent,command):

        super().__init__(
            parent,
            text="",
            command=command,
            bg = "#E799ED",
            font=("Arial", 24, "bold"),
            width=100,
            height=100,
            highlightthickness=1,
            borderwidth=1,
        )

tie = True
def game_screen():

    global chance1
    board = tk.Frame(
        root,bg = "black",
        width=308,
        height=308,
        highlightbackground="black",
        highlightthickness=2
        )
    board.grid(padx=96,pady=150)
    board.grid_propagate(False)

    for i in range(3):
        board.rowconfigure(i, weight=1)
        board.columnconfigure(i, weight=1)

    label = tk.Label(
        root,
        bg="royalblue",
        height=5,
        width=20,
        font = ("Times new Roman",15,"bold")
    )
    label.config(text="Player 1 Turn")
    label.grid(row=0,column=0,sticky=tk.N,pady=8)

    win_label = tk.Label(
        root,
        bg="royalblue",
        height=5,
        width=20,
        font = ("Times new Roman",15,"bold")   
    )

    tie_label = tk.Label(
        root,
        bg="royalblue",
        height=5,
        width=20,
        font = ("Times new Roman",15,"bold")        
    )
    cells = []
    for i in range(3):
        for j in range(3):
            cell = tk.Frame(
                board,
                width = 100,
                height = 100,
                bg="black"
            )
            cell.grid(row=i, column=j, sticky="nsew")
            cell.grid_propagate(False)
            cells.append(cell)
    
    buttons = []
    for index in range(9):

        new_btn = Btn(cells[index], command=lambda i=index: single_click(buttons[i], i,label,win_label,tie_label))
        new_btn.pack(fill="both", expand=True)
        buttons.append(new_btn)

def transition(frame,e1,e2):

    p1.records[0] = e1.get()
    p2.records[0] = e2.get()
    frame.destroy()

    game_screen()
start_screen()
root.mainloop()