"""
Author: Opal Peltzman 208521385
"""
from math import sqrt
from tkinter import *
from tkinter.ttk import Combobox


"""
The App class
"""
class myWindowApp():

    def __init__(self):
        self.window = 0
        self.canvas = 0
        self.img = 0
        self.tollbar = 0
        self.shapeChosen = 0
        self.click_number = 0
        self.messages = 0

        self.line_points = {'start': (0, 0), 'end': (0, 0)}
        self.circle_points = {'center': (0, 0), 'perimeter': (0, 0)}
        self.curve_points = {'p1': (0, 0), 'p2': (0, 0), 'p3': (0, 0), 'p4': (0, 0)}

        # parameters for curve drawing
        self.number_lines_for_curve = 10
        self.lines_label = 0
        self.scale = 0

        # colors
        # default color for pixel (pink in hex)
        self.color = "#ffa4a9"
        self.colors_dictionary = {"pink": "#ffa4a9", "black": "#041412", "orange": "#ff991a", "blue": "#1a35ff",
        "yellow": "#ffff00", "green": "#009b3b", "red": "#ff311a", "magenta": "#ff00ff", "cyan": "#00ffff", "grey": "#a6aea9"}
        # Combobox, allowing the user to chose colors
        self.cb = 0

        # start function
        self.initWindow()

    """
        set_color(self, event):
        update the pixel color according to the user.
            """
    def set_color(self, event):
        self.color = self.cb.get()
        print("color", self.color)
        self.color = self.colors_dictionary[self.color]
        print("color in hex", self.color)

    """
        destroy_curve_widget(self):
        deletes all widgets relevant to curve drawing.
            """
    def destroy_curve_widget(self):
        for widget in self.tollbar.winfo_children():
            if widget == self.lines_label or widget == self.scale:
                widget.destroy()

    """
       clean_canvas(self):
       deletes all drawing from canvas.
            """
    def clean_canvas(self):
        self.canvas.delete("all")
        print("clean canvas")
        self.messages.config(text="All clean! Let's start again")
        # Adding img
        self.img = PhotoImage(width=800, height=420)
        self.canvas.create_image((0, 0), image=self.img, anchor="nw")

    """
        putpixel(self, X, Y, color): 
        turn on a single pixel in the active window.
            """
    def putpixel(self, X, Y, color):
        self.img.put(color, (X, Y))

    """
        absolute_value(self, value):
        returns the absolute value.
            """
    def absolute_value(self, value):
        val = value
        if value < 0:
            val = value * -1
        return val

    """
       handle_canvas_line(self): 
       handles toolbar line button click,
       and creates a canvas mouse event listening.
       
            """
    def handle_canvas_line(self):
        print("drawing a Line")
        self.destroy_curve_widget()
        self.messages.config(text='Drawing a Line! Please click for a start and end point')
        self.canvas.bind('<Button-1>', self.handle_line_inputs)

    """
      handle_line_inputs(self, event):
      handles the mouse inputs and send start and end's line points
      to draw_line(self, point_start, point_end) function.
           """
    def handle_line_inputs(self, event):
        if self.click_number == 0:
            self.line_points['start'] = (event.x, event.y)
            self.click_number = 1

        else:

            self.line_points['end'] = (event.x, event.y)
            self.draw_line(self.line_points['start'][0], self.line_points['start'][1],
                           self.line_points['end'][0], self.line_points['end'][1])
            self.click_number = 0

    """
        draw_line(self, point_start, point_end): 
        create a line based on start and 
        end points the user choose.
        Based on Bresenham algorithm
            """
    def draw_line(self, x1, y1, x2, y2):
        if((self.absolute_value(x1-x2)>= self.absolute_value(y1-y2) and x2 < x1) or ((self.absolute_value(y1-y2)> self.absolute_value(x1-x2)) and y2 <y1)):
            x1,y1,x2,y2,x2,y2,x1,y1
        start_points = [x1, y1]
        end_points = [x2, y2]

        dX = end_points[0] - start_points[0]
        dY = end_points[1] - start_points[1]

        step = self.absolute_value(dY) > self.absolute_value(dX)

        if step:
            start_points[0], start_points[1] = start_points[1], start_points[0]
            end_points[0], end_points[1] = end_points[1], end_points[0]

        if start_points[0] > end_points[0]:
            start_points[0], end_points[0] = end_points[0], start_points[0]
            start_points[1], end_points[1] = end_points[1], start_points[1]

        dX = end_points[0] - start_points[0]
        dY = end_points[1] - start_points[1]

        error = (2 * dY) - dX
        ystep = -1
        y = start_points[1]
        if start_points[1] < end_points[1]:
            ystep = 1

        for x in range(start_points[0], end_points[0] + 1):
            if step:
                self.putpixel(y, x, self.color)
            else:
                self.putpixel(x, y, self.color)
            error += 2 * dY
            if error >= 0:
                y += ystep
                error -= 2 * dX

    """
        handle_canvas_circle(self):
        handles toolbar circle button click,
        and creates a canvas mouse event listening.

            """
    def handle_canvas_circle(self):
        print("drawing a Circle")
        self.destroy_curve_widget()
        self.messages.config(text="Drawing a Circle! Please click for a center point and then perimeter point")
        self.canvas.bind('<Button-1>', self.handle_circle_inputs)

    """
       handle_circle_inputs(self, event):
       handles the mouse inputs and send center and perimeter's circle points
       to draw_circle(self, center_point, perimeter_point) function.
            """
    def handle_circle_inputs(self, event):
        if self.click_number == 0:
            self.circle_points['center'] = (event.x, event.y)
            self.click_number = 1

        else:

            self.circle_points['perimeter'] = (event.x, event.y)
            self.draw_circle(self.circle_points['center'][0], self.circle_points['center'][1],
                           self.circle_points['perimeter'][0], self.circle_points['perimeter'][1])
            self.click_number = 0

    """
       circle_pixel(self, x_center, y_center, x_r, y_r):
       draw all 8 pixels.
            """
    def circle_pixel(self, x_center, y_center, x_r, y_r):
        self.putpixel(x_center + x_r, y_center + y_r, self.color)
        self.putpixel(x_center - x_r, y_center + y_r, self.color)
        self.putpixel(x_center + x_r, y_center - y_r, self.color)
        self.putpixel(x_center - x_r, y_center - y_r, self.color)
        self.putpixel(x_center + y_r, y_center + x_r, self.color)
        self.putpixel(x_center - y_r, y_center + x_r, self.color)
        self.putpixel(x_center + y_r, y_center - x_r, self.color)
        self.putpixel(x_center - y_r, y_center - x_r, self.color)

    """
       draw_circle(self, x1, y1, x2, y2): 
       create a circle based on center and 
       perimeter points the user choose.
       Based on Closed Corners Bresenham circle algorithm
            """
    def draw_circle(self, x1, y1, x2, y2):
        x = 0
        # find the circle radius with pythagoras
        y = int(sqrt((x2 - x1)**2 + (y2 - y1)**2))
        p = 3 - 2*y
        self.circle_pixel(x1, y1, x, y)
        while(y >= x):
            x+= 1
            if(p >= 0):
                y-= 1
                p = p + 4 * (x - y) + 10
            else:
                p = p + 4*x + 6
            self.circle_pixel(x1, y1, x, y)
    """
        handle_canvas_curve(self):
        handles toolbar curve button click,
        and creates a canvas mouse event listening.

            """
    def handle_canvas_curve(self):
        print("drawing a Curve")
        self.destroy_curve_widget()
        self.messages.config(text="Drawing a Curve! Please choose no. of lines and click for 4 different points")

        self.scale = Scale(self.tollbar, label='no. of lines', from_=10, to=50, orient=HORIZONTAL, showvalue=0, tickinterval=10, command=self.numberOfLines)
        self.scale.pack(side=LEFT, padx=5, pady=2)

        self.lines_label = Label(self.tollbar, bg='white', width=10, text=self.number_lines_for_curve)
        self.lines_label.pack(side=LEFT, padx=5, pady=2)
        # self.canvas.bind('<Button-1>', self.handle_line_inputs)

    def numberOfLines(self, number):
        self.number_lines_for_curve = number
        self.lines_label.config(text='no.   ' + self.number_lines_for_curve)

    """
        initWindow(): creates the application that allow user to draw 
        3 geometrics shapes.
        creating window with Python GUI Tkinter
            """
    def initWindow(self):
        self.window = Tk()
        # Set bar Title
        self.window.title('SHAPES')
        # Set fixed dimensions to window
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

        # clean canvas button
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
        data = ("pink", "black", "orange", "blue", "yellow", "green", "red", "magenta", "cyan", "grey")
        self.cb = Combobox(self.tollbar, values=data)
        self.cb.current(0)
        self.cb.pack(side=LEFT, padx=2, pady=2)
        self.cb.bind("<<ComboboxSelected>>", self.set_color)

        self.messages = Label(self.window, bg='pink', text=" Enjoy your drawing! Please choose you're shape ", anchor='w')
        self.messages.pack(fill=X, padx=2, pady=2)

        # Adding canvas to the window
        self.canvas = Canvas(self.window, width=400, height=420, background='white')
        self.canvas.pack(fill=X)
        # Adding img
        self.img = PhotoImage(width=800, height=420)
        self.canvas.create_image((0, 0), image=self.img, anchor="nw")

        # window.mainloop(), enables Tkinter listen to events in the window
        self.window.mainloop()


"""
run app
"""
def main():
    myWindowApp()


if __name__ == '__main__':
    main()