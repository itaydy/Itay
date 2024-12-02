__author__: "Itay Dykman"

import csv
import matplotlib.pyplot as plt

#  The code shows the cones as points on the XY graph
#  and draw the path where the car supposed to drive through


def main():
    xy_list_left = []
    xy_list_right = []
    flag = False
    first = False
    # Read the CSV file
    with open('BrandsHatchLayout1.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            x, y = (row[0]), (row[1])  # Convert strings to floats
            if (x == '' or y == '') and first:
                flag = True
            if x == '' or y == '':
                first = True
            if not flag:
                xy_list_left.append([x, y])  # Append as a list
            else:
                xy_list_right.append([x, y])
    x_list_left = [item[0] for item in xy_list_left]
    x_list_left = [item for item in x_list_left if item != '']
    x_list_right = [item[0] for item in xy_list_right]
    x_list_right = [item for item in x_list_right if item != '']
    y_list_left = [item[1] for item in xy_list_left]
    y_list_left = [item for item in y_list_left if item != '']
    y_list_right = [item[1] for item in xy_list_right]
    y_list_right = [item for item in y_list_right if item != '']

    # לא עבד לי עם הCSV משום מה אז בניתי רשימות משלי לפי הנתונים שהיו בCSV
    x_list_left = [15.3785935, 38.5635375, 61.49431152, 84.16821156, 109.0912319,
                   134.8184519, 161.9838103, 187.8783283, 215.2712872, 242.8464722,
                   268.3631856, 288.0300621, 298.3925275, 305.8803183, 307.3890353,
                   307.9819112, 308.5647815, 307.7340162, 305.2911052, 302.494827]
    x_list_right = [27.90547925, 51.05122081, 74.40031754, 97.42212528, 119.309689,
                    141.9096745, 164.3279753, 188.6212375, 211.3231202, 231.2841168,
                    246.878733, 260.5165478, 266.8394448, 272.4338095, 274.1141685,
                    275.1573581, 276.7155272, 278.1017045, 276.2191474, 273.9059954]
    y_list_left = [25.16055073, 34.85236226, 44.53852231, 56.11236114, 63.94094084,
                   69.99707596, 74.57541112, 74.83520285, 73.88935827, 63.58309158,
                   48.85743341, 26.29290405, -1.414580998, -27.47983133, -54.41939171,
                   -79.72229599, -104.9058962, -131.0699591, -156.6185963, -181.4887076]
    y_list_right = [-4.280189042, 4.923067824, 14.31364459, 23.18365349, 33.08704096,
                    40.5910126, 43.76746572, 42.39570855, 43.784147, 36.7513002,
                    24.03879977, 8.799266761, -10.83032081, -33.11558977, -56.22831751,
                    -80.93643066, -105.7332995, -129.6357374, -154.0297285, -178.9199875]

    min_length = min(len(x_list_left), len(x_list_right), len(y_list_left), len(y_list_right))
    midpoints_x = [(x_list_left[i] + x_list_right[i]) / 2 for i in range(len(x_list_left))]
    midpoints_y = [(y_list_left[i] + y_list_right[i]) / 2 for i in range(len(y_list_left))]

    for i in range(min_length):
        plt.scatter(x_list_left[i], y_list_left[i], color='blue', s=2, label='Point from (x1, y1)' if i == 0 else "")
        plt.scatter(x_list_right[i], y_list_right[i], color='red', s=2, label='Point from (x2, y2)' if i == 0 else "")

    ax = plt.gca()
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    plt.title('XY Graph')
    plt.xlabel('X')
    plt.ylabel('Y')

    plt.plot(midpoints_x, midpoints_y, color='orange', linestyle='-', linewidth=2, label='car path')

    plt.legend()
    plt.show()
    plt.show()


if __name__ == '__main__':
    main()
