from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Inter"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_button_fun():
    window.after_cancel(timer)
    timer_label["text"] = "timer"
    canvas.itemconfig(timer_text, text= "00:00")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)  # long break
        timer_label["text"] = "break"
        timer_label["fg"] = GREEN
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)  # work-break (2nd time)
        timer_label["text"] = "break"
        timer_label["fg"] = GREEN
    else:
        count_down(WORK_MIN * 60)
        timer_label["text"] = "work"
        timer_label["fg"] = RED


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(seconds):
    minutes_left = math.floor(seconds / 60)
    seconds_left = seconds % 60

    canvas.itemconfig(timer_text, text=f"{minutes_left:02}:{seconds_left:02}")
    if seconds > 0:
        global timer
        timer = window.after(1000, count_down, seconds - 1)
    else:
        start_timer()
        tick_mark = ""
        work_session = math.floor(reps/2)
        for i in range(work_session):
            tick_mark += "✔"
        tick_label["text"] = f"{tick_mark}"


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# label
timer_label = Label(text="timer", fg=GREEN, font=(FONT_NAME, 50, "bold"), bg=YELLOW)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(
    100, 125, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)


# button
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_button_fun)
reset_button.grid(column=2, row=2)

# tick label
tick_label = Label(text="", fg=GREEN, font=(FONT_NAME, 15, "bold"), bg=YELLOW)
tick_label.grid(column=1, row=3)


window.mainloop()
