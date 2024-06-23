# coding=windows-1252
import os
import random
import sys
from PIL import Image
import PIL.Image
import subprocess
from os.path import exists as file_exists
from NzlContourPlotGenerator import plot
from PREG_Logic import main_code, findexB, findexA, findexC
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

# Variable Declaration Section
count = 2
filelogging = True
blue = "#0000FF"
gray = "#C8C8C8"
black = "#000000"
white = "#FFFFFF"
dark_gray = "#141414"
light_blue = "#B4DDFF"
darker_gray = "#A5A4A5"
button_font = ("Helvetica", 16)
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")
customtkinter.set_widget_scaling(0.8)

class Proced_REG(customtkinter.CTk):
    def __init__(self, **kwargs):
        # Initial Variable Declartion
        super().__init__(**kwargs)
        self.imgge = None
        self.graph_img = None
        self.graphical_rep = None
        self.genlistA = None
        self.output = None
        self.t_output = None
        self.dev_explorer = None
        self.interiorTitle = None
        self.interiorText = None
        self.open_explorer = None
        self.filelog = None
        self.reload = None
        self.label = None
        self.labelTitle = None
        self.labelText = None
        self.st = 0
        self.state("zoomed")
        self.title("Procedural Rocket Engine Generator")
        self.iconbitmap("Assets/icon.ico")

        # Generates the cosmetics for the main framework
        self.sidebar = customtkinter.CTkFrame(self, width=305, height=1200, corner_radius=5)
        self.random = customtkinter.CTkButton(self.sidebar, corner_radius=6, height=50, width=200, border_spacing=10, text="Automated Generation", font=button_font, command=self.auto)
        self.basic = customtkinter.CTkButton(self.sidebar, corner_radius=6, height=50, width=200, border_spacing=10, text="Basic Generation", font=button_font, command=self.basic)
        self.extended = customtkinter.CTkButton(self.sidebar, corner_radius=6, height=50, width=200, border_spacing=10, text="Extended Generation", font=button_font, command=self.adv)
        self.about = customtkinter.CTkButton(self.sidebar, corner_radius=6, height=50, width=160, border_spacing=10, text="About Us", font=button_font, command=self.about)

        # Reference for the variables for placement of cosmetic items
        self.sidebar.place(x=0, y=120)
        self.random.place(x=53, y=35)
        self.basic.place(x=53, y=110)
        self.extended.place(x=53, y=185)
        self.about.place(x=73, y=260)

        # Main Frame / Title Creation
        self.mainFrame = customtkinter.CTkFrame(self, width=2075, height=1200, corner_radius=5, fg_color="#242424")
        self.mainTitle = customtkinter.CTkFrame(self, width=2075, height=120, corner_radius=5, fg_color="#242424")
        self.line = customtkinter.CTkFrame(self, width=2500, height=3, fg_color="#404040")

        # Main Frame / Title Placement
        self.mainFrame.place(x=305, y=120)
        self.mainTitle.place(x=0, y=0)
        self.line.place(x=0, y=120)

        # Adds the different buttons and itonc (mostly the home button)
        self.home_image = customtkinter.CTkImage(PIL.Image.open(open("./Assets/reload.png", "rb")))
        self.home_button = customtkinter.CTkButton(self, corner_radius=2, height=20, border_spacing=0, text="", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), image=self.home_image)

        # Makes sure the app closes like it is supposed to
        self.make_topmost()
        self.protocol("WM_DELETE_WINDOW", self.on_exit)
        self.auto()
        self.update()
    def on_exit(self):
        # Exit protocol for app
        self.destroy()
        sys.exit(1)
    def center(self):
        # Centering the tkinter window
        self.eval('tk::PlaceWindow %s center' % app.winfo_pathname(app.winfo_id()))
    def txt_gen(self, array):
        y_coor = 0
        self.labelTitle = customtkinter.CTkLabel(self.interiorTitle, text=str(f"""  {array[0]}"""), font=("Segoe UI", 32))
        self.labelTitle.place(x=14, y=10)
        for i in range(1, len(self.output)):
            self.labelText = customtkinter.CTkLabel(self.interiorText, text=str(f"   {array[i]}\n"), font=("Segoe UI", 20))
            self.labelText.place(x=15, y=y_coor + 30)
            y_coor = y_coor + 30
    def make_topmost(self):
        # No idea anymore lol
        self.lift()
        self.attributes("-topmost", 1)
        self.attributes("-topmost", 0)

    def reload_button(self):
        self.st = random.randint(5, 500)

        # Destroying any widgets already displayed
        for widgets in self.interiorTitle.winfo_children(): widgets.destroy()
        for widgets in self.interiorText.winfo_children(): widgets.destroy()
        for widgets in self.imgge.winfo_children(): widgets.destroy()

        # Gets the output from the main code
        self.output = main_code(filelogging)
        self.genlistA = self.output

        # Deletes and re-creates the graph for the nozzle
        if file_exists("graph_plot.png"):
            os.remove("graph_plot.png")

        # Generates the graphical plot for the Rocket Engine Nozzle
        try:
            findexA(self.output, "None (Nozzle doesnt have a throat)")
        except:
            l_p = 80
            try:
                Ar = int((findexB(self.output, "Exhaust Expansion Ratio")[0]).split(":")[1])
                if findexC(self.output, "Conical Nozzle") > 0:
                    l_p = 100
                elif findexC(self.output, "Contour Bell Nozzle") > 0:
                    l_p = 90
                plot(self.st, int(Ar), l_p, 1.2, "graph_plot.png")

                # Displays the graphical plot for the Rocket Engine Nozzle
                self.graphical_rep = customtkinter.CTkImage(PIL.Image.open("graph_plot.png"), size=(835, 625))
                self.graph_img = customtkinter.CTkLabel(self.imgge, text="", font=("Arial", 18), text_color="White",
                                                        image=self.graphical_rep)
                self.graph_img.place(x=0, y=0)
            except:
                # Displays the graphical plot for the Rocket Engine Nozzle
                self.graphical_rep = customtkinter.CTkImage(PIL.Image.open("None.png"), size=(835, 625))
                self.graph_img = customtkinter.CTkLabel(self.imgge, text="", font=("Arial", 18), text_color="White",
                                                        image=self.graphical_rep)
                self.graph_img.place(x=0, y=0)

        # Places the output from the main code (Title and Label)
        self.txt_gen(self.output)

        # Saves the output from the main logic in memory (stops it from changing / reloading)
        self.t_output = self.output

        # Creates the graphical plot for the Rocket Engine Nozzle
        try:
            self.graphical_rep = customtkinter.CTkImage(PIL.Image.open("graph_plot.png"), size=(835, 625))
            self.graph_img = customtkinter.CTkLabel(self.imgge, text="", font=("Arial", 18), text_color="White", image=self.graphical_rep)
            self.graph_img.place(x=0, y=0)
        except:
             pass

    def auto(self):
        # Destroying any widgets already displayed
        for widgets in self.mainFrame.winfo_children(): widgets.destroy()
        for widgets in self.mainTitle.winfo_children(): widgets.destroy()

        # Display main window title
        self.label = customtkinter.CTkLabel(self.mainTitle, text="Automated Generation", font=("Sans-Serif", 65, "bold"))
        self.label.grid(padx=20, pady=(20, 100))
        self.label.place(x=405, y=98, anchor="s")

        # Creates and places the "Generate" button
        self.reload = customtkinter.CTkButton(self.mainFrame, command=self.reload_button, text="Generate")
        self.reload.grid(padx=20, pady=10)
        self.reload.place(x=70, y=760)

        # Creates the tooltip on button hover (for the "Generate" button)
        CreateToolTip(self.reload, text='Generates a new engine', font=("Arial", 13), fg="white", padx=8, pady=2, bg="#444444", bw=0, delay=150)

        # Creates and places the "Open Files" button
        self.open_explorer = customtkinter.CTkButton(self.mainFrame, text="Open Files", command=lambda: subprocess.run(["C:/Windows/explorer.exe", 'GenFiles']))
        self.open_explorer.grid(padx=20, pady=10); self.open_explorer.place(x=230, y=760)

        # Creates and places the "Dev Data" button
        self.dev_explorer = customtkinter.CTkButton(self.mainFrame, text="Open Dev Data", command=lambda: subprocess.run(["C:/Windows/explorer.exe", 'GenFiles/GenData']))
        self.dev_explorer.grid(padx=20, pady=10); self.dev_explorer.place(x=390, y=760)

        # Creates and places the "File Logging" button
        self.filelog = customtkinter.CTkSwitch(master=self.mainFrame, text="File Logging", command=file_log)
        self.filelog.select(); self.filelog.grid(pady=10, padx=20, sticky="n")
        self.filelog.place(x=605, y=785, anchor="s")

        # Creates and places the interior title of the window
        self.interiorTitle = customtkinter.CTkFrame(self.mainFrame, width=3000, height=65, corner_radius=5)
        self.interiorTitle.grid(padx=(20, 20), pady=(0, 0), sticky="nsew")
        self.interiorTitle.place(x=45, y=25)

        # Creates and places the interior text of the window
        self.interiorText = customtkinter.CTkFrame(self.mainFrame, width=3000, height=650, corner_radius=5)
        self.interiorText.place(x=45, y=95)

        # Creates and sets the graph image on the main frame
        self.imgge = customtkinter.CTkFrame(self.mainFrame, width=835, height=625, corner_radius=5)
        self.imgge.place(x=1225, y=107)

        # Enacts on the reload if nothing is saved in memory, keeps it if something is in memory (Title and Label)
        if self.t_output is None:
            self.reload_button()
        else:
            self.txt_gen(self.t_output)

        # Generates the graphical plot for the Rocket Engine Nozzle
        try:
            findexA(self.output, "None (Nozzle doesnt have a throat)")
        except:
            l_p = 80
            try:
                Ar = int((findexB(self.output, "Exhaust Expansion Ratio")[0]).split(":")[1])
                if findexC(self.output, "Conical Nozzle") > 0:
                    l_p = 100
                elif findexC(self.output, "Contour Bell Nozzle") > 0:
                    l_p = 90
                plot(self.st, int(Ar), l_p, 1.2, "graph_plot.png")

                # Displays the graphical plot for the Rocket Engine Nozzle
                self.graphical_rep = customtkinter.CTkImage(PIL.Image.open("graph_plot.png"), size=(835, 625))
                self.graph_img = customtkinter.CTkLabel(self.imgge, text="", font=("Arial", 18), text_color="White",
                                                        image=self.graphical_rep)
                self.graph_img.place(x=0, y=0)
            except:
                # Displays the graphical plot for the Rocket Engine Nozzle
                self.graphical_rep = customtkinter.CTkImage(PIL.Image.open("None.png"), size=(835, 625))
                self.graph_img = customtkinter.CTkLabel(self.imgge, text="", font=("Arial", 18), text_color="White",
                                                        image=self.graphical_rep)
                self.graph_img.place(x=0, y=0)

    def basic(self):
        # Destroying any widgets already displayed
        for widgets in self.mainFrame.winfo_children(): widgets.destroy()
        for widgets in self.mainTitle.winfo_children(): widgets.destroy()

        # Display main window title
        self.label = customtkinter.CTkLabel(self.mainTitle, text="Basic Generation", font=("Sans-Serif", 65, "bold"))
        self.label.grid(padx=20, pady=(20, 100)); self.label.place(x=325, y=98, anchor="s")

    def adv(self):
        # Destroying any widgets already displayed
        for widgets in self.mainFrame.winfo_children(): widgets.destroy()
        for widgets in self.mainTitle.winfo_children(): widgets.destroy()

        # Display main window title
        self.label = customtkinter.CTkLabel(self.mainTitle, text="Extended Generation", font=("Sans-Serif", 65, "bold"))
        self.label.grid(padx=20, pady=(20, 100)); self.label.place(x=385, y=98, anchor="s")

    def about(self):
        # Destroying any widgets already displayed
        for widgets in self.mainFrame.winfo_children(): widgets.destroy()
        for widgets in self.mainTitle.winfo_children(): widgets.destroy()

        # Display main window title
        self.label = customtkinter.CTkLabel(self.mainTitle, text="About Us", font=("Sans-Serif", 65, "bold"))
        self.label.grid(padx=20, pady=(20, 100)); self.label.place(x=205, y=98, anchor="s")

if __name__ == "__main__":
    # Ensures that the superclass "Proced_REG" is only executed when the script is run directly
    app = Proced_REG()
    app.mainloop()
