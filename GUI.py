import tkinter as tk
from project import players

root = tk.Tk()

win_width = 500
win_height = 500

screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()

center_x = int(screen_w/2 - win_width/2)
center_y = int(screen_h/2 - win_height/2)

root.geometry(f'{win_width}x{win_height}+{center_x}+{center_y}')
root.configure(bg="royalblue")

def single_click(button,sym):
    print("button clicked")

    button.config(state="disabled",text=sym)

def start_screen():
    frame = tk.Frame(
        root,
        height =100,
        bg="green",
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
        root,
        height=200,
        bg="#98ff98",
    )
    frame1.pack(fill="x")
    frame1.pack_propagate(False)

    label1 = tk.Label(
        frame1,
        bg="red",
        text="Name :\nSymbol : ",
        font = ("Times New Roman",9,"bold"),
        width=int(win_width/2),
    )
    label1.pack(fill="y",side="left")




def game_screen():
    board = tk.Frame(
        root,bg = "black",
        width=308,
        height=308,
        highlightbackground="black",
        highlightthickness=2
        )
    board.grid(padx=96,pady=96)
    board.grid_propagate(False)

    for i in range(3):
        board.rowconfigure(i, weight=1)
        board.columnconfigure(i, weight=1)
    for r in range(3):
        for c in range(3):
            cell = tk.Frame(board,bg="white",width=100,height=100)
            cell.grid(row=r,column=c, padx=2,pady=2,sticky="nsew")
            cell.grid_propagate(False)
            
            button = tk.Button(
                cell,
                width=100,
                height=100,
                borderwidth=0,
                highlightthickness=0,
                bg="#E799ED",
                font=("Arial", 24, "bold")
                )
            button.config(command=lambda b=button:single_click(b,sym="X"))
            button.pack()

start_screen()

root.mainloop()