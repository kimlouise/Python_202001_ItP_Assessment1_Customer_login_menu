import time
from os import name, system


def slow_print(text, speed=0.05):
    """
    Purpose:    Print text in the console character by character.
    Usage:      slow_print(['Kimberly', 'Randall'], 0.09)
    Args:   text:   List of strings (must be a list - even if one line) to be processed.  Each element of the list will
                    be on a separate line.
            speed:  interval in seconds (default of 0.05 seconds).  Each new line will be delayed longer.
    """
    for slow in text:  # process each element of the text
        broken_string = list(slow)  # split the element into single chars
        for char in broken_string:  # process each char
            print(char, end='', flush=True)  # print each new char without a new line - flush to print at this point
            time.sleep(speed)  # pause
        time.sleep(speed * 6)  # pause for a new line
    print('\n')


def clear():  # func to clear the console window
    if name == 'nt':  # if windows
        _ = system('cls')
    else:  # mac / linux
        _ = system('clear')
