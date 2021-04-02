"""
Author: Opal Peltzman 208521385
"""
from math import sqrt
from tkinter import *
from tkinter.ttk import Combobox
import numpy as np


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
        self.img = PhotoImage(width=1000, height=500)
        self.canvas.create_image((1000 // 2, 500 // 2), image=self.img, state="normal")

    """
        putpixel(self, X, Y, color): 
        turn on a single pixel in the active window.
            """
    def putpixel(self, X, Y, color):
        if X < 0 or Y < 0:
            pass
        else:
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
        based on DDA algorithm
            """
    def draw_line(self, x1, y1, x2, y2):
        start_points = [x1, y1]
        end_points = [x2, y2]

        if x1 > x2 and y1 > y2:
            start_points, end_points = end_points, start_points

        dX = self.absolute_value(end_points[0] - start_points[0])
        dY = self.absolute_value(end_points[1] - start_points[1])

        max_range = max(dX, dY)
        if max_range != 0:
            dX = dX / max_range
            dY = dY / max_range

        x = start_points[0]
        y = start_points[1]

        for i in range(max_range):
            self.putpixel(round(x), round(y), self.color)
            if x1 < x2 and y1 > y2:
                x += dX
                y -= dY
            elif x1 > x2 and y2 > y1:
                x -= dX
                y += dY
            else:
                x += dX
                y += dY

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
       to draw_circle(self, x1, y1, x2, y2) function.
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
       Based on Bresenham circle algorithm
            """
    def draw_circle(self, x1, y1, x2, y2):
        x = 0
        # find the circle radius with pythagoras
        y = int(sqrt((x2 - x1)**2 + (y2 - y1)**2))
        p = 3 - 2*y
        self.circle_pixel(x1, y1, x, y)
        while(y >= x):
            x += 1
            if(p >= 0):
                y -= 1
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
        self.destroy_curve_widget()
        self.messages.config(text="Drawing a Curve! Please choose no. of lines and click for 4 different points")

        self.scale = Scale(self.tollbar, label='no. of lines', from_=10, to=50, orient=HORIZONTAL, showvalue=0, tickinterval=10, command=self.numberOfLines)
        self.scale.pack(side=LEFT, padx=5, pady=2)

        self.lines_label = Label(self.tollbar, bg='white', width=10, text=self.number_lines_for_curve)
        self.lines_label.pack(side=LEFT, padx=5, pady=2)
        self.canvas.bind('<Button-1>', self.handle_curve_inputs)

    """
        numberOfLines(self, number):
        present to the user the number of lines he chose to draw
        a curve.
            """
    def numberOfLines(self, number):
        self.number_lines_for_curve = number
        self.lines_label.config(text='no.   ' + self.number_lines_for_curve)

    """
        handle_curve_inputs(self, event):
        handles the mouse inputs and send 4 points
        to draw_curve(self, x1, y1, x2, y2, x3, y3, x4, y4, lines) function.
            """
    def handle_curve_inputs(self, event):
        if self.click_number == 0:
            self.curve_points['p1'] = (event.x, event.y)
            self.click_number = 1

        elif self.click_number == 1:
            self.curve_points['p2'] = (event.x, event.y)
            self.click_number = 2

        elif self.click_number == 2:
            self.curve_points['p3'] = (event.x, event.y)
            self.click_number = 3

        elif self.click_number == 3:
            self.curve_points['p4'] = (event.x, event.y)
            self.draw_curve(self.curve_points['p1'][0], self.curve_points['p1'][1], self.curve_points['p2'][0],
                            self.curve_points['p2'][1], self.curve_points['p3'][0], self.curve_points['p3'][1],
                            self.curve_points['p4'][0], self.curve_points['p4'][1], self.number_lines_for_curve)
            self.click_number = 0

    """
        draw_curve(self, x1, y1, x2, y2, x3, y3, x4, y4, lines):
        create a curve based on 4 points the user choose.
        Based on Bezier curves algorithm
            """
    def draw_curve(self, x1, y1, x2, y2, x3, y3, x4, y4, lines):
        # initialize parameters
        t = accuracy = 1 / int(lines)
        mb = [[-1, 3, -3, 1],
              [3, -6, 3, 0],
              [-3, 3, 0, 0],
              [1, 0, 0, 0]]

        x_vector = [[x1, x2, x3, x4]]
        y_vector = [[y1, y2, y3, y4]]

        previous_x = x1
        previous_y = y1

        self.putpixel(x1, y1, "black")
        self.putpixel(x2, y2, "black")
        self.putpixel(x3, y3, "black")
        self.putpixel(x4, y4, "black")

        while t <= 1:
            t_vector = [(t ** 3), (t ** 2), t, 1]
            x = int(np.dot(t_vector, np.dot(mb, np.transpose(x_vector))))
            y = int(np.dot(t_vector, np.dot(mb, np.transpose(y_vector))))
            self.draw_line(previous_x, previous_y, x, y)
            previous_x = x
            previous_y = y
            t += accuracy
        self.draw_line(previous_x, previous_y, x4, y4)

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
        self.canvas = Canvas(self.window, width=1000, height=500, background='white')
        self.canvas.pack(fill=X)
        # Adding img
        self.img = PhotoImage(width=1000, height=500)
        self.canvas.create_image((1000//2, 500//2), image=self.img, state="normal")

        # window.mainloop(), enables Tkinter listen to events in the window
        self.window.mainloop()


"""
run app
"""
def main():
    myWindowApp()


if __name__ == '__main__':
    main()