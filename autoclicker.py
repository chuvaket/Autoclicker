import os
from mouse import click
import keyboard
from keyboard import add_hotkey as ahk
from time import sleep


print("Press '*' to activate")
print("Press 'Del' to close")
print("Press 'Ctrl + Shift + e' to change time interval")

status = False
active = True


def change_interval():
    global status
    status = False
    global time_interval
    time_interval = float(input("Enter the time between clicks(sec): "))
    print(f"Interval is {time_interval}")


def activate():
    os.system("cls")
    global status
    status = not status
    if status:
        print("activated")
    else: 
        print("inactive")


def get_out():
    global active
    active = False
    print("exit with code 0!")
    sleep(1)

change_interval()

ahk("*", activate) # "*" is activate button

ahk("del", get_out)

ahk("ctrl+shift+e", change_interval)

while active:
    if status:
        click(button='left')
        sleep(time_interval)