import sys
from time import sleep

curr = 0
def progress_bar(total, bar_length, current):
    fraction = curr / total
    arrow = int(fraction * bar_length+1) * '░'
    padding = int(bar_length - len(arrow)) * '█'
    sys.stdout.write(f"\rProgress: {arrow}{padding} {int(fraction*101)}" + "%")
    sys.stdout.flush()
    sleep(0.25)

progress_bar(101, 25, curr)