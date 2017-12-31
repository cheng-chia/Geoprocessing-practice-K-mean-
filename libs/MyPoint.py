# Name: Cheng-Chia (Karie) Huang

import math

class Point:    # Create a point class
    # Q1.2
    def __init__(self,dimension,tuple1,clust_id=-1):   # the point class takes two parameter: dimension and a tuple

        self.x = tuple1[0]
        self.y = tuple1[1]
        self.dimension = dimension    # Store the dimension
        if dimension == 3:            # If dimension is 3, z coordinate is the third item in the tuple
            self.z = tuple1[2]
        if dimension == 2:            # If dimension is 2, z coordinate is zero
            self.z = 0

        self.coordinate = (self.x, self.y, self.z)  # Store the coordinate
        self.clust_id =clust_id



    # Q1.3
    def print_coordinate(self):
        return self.coordinate, self.clust_id

    # Q1.4
    def calc_distance(self,otherPoint):
        try:
            if isinstance(otherPoint, Point) == True: # Check the the type of the input
                x1 = otherPoint.x
                y1 = otherPoint.y
                z1 = otherPoint.z

                distance = math.sqrt(pow((self.x-x1),2) + pow((self.y-y1),2) + pow((self.z-z1),2)) # calculate the distance between point and input point
                return distance
                #print self.clust_id

            else:
                print "The input is not a instance of Point class."

        except Exception as e:    # Handle any kind of exceptions
            print  e              # Print error message
            print "The type of the error is:", type(e)  # Print the type of error
