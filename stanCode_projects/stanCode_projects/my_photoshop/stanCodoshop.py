"""
File: stanCodoshop.py
Name: Ruby
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage



def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """

    color_distance = ((red - pixel.red)**2 + (green - pixel.green)**2 + (blue - pixel.blue)**2)
    # color_distance = math.sqrt((red - pixel.red)**2 + (green - pixel.green)**2 + (blue - pixel.blue)**2)
    return color_distance**0.5


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    sum_pixel_red = 0
    sum_pixel_blue = 0
    sum_pixel_green = 0
    for i in range(len(pixels)):
        pixel = pixels[i]
        sum_pixel_red += pixel.red
        sum_pixel_green += pixel.green
        sum_pixel_blue += pixel.blue
    red = sum_pixel_red//len(pixels)
    blue = sum_pixel_blue//len(pixels)
    green = sum_pixel_green//len(pixels)
    new_list = [red, green, blue]
    return new_list


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    compared_pixel = get_average(pixels)
    red = compared_pixel[0]
    green = compared_pixel[1]
    blue = compared_pixel[2]
    new_pixel_dic = []
    # best_pixel = pixels[0]
    for i in range(len(pixels)):
        pixel_dic = (get_pixel_dist(pixels[i], red, green, blue), pixels[i])
        new_pixel_dic.append(pixel_dic)
    sort_dis = min(new_pixel_dic, key=lambda e: e[0])
    # sort_dis = min(new_pixel_dic)
    # best_pix = sort_dis[1]
    return sort_dis[1]


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)

    for x in range(result.width):
        for y in range(result.height):
            pixels = []
            result_pix = result.get_pixel(x, y)
            for i in range(len(images)):
                pixel = images[i].get_pixel(x, y)
                pixels.append(pixel)
            best_pix = get_best_pixel(pixels)
            result_pix.red = best_pix.red
            result_pix.green = best_pix.green
            result_pix.blue = best_pix.blue




    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect
    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
