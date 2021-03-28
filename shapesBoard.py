"""
Author: Opal Peltzman 208521385
"""
from tkinter import *
from tkinter.ttk import Combobox

"""
The App class
"""
class myWindowApp():

    def __init__(self):
        self.color = "pink"
        self.window = 0
        self.canvas = 0
        self.tollbar = 0
        self.shapeChosen = 0
        self.click_number = 0
        self.initWindow()
        # Combobox, allowing the user to chose colors
        self.cb = 0
        self.scale = 0

    """
        set_color(self, event):
        update the pixel color according to the user.
            """
    def set_color(self, event):
        self.color = self.cb.get()
        print("color", self.color)

    """
       clean_canvas(self):
       deletes all drawing from canvas.
            """
    def clean_canvas(self):
        self.canvas.delete("all")
        print("clean canvas")

    """
        putpixel(self, X1, Y1, color): 
        turn on a single pixel in the active window.
            """
    def putpixel(self, X1, Y1, color):
        pass

    """
       handle_canvas_line(self): 
       handles toolbar line button click,
       and creates a canvas mouse event listening.
       
            """
    def handle_canvas_line(self):
        print("drawing a Line")
        self.canvas.bind('<Button-1>', self.handle_line_inputs)

    """
      handle_line_inputs(self, event):
      handles the mouse inputs and send start and end's line point
      to draw_line(self, point_start, point_end) function.
           """
    def handle_line_inputs(self, event):
        global x1, y1
        if self.click_number == 0:
            x1 = event.x
            y1 = event.y
            self.click_number = 1

        else:
            x2 = event.x
            y2 = event.y

            self.draw_line((x1, y1), (x2, y2))
            self.click_number = 0

    """
        draw_line(self, point_start, point_end): create a line based on start and 
        end points the user choose.
        Based on DDA algorithm
            """
    def draw_line(self, point_start, point_end):
        self.canvas.create_line(point_start[0], point_start[1], point_end[0], point_end[1], fill=self.color, width=5)

    """
        handle_canvas_circle(self):
        handles toolbar circle button click,
        and creates a canvas mouse event listening.

            """
    def handle_canvas_circle(self):
        print("drawing a Circle")
        # self.canvas.bind('<Button-1>', self.handle_line_inputs)

    """
        handle_canvas_curve(self):
        handles toolbar curve button click,
        and creates a canvas mouse event listening.

            """
    def handle_canvas_curve(self):
        print("drawing a Curve")

        self.scale = Scale(self.tollbar, label='no. of lines', from_=10, to=50, orient=HORIZONTAL, showvalue=0, tickinterval=10)
        self.scale.pack(side=LEFT, padx=5, pady=2)
        # self.canvas.bind('<Button-1>', self.handle_line_inputs)

    """
        initWindow(): creates the application that allow user to draw 
        3 geometrics shapes.
        creating window with Python GUI Tkinter
            """
    def initWindow(self):
        self.window = Tk()
        # Title bar Title
        self.window.title('SHAPES')
        # Set fixed price to window
        self.window.geometry("800x500")
        # Create toolbar menu
        self.tollbar = Frame(self.window)
        self.tollbar.pack(side=TOP, fill=X)

        # Add shape button options
        # line button
        drawLine = Button(
            self.tollbar,
            relief=FLAT,
            compound=LEFT,
            text="Draw Line",
            activebackground='pink',
            command=self.handle_canvas_line
        )
        drawLine.pack(side=LEFT, padx=2, pady=2)

        # circle button
        drawCircle = Button(
            self.tollbar,
            relief=FLAT,
            compound=LEFT,
            text="Draw Circle",
            activebackground='pink',
            command=self.handle_canvas_circle
        )
        drawCircle.pack(side=LEFT, padx=2, pady=2)

        # curve button
        drawCurve = Button(
            self.tollbar,
            relief=FLAT,
            compound=LEFT,
            text="Draw Curve",
            activebackground='pink',
            command=self.handle_canvas_curve
        )
        drawCurve.pack(side=LEFT, padx=2, pady=2)

        # clean canvas
        cleanCanvas = Button(
            self.tollbar,
            relief=FLAT,
            compound=LEFT,
            text="Clean Canvas",
            activebackground='pink',
            command=self.clean_canvas
        )
        cleanCanvas.pack(side=LEFT, padx=2, pady=2)

        # Adding color option
        data = ("pink", "black", "orange", "blue", "yellow")
        self.cb = Combobox(self.tollbar, values=data)
        self.cb.current(0)
        self.cb.pack(side=LEFT, padx=2, pady=2)
        self.cb.bind("<<ComboboxSelected>>", self.set_color)

        # Adding canvas to the window
        self.canvas = Canvas(self.window, width=400, height=400, background='white')
        self.canvas.pack(fill=X)

        # window.mainloop(), enables Tkinter listen to events in the window
        self.window.mainloop()


"""
run app
"""
def main():
    myWindowApp()



if __name__ == '__main__':
    main()