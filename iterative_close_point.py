import math
import numpy as np
import matplotlib.pyplot as plt

"""
Fill in all the code lines which have been left blank with place holder   ' ... '
"""


class ICP:
    def __init__(self, epsilon=0.0001, max_iter=100, show_animation=True):
        # ICP parameters
        self.EPS = epsilon
        self.MAX_ITER = max_iter
        self.show_animation = show_animation

    def icp_matching(self, source_points: np.ndarray, target_points: np.ndarray) -> tuple:
        """
        Iterative Closest Point matching
        - input
        source_points: 2D points in the previous frame
        target_points: 2D points in the current frame
        - output
        R: Rotation matrix
        T: Translation vector
        """

        

        H = None  # homogeneous transformation matrix
        leftover_error = np.inf
        preError = np.inf
        count = 0

        if self.show_animation:
            fig = plt.figure()
            if source_points.shape[0] == 3:
                fig.add_subplot(111, projection='3d')

        while leftover_error >= self.EPS:
            count += 1

            if self.show_animation:  # pragma: no cover
                self.plot_points(source_points, target_points, fig)
                plt.pause(0.1)

            #TODO:
            # call the nearest neighbour association functions
            # this functiosn gives you the indexes of the points in source_points 
            # which associate with target_points 
            indexes, error = ...


            #TODO:
            # fill and call the svd_estimation function on the associated points, 
            # remember to splice the source_points with the indexes you just calcualted
            
            Rt, Tt = ...
            #TODO:
            # update target points with Rt and Tt
            target_points = ...
            
            #calculate leftover error
            leftover_error = preError - error
            print("leftover error:", error)

            if leftover_error < 0:  # prevent matrix H changing, exit loop
                print("Not Converge...", preError, leftover_error, count)
                break

            preError = error
            #TODO:
            #update the H matrix using the update_H function
            H = ...

            if leftover_error <= self.EPS:
                print("Converge", error, leftover_error, count)
                break
            elif self.MAX_ITER <= count:
                print("Not Converge...", error, leftover_error, count)
                break
        #TODO:
        #extract R and T from H
        R = ...
        T = ...

        return R, T

    def update_H(self, Hin, R, T):
        r_size = R.shape[0]
        H = np.zeros((r_size + 1, r_size + 1))

        H[0:r_size, 0:r_size] = R
        H[0:r_size, r_size] = T
        H[r_size, r_size] = 1.0

        if Hin is None:
            return H
        else:
            return Hin @ H

    def nearest_association(self, source_points, target_points):
        # calc the sum of residual errors
        delta_points = source_points - target_points
        d = np.linalg.norm(delta_points, axis=0)
        error = sum(d)

        # calc index with nearest neighbor association
        d = np.linalg.norm(np.repeat(target_points, source_points.shape[1], axis=1)
                           - np.tile(source_points, (1, target_points.shape[1])), axis=0)
        indexes = np.argmin(d.reshape(target_points.shape[1], source_points.shape[1]), axis=1)

        return indexes, error


    #TODO: complete the svd estimation function to calculate Rotation and translation matrices 
    def svd_estimation(self, source_points: np.ndarray, target_points: np.ndarray):
        # calculate mean of the source points and target points, you can use the 
        # np.mean function, remember to pass the correct axis parameter to it 
        source_mean = ...
        target_mean = ...

        # calculate the shift of the points from their mean
        source_shift = ...
        target_shift = ...
    
        # calcualte cross covariance matrix
        W = ...

        # perform singular value decomposition of the covariance matrix, 
        # you can use the np.linalg.svd() function
        u, s, vh = ...
        # get rotation and translation matrix
        R = ...
        t = ...

        return R, t

    def plot_points(self, source_points, target_points, figure):
        # for stopping simulation with the esc key.
        plt.gcf().canvas.mpl_connect(
            'key_release_event',
            lambda event: [exit(0) if event.key == 'escape' else None])

        plt.cla()
        plt.plot(source_points[0, :], source_points[1, :], ".r")
        plt.plot(target_points[0, :], target_points[1, :], ".b")
        plt.plot(0.0, 0.0, "xr")
        plt.axis("equal")


class Simulation:
    def __init__(self, n_points=1000, field_length=50.0, motion=None, nsim=3):
        if motion is None:
            motion = [0.5, 2.0, np.deg2rad(-10.0)]  # movement [x[m],y[m],yaw[deg]]
        self.n_points = n_points
        self.field_length = field_length
        self.motion = motion
        self.nsim = nsim

    def run(self):
        icp = ICP()

        for _ in range(self.nsim):
            # previous points
            px = (np.random.rand(self.n_points) - 0.5) * self.field_length
            py = (np.random.rand(self.n_points) - 0.5) * self.field_length
            source_points = np.vstack((px, py))

            # current points
            cx = [math.cos(self.motion[2]) * x - math.sin(self.motion[2]) * y + self.motion[0]
                  for (x, y) in zip(px, py)]
            cy = [math.sin(self.motion[2]) * x + math.cos(self.motion[2]) * y + self.motion[1]
                  for (x, y) in zip(px, py)]
            target_points = np.vstack((cx, cy))

            R, T = icp.icp_matching(source_points, target_points)
            print("R:", R)
            print("T:", T)


if __name__ == '__main__':
    sim = Simulation()
    sim.run()
