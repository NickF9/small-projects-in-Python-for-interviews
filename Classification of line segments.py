"""
the code classifies line segments into vertical, horizontal, degenerated and inclined
    for example: a line with coordinates (42, 1), (42, 2) will be vertical
"""

def classification_of_line_segments(tuple_0, tuple_1):
    if tuple_0[0] == tuple_1[0] and tuple_0[1] == tuple_1[1]:
        print('Class of line segments is degenerated')
    elif tuple_0[0] == tuple_1[0] and tuple_0[1] != tuple_1[1]:
        print('Class of line segments is vertical')
    elif tuple_0[0] != tuple_1[0] and tuple_0[1] == tuple_1[1]:
        print('Class of line segments is horizontal')
    else:
        print('Class of line segments is inclined')

tuple_0X = int(input('Input the coordinate of the first point on the X axis: '))
tuple_0Y = int(input('Input the coordinate of the first point on the Y axis: '))
tuple_1X = int(input('Input the coordinate of the second point on the X axis: '))
tuple_1Y = int(input('Input the coordinate of the second point on the Y axis: '))
tuple_0 = (tuple_0X, tuple_0Y)
tuple_1 = (tuple_1X,  tuple_1Y)
classification_of_line_segments(tuple_0, tuple_1)