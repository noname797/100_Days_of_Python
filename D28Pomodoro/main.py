from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
timer = None
mark = ""
START = False
end_count = 0

reps = 0

# TODO: Reset Mechanism


def reset_timer():
    window.after_cancel(timer)
    label1.config(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
    canvas.itemconfig(timer_text, text="00:00")
    checks.config(text="")
    global reps
    reps = 0
    start.config(state='active')
    reset.config(state='disabled')


def ended():
    global end_count
    end_count = 0
    global mark
    mark = "✔✔✔✔"
    window.after_cancel(timer)
    label1.config(text="End", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
    canvas.itemconfig(timer_text, text="00:00")
    checks.config(text=mark)
    global reps
    reps = 0
    start.config(state='active')
    reset.config(state='disabled')


# TODO: Countdown Mechanism
# time.sleep() wont work as the GUI is event driven and refreshes screen continuously
# Hence we can use "after" from tkinter


def countdown(count):
    global end_count
    global reps
    sec = "{:02d}".format(count % 60)
    minutes = "{:02d}".format(count//60)
    global mark
    mark = ""
    # OR

    # if sec < 10:
    #     sec = f"0{sec}"
    #
    # if minutes < 10:
    #     minutes = f"0{minutes}"

    new_time = f"{minutes}:{sec}"

    canvas.itemconfig(timer_text, text=new_time)

    if count >= 0:
        global timer
        timer = window.after(1000, countdown, count - 1)  # Calls countdown with input argument "count-1"
    else:
        start_timer()
        mark = ""
        for _ in range(reps//2):
            mark += "✔"

        checks.config(text=mark)

    if reps % 8 == 0:
        end_count += 1

    if end_count == 8:
        ended()


def check_start():
    global START
    START = True


def start_timer():
    start.config(state='disabled')
    reset.config(state='active')
    global mark
    mark = ""
    checks.config(text=mark)

    global reps
    reps += 1
    if reps % 2 != 0:
        countdown(int(WORK_MIN*60))
        label1.config(text="Work", fg=GREEN)
    elif reps % 8 == 0:
        countdown(int(LONG_BREAK_MIN*60))
        label1.config(text="Break", fg=RED)
    else:
        countdown(int(SHORT_BREAK_MIN*60))
        label1.config(text="Break", fg=PINK)


# TODO: Config UI

window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)
window.title("Pomodoro")

bg = PhotoImage(file="tomato.png")

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # "highlightthickness" removes the border
canvas.create_image(100, 112, image=bg)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# use colorhunt.co

# bg_img = Label(window, image=bg)
# bg_img.grid(column=1, row =1)

label1 = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
label1.grid(column=1, row=0)

start = Button(text="Start", font=(FONT_NAME, 10), highlightthickness=0, border=0, bg=YELLOW, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", font=(FONT_NAME, 10), highlightthickness=0, border=0, bg=YELLOW, command=reset_timer, state='disabled')
reset.grid(column=2, row=2)

checks = Label(text="", font=(FONT_NAME, 10), fg=GREEN, bg=YELLOW, highlightthickness=0, border=0)
checks.grid(column=1, row=3)

window.mainloop()
