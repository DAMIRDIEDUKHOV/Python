import numpy as np
import matplotlib.pyplot as plt

def create_sick_night_background(width, height):
    x = np.linspace(0, 1, width)
    y = np.linspace(0, 1, height)
    X, Y = np.meshgrid(x, y)

    # Define colors for the gradient
    color1 = [0, 0, 20]    # Dark blue
    color2 = [0, 0, 0]     # Black

    # Create the gradient using the linear interpolation
    R = np.interp(Y, [0, 1], [color1[0], color2[0]])
    G = np.interp(Y, [0, 1], [color1[1], color2[1]])
    B = np.interp(Y, [0, 1], [color1[2], color2[2]])

    # Combine the colors to form the background
    background = np.stack([R, G, B], axis=-1)

    return background

if __name__ == "__main__":
    # Set the width and height of the background
    width = 800
    height = 600

    # Create the background
    background = create_sick_night_background(width, height)

    # Display the background using matplotlib
    plt.imshow(background)
    plt.axis('off')
    plt.show()