# author: Cheng-Chia (Karie) Huang

from libs.MyKmean import *


def main():
    mk = MyKmeans(3,50,2,0,5)

    mk.generate_points()     # create a list of random points
    mk.initialize_centroids()  # create a dictionary with centroids
    mk.assign_random_clust_number()   # assign random cluster numbers for crated list of points


    flag_terminate = False   # create a flag for checking if the loop should keep running

    while flag_terminate == False:   # when the flag is False, this loop will keep running
        mk.assign_clust_number()  # update cluster number of the point, if the point is closer to other centroid
        flag_terminate = mk.update_centroid()
        # print mk.centroids
        # print flag_terminate

    plot_clust_points(mk)
    # if pt_dimension == 2:
    #     plot_clust_points(mk)
    # if pt_dimension == 3:
    #     plot_clust_points_3d(mk)


if __name__ == "__main__":
    main()