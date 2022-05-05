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
LONG_BREAK_MIN = 30
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    top_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    # If it's the 1st/3rd/5th/7th rep:

    if reps % 8 == 0:
        count_down(long_break_seconds)
        top_label.config(text="Break", font=(FONT_NAME, 45), fg=RED, bg=YELLOW)
    elif reps % 2 == 0:
        count_down(short_break_seconds)
        top_label.config(text="Break", font=(FONT_NAME, 45), fg=PINK, bg=YELLOW)
    else:
        count_down(work_seconds)
        top_label.config(text="Work", font=(FONT_NAME, 45), fg=GREEN, bg=YELLOW)
    # count_down(1 * 60)
    # If its the 8th rep:
    # if its the 2nd 4th or 5th


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    # How to get the timer in seconds and minutes
    count_min = math.floor(count / 60)
    # Get the seconds left after minutes so % to get the remainder
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # prints the timer in "00:00"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)


timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)


top_label = Label(text="Timer", font=(FONT_NAME, 45), fg=GREEN, bg=YELLOW)
top_label.grid(column=2, row=1)


check_marks = Label(fg=GREEN, bg=YELLOW, font=25)
check_marks.grid(column=2, row=4)


start_button = Button(text="Start", command=start_timer)
start_button.grid(column=1, row=3)


reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=3, row= 3)


window.mainloop()