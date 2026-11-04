import tkinter as tk
import math

window = tk.Tk()

window.title("a little surprise for you..")

window.geometry("650x550")

window.configure(bg="#FFF0F5")

window.resizable(False,False)

welcome = tk.Label(
    window,
    text="you've got mail!",
    font=("Arial", 26, "bold"),
    bg="#FFF0F5",
    fg="#D65A8A"
)

welcome.pack(pady=40)

canvas = tk.Canvas(
    window,
    width=450,
    height=380,
    bg="#FFF0F5",
    highlightthickness=0
)
canvas.pack()

canvas.create_rectangle(
    75, 70, 375, 240,
    fill="#F8AFC5",
    outline="#D65A8A",
    width=3
)

canvas.create_polygon(
    75, 70,
    225, 175,
    375, 70,
    fill="#FFD1DF",
    outline="#D65A8A",
    width=3
)

canvas.create_text(
    225, 150,
    text="♡",
    font=("Arial", 42),
    fill="#E84378"
)

canvas.create_text(
    225, 275,
    text="click the envelope ♡",
    font=("Arial", 15),
    fill="#B94E76"
)

def open_letter(event):

    canvas.delete("all")
    
    points = [] 
    
    for i in range(361):
        t = math.radians(i)
        
        x = 16 * math.sin(t) ** 3
        y = (
            13 * math.cos(t)
            - 5 * math.cos(2 * t) 
            - 2 * math.cos(3 * t)
            - math.cos(4 * t)
        )
        
        points.append((225 + x * 8, 140 - y * 8))
        
    def draw_heart(index=1):
        if index < len(points):
            x1, y1 = points[index - 1]
            x2, y2 = points[index] 
            
            canvas.create_line(
                x1, y1, x2, y2,
                fill="#E84378",
                width=4
            )
            
            window.after(8, draw_heart, index + 1) 
            
        else:
            canvas.create_text(
            225, 295, 
            text=" type your message here ",
            font=("Arial", 17, "bold"),
            fill="#D65A8A",
            width=420
        )
        
    draw_heart()
        
    

  
  
canvas.bind("<Button-1>", open_letter)

window.mainloop()