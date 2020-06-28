from sklearn.cluster import KMeans
import cv2
import matplotlib.pyplot as plt
import numpy as np
from time import sleep


class Extract:

    def __init__(self, myimage, myclusters = 4):
        self.IMAGE = myimage 
        self.CLUSTERS = myclusters
        self.clt = None

    def RGBtoHEX(self,rgblist):
        hexlist = ['#%02x%02x%02x'%tuple(i) for i in rgblist]
        return(hexlist)

    def imgtColors(self):
        # load the image and convert it from BGR to RGB so that
        # we can dispaly it with matplotlib
        image = cv2.imread(self.IMAGE)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # reshape the image to be a list of pixels
        image = image.reshape((image.shape[0] * image.shape[1], 3))
        # cluster the pixel intensities

        print("please wait,This may take a moment :)")
        self.clt = KMeans(n_clusters = self.CLUSTERS)
        self.clt.fit(image)

        colors = self.clt.cluster_centers_
        colors = colors.astype(int)
        #convert numpy array into list
        rgblist = np.array(colors).tolist()
        hexlist = ['#%02x%02x%02x'%tuple(i) for i in rgblist]

        '''for i in range(21):
            # the exact output you're looking for:
            print ("\r[%-21s] %d%%" % ('='*i, 5*i), end='')
            sleep(0.25)
        
        print("")'''
        
        return(hexlist)

    def centroid_histogram(self):

        # grab the number of different clusters and create a histogram
        # based on the number of pixels assigned to each cluster
        numLabels = np.arange(0, len(np.unique(self.clt.labels_)) + 1)
        (hist, _) = np.histogram(self.clt.labels_, bins = numLabels)
        # normalize the histogram, such that it sums to one
        hist = hist.astype("float")
        hist /= hist.sum()
        # return the histogram
        return hist

    def display(self):

        colors = self.clt.cluster_centers_
        colors = colors.astype(int)
        #convert numpy array into list
        colors = np.array(colors).tolist()
        rgblist = ((self.clt.cluster_centers_).astype(int)).tolist()

        hist = self.centroid_histogram()

        fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"), facecolor='#FAFAFA')

        clrcode = self.RGBtoHEX(rgblist)
        data = hist.tolist()
        color = self.RGBtoHEX(rgblist)

        wedges, texts = ax.pie(data, colors = color , wedgeprops=dict(width=0.5, linewidth = 3, edgecolor = 'white'), startangle=-40)

        bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
        kw = dict(arrowprops=dict(arrowstyle="-"),
                bbox=bbox_props, zorder=0, va="center")

        for i, p in enumerate(wedges):
            ang = (p.theta2 - p.theta1)/2. + p.theta1
            y = np.sin(np.deg2rad(ang))
            x = np.cos(np.deg2rad(ang))
            horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
            connectionstyle = "angle,angleA=0,angleB={}".format(ang)
            kw["arrowprops"].update({"connectionstyle": connectionstyle})
            ax.annotate(clrcode[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y), horizontalalignment=horizontalalignment, **kw)

        plt.show()

