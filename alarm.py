# Importing all the necessary libraries to form the alarm clock:
from tkinter import *  # Tkinter module belongs to a standard library of GUI in Python. It helps us to create a dialog box with any information that we want to provide or get from the users.
from tkinter import messagebox
import datetime  # Datetime and time modules in python help us to work with the dates and time of the current day when the user is operating python and to manipulate it too.
import time
import pyttsx3
import pytz


def welcomeMessage():
    return messagebox.showinfo("message", f"Your time is up!.")


def alarm(
    set_alarm_timer,
):  # Define a function named as alarm() which takes the argument of (set_alarm_timer).It contains a while loop with a Boolean function True which makes the program automatic to work.
    while True:
        time.sleep(
            1
        )  # time.sleep(1) halts the execution of the further commands given until we get the time value from the user later in the code and returns the background thread of the clock time going on at a regular interval.
        current_time = (
            datetime.datetime.now()
        )  # Get the current time using current_time which takes the argument of datetime.datetime.now().
        now = current_time.strftime(
            "%H:%M:%S"
        )  # now is used to print the time and date is used to print the current date by string conversion using strftime().
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:", date)
        print(now)
        clock.iconify()
        if now >= set_alarm_timer:
            print("Time to Wake up")
            engine = pyttsx3.init()  # object creation
            """ RATE"""
            rate = engine.getProperty(
                "rate"
            )  # getting details of current speaking rate
            print(rate)  # printing current voice rate
            engine.setProperty("rate", 180)  # setting up new voice rate
            """VOLUME"""
            volume = engine.getProperty(
                "volume"
            )  # getting to know current volume level (min=0 and max=1)
            print(volume)  # printing current volume level
            engine.setProperty(
                "volume", 1.0
            )  # setting up volume level  between 0 and 1
            """VOICE"""
            voices = engine.getProperty("voices")  # getting details of current voice
            # engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
            engine.setProperty(
                "voice", voices[17].id
            )  # changing index, changes voices. 1 for female
            engine.say("Boss")
            engine.say("You ran out of Time!")
            engine.say("It's time for you to Go!")
            engine.runAndWait()
            engine.stop()
            welcomeMessage()
            break


def actual_time():  # Define another function here named actual_time() which takes in the user value for setting the alarm in the string format. The same argument of (set_alarm_timer) as alarm before to execute the while loop which we further use while making GUI.
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"  # If loop suggests that if the user input time set_alarm_timer matches with the while loop ongoing time now, the message is printed as” Time to Wake up”.
    alarm(set_alarm_timer)


clock = Tk()  # To Initialize tkinter, we pass a command under the name clock as Tk().

clock.title("Python programmed Alarm Clock!")
clock.resizable(False, False)
clock.geometry(
    "700x480+600+300"
)  # The dialog box has the title as DataFlair Alarm Clock with a geometry of (400*200). We pass on the heading to mention the time format for 24 hours using time_format.
# Add Frame
frame1 = Frame(clock, height=130, width=180, bg="#EEB422", bd=1, relief=FLAT).place(
    x=0, y=0
)
frame2 = Frame(clock, height=130, width=510, bg="#ED9121", bd=1, relief=FLAT).place(
    x=190, y=0
)
frame3 = Frame(clock, height=20, width=700, bg="#4A4A4A", bd=1, relief=RAISED).place(
    x=0, y=130
)
frame4 = Frame(clock, height=330, width=700, bg="#212121", bd=1, relief=FLAT).place(
    x=0, y=150
)
frame5 = Frame(clock, height=130, width=10, bg="#4A4A4A", bd=1, relief=RAISED).place(
    x=180, y=0
)
# Labels
label_date_now = Label(text="Current Date", bg="#EEB422", font="verdana 20 bold")
label_date_now.place(x=10, y=35)
label_time_now = Label(text="Current Time", bg="#EEB422", font="verdana 20")
label_time_now.place(x=20, y=60)
# Clock
IST = pytz.timezone("Europe/Zurich")


def update_clock():
    raw_TS = datetime.datetime.now(IST)
    date_now = raw_TS.strftime("%d. %b. %Y")
    time_now = raw_TS.strftime("%H:%M:%S %p")
    label_date_now.config(text=date_now)
    label_time_now.config(text=time_now)
    label_time_now.after(1000, update_clock)


update_clock()

time_format = Label(
    clock,
    text="WELCOME\nHow may I assist you?",
    fg="black",
    bg="#ED9121",
    font=("Helvetica", 40, "bold"),
).place(x=220, y=15)
addTime = Label(
    clock,
    text="Hour              Minutes         Seconds",
    font=("Helvetica", 25),
    bg="#212121",
    fg="#F0FFF0",
).place(
    x=120, y=210
)  # The second heading is given above the user input boxes for the labeling to be “Hour Min Sec” using addTime.
setYourAlarm = Label(
    clock,
    text="© Choekyel Nyungmartsang",
    bg="#212121",
    relief=FLAT,
    font=("Helvetica", 12),
).place(
    x=550, y=460
)  # Just to make the dialog box look funkier, adding another label as “when to wake you up” using setYourAlarm.

# The Variables we require to set the alarm(initialization):
hour = (
    StringVar()
)  # As we have already converted the current time in the string before (actual time), the variables we initialize for the user input dialog boxes are in StringVar().
min = StringVar()
sec = StringVar()

# Time required to set the alarm clock:
hourTime = Entry(
    clock,
    textvariable=hour,
    relief=RIDGE,
    font=("Helvetica", 80, "bold"),
    fg="#FFFAFA",
    bg="#555555",
    highlightcolor="#63B8FF",
    justify=CENTER,
    width=3,
)  # Finally make the input boxes such as hourTime, minTime, and secTime which takes the entry of the time the user wants to set the alarm on in 24-hour format.
hourTime.insert(END, datetime.datetime.now(IST).strftime("%H"))
hourTime.place(x=120, y=250)
minTime = Entry(
    clock,
    textvariable=min,
    relief=RIDGE,
    font=("Helvetica", 80, "bold"),
    fg="#FFFAFA",
    bg="#555555",
    highlightcolor="#63B8FF",
    justify=CENTER,
    width=3,
)
minTime.insert(END, datetime.datetime.now(IST).strftime("%M"))
minTime.place(x=270, y=250)
secTime = Entry(
    clock,
    textvariable=sec,
    relief=RIDGE,
    font=("Helvetica", 80, "bold"),
    fg="#FFFAFA",
    bg="#555555",
    highlightcolor="#63B8FF",
    justify=CENTER,
    width=3,
)
secTime.insert(END, "00")
secTime.place(x=420, y=250)
# To take the time input by user:
submit = Button(
    clock,
    text="Set Alarm",
    # relief=RAISED,
    font=("Helvetica", 40, "bold"),
    bg="#C6E2FF",
    fg="black",
    activebackground="#7CFC00",
    activeforeground="#4682B4",
    width=19,
    command=actual_time,
).place(
    x=120, y=380
)  # Submit takes the command of the defined function actual_time and executes the clock as it acts as a set button to start the program.

clock.mainloop()  # Clock.mainloop() is the basic and the last command was given to compile all the previous commands with their basic settings of color, font, width, axis, etc. and displays the window as soon as the program is run.
# Execution of the window.
