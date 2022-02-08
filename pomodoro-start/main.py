from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
RESP = 0
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_times():
    window.after_cancel(TIMER) 
    canvas.itemconfig(show_time, text="00:00")
    label_time.config(text="Timer")
    marker.config(text="")

    global RESP
    RESP = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global RESP
    global label_time
    RESP += 1

    work_min = WORK_MIN * 60
    short_break_min = SHORT_BREAK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60

    if RESP % 8 == 0:
        count_down(long_break_min)
        label_time.config(text="Long Break")
        label_time.grid(column=1, row=0)
    elif RESP % 2 == 0:
        count_down(short_break_min)
        label_time.config(text="Short Break")
        label_time.grid(column=1, row=0)        
    else:
        count_down(work_min)
        label_time.config(text="Work Times")
        label_time.grid(column=1, row=0)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sce = count % 60
    global TIMER

    if count_sce < 10:
        count_sce = f"0{count_sce}"

    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(show_time, text=f"{count_min}:{count_sce}")
    if count > 0:
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(RESP/2)
        for n in range(work_sessions):
            marks += "✔"
        marker.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label_time = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
label_time.grid(column=1, row=0)

button_start = Button(text="Start", command=start_timer, highlightthickness=0)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", command=reset_times, highlightthickness=0)
button_reset.grid(column=2, row=2)

marker = Label(font=(FONT_NAME, 12, "bold"), fg=GREEN, bg=YELLOW)
marker.grid(column=1, row=3)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_png = PhotoImage(file="pomodoro-start/tomato.png")
canvas.create_image(100, 112, image=tomato_png)
show_time = canvas.create_text(100, 112, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)






window.mainloop()