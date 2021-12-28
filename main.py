
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
CHECKMARK = ""
TIMER = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global REPS
    window.after_cancel(TIMER)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")
    REPS = 0




# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    work_reps = [1, 3 , 5, 7]
    short_break_sec = SHORT_BREAK_MIN * 60
    short_break_reps = [2, 4, 6]
    long_break_sec = LONG_BREAK_MIN * 60
    long_break_rep = 8
    if REPS in work_reps:
        count_down(work_sec)
        # Use of timer_lable.config since we already created and place the label down in the code below
        timer_label.config(text="Work Time!", foreground=GREEN)
    elif REPS in short_break_reps:
        count_down(short_break_sec)
        timer_label.config(text="5min Break!", foreground=PINK)
    elif REPS == 8:
        count_down(long_break_sec)
        timer_label.config(text="20min Break!", foreground=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global REPS,CHECKMARK,TIMER
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    # Unlike label and buttons where to edit is button_name.config, for canvas you need to use canvas.itemconfig(canvas_item)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        # Passes arguments to a function after a specific amount of time
       TIMER = window.after(1000,count_down, count - 1)
    else:
        start_timer()
        if REPS % 2 == 0:
            CHECKMARK += "✔"
            check_mark.config(text=CHECKMARK)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# highlightthickness=0 removes the rectangle border around a widget
# CANVAS PORTION
# canvas creation
canvas = Canvas(width= 200, height=224, bg=YELLOW, highlightthickness=0)
# Convert png to PhotoImage
file_image = PhotoImage(file="tomato.png")
# Placing tomato image on canvas,image argument requires Photoimage
canvas.create_image(100, 112, image=file_image)
# Placing text on canvas
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))


# Placing canvas on screen
canvas.grid(column=1, row=2)

# Button Portion
start_button = Button(text="Start",highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=3)
reset_button = Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(column=2, row=3)
# Label Portion
timer_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), foreground=GREEN,background=YELLOW)
timer_label.grid(column=1, row=1)
check_mark = Label(fg=GREEN, bg=YELLOW,font=(FONT_NAME, 15, "bold"))
check_mark.grid(column=1, row=3)


window.mainloop()