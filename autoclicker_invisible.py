from mouse import click
from keyboard import add_hotkey as ahk
from time import sleep

status = False
active = True


def activate():
    global status
    status = not status


def get_out():
    global active
    active = False


ahk("*", activate) # "*" is activate button

ahk("del", get_out)

while active:
    if status:
        click(button='left')
        sleep(0.1)