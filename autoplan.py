import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math
import os

#list of points added by user
points = []

# autonomous pathing to compare user's path to
# can be changed by running program, inputing your path, and copying array from terminal for each side
ubett_left = [(36, 12), (13, 12), (47, 57)]
ubett_right = [(108, 12), (72, 44), (93, 44), (91, 56)]

# utility distance between points function
def distance(pt1, pt2):
    dist_x = pt1[0] - pt2[0]
    dist_y = pt1[1] - pt2[1]
    return math.sqrt(dist_x * dist_x + dist_y * dist_y)

# handle input
def onclick(event):
    if event.xdata and event.ydata:
        point = (int(event.xdata), int(event.ydata))
        # puts near points together to make path look cleaner
        for p in points:
            if(distance(point, p) < 3):
                point = p
    
        plt.plot([points[-1][0], point[0]], [points[-1][1], point[1]], color="black", linewidth=5)
        plt.scatter(point[0], point[1], color="black")
        plt.draw()

        points.append(point)

def create_field(background_img, left):
    img = mpimg.imread(background_img)
    
    # Create a figure with the game field as the background
    fig, ax = plt.subplots()
    ax.imshow(img, extent=[0, 144, 0, 144])  # Adjust based on image size and field dimensions
    # FTC field dimensions in inches
    ax.set_xlim(0, 144)  
    ax.set_ylim(0, 144)

    plt.gca().set_aspect('equal', adjustable='box')
    plt.title("Click to set waypoints on the field")
    cid = fig.canvas.mpl_connect('button_press_event', onclick)


    ubett_path = []
    if left:
        points.append((36, 12))
        ubett_path = ubett_right
    else:
        points.append((108, 12))
        ubett_path = ubett_left
    
    for p in ubett_path: plt.scatter(p[0], p[1], color="gold")
    plt.plot([pt[0] for pt in ubett_path], [pt[1] for pt in ubett_path], color="gold", linewidth=5)
    
    
    plt.scatter(points[0][0], points[0][1], color="black")
    plt.show()



if __name__ == "__main__":
    bg_img = f"{os.path.dirname(__file__)}\\field.png"

    create_field(bg_img, input("Left or right auto (type L or R): ") == "L")

    # after auto path in inputted: give total length (in.)
    total_dist = 0
    for i in range(1, len(points)):
        total_dist += distance(points[i-1], points[i])


    print(f"path distance is {int(total_dist * 10)/10} inches")

    # share points if wanted
    print(points)