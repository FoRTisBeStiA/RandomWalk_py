import matplotlib.pyplot as plt

from Random_walk import Randomwalk

while True:
    # Make a random walk, and plot the points.
    rw = Randomwalk(50000)
    rw.fill_walk()    

    point_numbers = list(range(rw.num_points))

    # Line graph option
    #plt.plot(rw.x_vals, rw.y_vals, linewidth=5)
    #
    # Scatter plot option w/colormap & B/E points
    plt.scatter(rw.x_vals, rw.y_vals, c=point_numbers,
                cmap=plt.cm.Blues, edgecolor='none', s=10)

    plt.scatter(0,0, c='green', edgecolor='none', s=100)
    plt.scatter(rw.x_vals[-1], rw.y_vals[-1], c='red',edgecolor='none', s=100)

    # Remove axes.
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    
    plt.show()

    # Set a shutdown flag, default: off
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
