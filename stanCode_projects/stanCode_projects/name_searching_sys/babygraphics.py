"""
File: babygraphics.py
Name: Ruby
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    x_dx = (width - GRAPH_MARGIN_SIZE)/(len(YEARS))
    x_c = x_dx * year_index
    return x_c


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    canvas.create_line(GRAPH_MARGIN_SIZE, 0, GRAPH_MARGIN_SIZE, CANVAS_HEIGHT, width=2, fill='black')
    canvas.create_line(0, GRAPH_MARGIN_SIZE, CANVAS_WIDTH, GRAPH_MARGIN_SIZE, width=2, fill='black')
    canvas.create_line(0, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                       width=2, fill='black')
    for i in range(len(YEARS)):
        x_index = YEARS[i]
        x_c = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(GRAPH_MARGIN_SIZE+x_c, 0, GRAPH_MARGIN_SIZE+x_c, CANVAS_HEIGHT, width=2, fill='black')
        canvas.create_text(GRAPH_MARGIN_SIZE+x_c+2, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE+2, text=x_index, anchor=tkinter.NW,
                           fill='black', font='10')


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #

    last_x_c = 0
    last_y_c_p = 0
    percent = CANVAS_HEIGHT/MAX_RANK
    no_rank = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
    color_index = 0
    for i in range(len(lookup_names)):
        name = lookup_names[i]  # divided name
        year_rank = name_data[name]
        for k in range(len(YEARS)):
            year = str(YEARS[k])
            x_c = get_x_coordinate(CANVAS_WIDTH, k)  # x coordinate
            if year in year_rank:
                y_c = year_rank[year]
                y_c_p = (int(y_c)*percent)+GRAPH_MARGIN_SIZE  # 符合比例y_c
                if year == '1900':
                    canvas.create_text(GRAPH_MARGIN_SIZE + x_c, y_c_p, text=name + year_rank[year],
                                       anchor=tkinter.SW, fill=COLORS[color_index])
                else:
                    canvas.create_text(GRAPH_MARGIN_SIZE + x_c, y_c_p, text=name + year_rank[year],
                                       anchor=tkinter.SW, fill=COLORS[color_index])
                    canvas.create_line(GRAPH_MARGIN_SIZE + last_x_c, last_y_c_p, GRAPH_MARGIN_SIZE+x_c, y_c_p,
                                       width=LINE_WIDTH, fill=COLORS[color_index])
                last_x_c = x_c
                last_y_c_p = y_c_p
            else:
                if year == '1900':
                    canvas.create_text(GRAPH_MARGIN_SIZE + x_c, no_rank,
                                       text=name + '*', anchor=tkinter.SW, fill=COLORS[color_index])
                else:
                    canvas.create_text(GRAPH_MARGIN_SIZE + x_c, no_rank,
                                       text=name+'*', anchor=tkinter.SW, fill=COLORS[color_index])
                    canvas.create_line(GRAPH_MARGIN_SIZE + last_x_c, last_y_c_p,
                                       GRAPH_MARGIN_SIZE + x_c, no_rank,
                                       width=LINE_WIDTH, fill=COLORS[color_index])
                last_x_c = x_c
                last_y_c_p = no_rank
        if color_index == len(COLORS):
            color_index = 0
        else:
            color_index += 1














# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
