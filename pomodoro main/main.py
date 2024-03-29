from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_button():
    window.after_cancel(timer)
    timer_label.config(text="Timer",fg = GREEN)
    check_label.config(text="")
    canvas.itemconfig(canvas_text,text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def s_button():
    global reps
    reps += 1
    work = WORK_MIN*60
    s_break = SHORT_BREAK_MIN*60
    l_break = LONG_BREAK_MIN*60
    if reps%2 == 0 and reps < 8:
        pomodoro(s_break)
        timer_label.config(text="Break",fg=PINK)
    elif reps == 8:
        pomodoro(l_break)
        timer_label.config(text="Break",fg=RED)
    else:
        pomodoro(work)
        timer_label.config(text="Work",fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def pomodoro(count):
    global timer
    if count%60 == 0:
        canvas.itemconfig(canvas_text,text=f"{int(count/60)}:00")
    elif count%60 in range(1,10):
        canvas.itemconfig(canvas_text, text=f"{int(count / 60)}:0{int(count%60)}")
    else:
        canvas.itemconfig(canvas_text, text=f"{int(count / 60)}:{int(count%60)}")
    if count > 0:
        timer = window.after(1000, pomodoro,count - 1)
    else:
        s_button()
        mark = ""
        for r in range(0,int(reps/2)):
            mark += "✔"
        check_label.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=30,bg = YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME,30,"bold"),fg=GREEN,bg=YELLOW)
timer_label.grid(row=0,column=1)

canvas = Canvas(window, width=200,height=224,bg= YELLOW)
image_tomato = PhotoImage(file="tomato.png")
canvas.create_image(102,112,image= image_tomato)
canvas_text = canvas.create_text(100,133,text="00:00",font=(FONT_NAME,30,"bold"),fill="white")
canvas.grid(row=1,column=1)

start_button = Button(text= "Start", font=(FONT_NAME,10), command=s_button)
start_button.grid(row=2,column=0)

check_label = Label(text="",bg=YELLOW,fg=GREEN,font=(FONT_NAME,13,"bold"))
check_label.grid(row=3,column=1)

reset_button = Button(text= "Reset", font=(FONT_NAME,10), command=reset_button)
reset_button.grid(row=2,column=2)

window.mainloop()