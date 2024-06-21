
import time
import customtkinter
from tkinter import *

def file_log():
    global count
    global filelogging
    # dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
    # print("CTkInputDialog:", dialog.get_input())
    if type(count % 2) != 0:   filelogging = False
    else:                      filelogging = True
    count = count + 1
    # return dialog.get_input()

class ToolTip(object):
    def __init__(self, widget):
        self.bw = None
        self.bg = None
        self.pady = None
        self.padx = None
        self.fg = None
        self.ft = None
        self.text = None
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0
    def showtip(self, text, font, textcolor, padx, pady, background_color, borderline_width):
        self.text = text
        self.ft = font
        self.fg = textcolor
        self.padx = padx
        self.pady = pady
        self.bg = background_color
        self.bw = borderline_width
        if self.tipwindow or not self.text: return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 60
        y = y + cy + self.widget.winfo_rooty() + 7
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = customtkinter.CTkLabel(tw, text=self.text, fg_color=self.bg, padx=self.padx, pady=self.pady, font=self.ft,
                                       text_color=self.fg, corner_radius=4, bg_color="#222222")
        label.pack(ipadx=1)
    def hidetip(self, delay):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            time.sleep((delay / 1000))
            tw.destroy()

def CreateToolTip(widget, text, font, fg, padx, pady, bg, bw, delay):
    toolTip = ToolTip(widget)
    def enter(event): toolTip.showtip(text, font, fg, padx, pady, bg, bw)
    def leave(event): toolTip.hidetip(delay)
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)