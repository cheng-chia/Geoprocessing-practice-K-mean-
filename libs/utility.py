import random
from MyPoint import Point


# Q 1.5
def point_lst(num_point,dimension,lower_bound, upper_bound):  # Create a function that takes 4 parameters
    newlst = []    # crate an empty list

    for p in range(num_point):
        if dimension == 2:   # if dimension ia two, create 2-D points, and append the point into newlst
            newPoint = Point(2,(random.uniform(lower_bound,upper_bound),random.uniform(lower_bound,upper_bound)))
            newlst.append(newPoint)

        if dimension == 3:  # if dimension is tree, create 3-D points, and append the point into newlst
            newPoint = Point(3,(random.uniform(lower_bound,upper_bound),random.uniform(lower_bound,upper_bound),random.uniform(lower_bound,upper_bound)))
            newlst.append(newPoint)


    return newlst   # Return a list of point objects



# Q 1.7
def min_distance(pointList):
    thePoint = Point(2,(50,50,0))
    thelst = []

    for p in pointList:
        distance = thePoint.calc_distance(p)
        thelst.append(distance)

    minDistance = min(thelst)
    pos = thelst.index(minDistance)
    print "Closest Point is :", pointList[pos]
    print "Closest Point's coordinates :", pointList[pos].print_coordinate()

    return pointList[pos]