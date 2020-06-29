from sklearn.cluster import KMeans
import cv2
import matplotlib.pyplot as plt
import numpy as np
from time import sleep


def HEXtoRGB(hexlist = None):

    if hexlist is None:
        raise TypeError("Hex Color List Not Found")

    else:
        rgblist = []
        for i in range(len(hexlist)):
            h = hexlist[i].lstrip('#')
            rgb = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
            rgblist.append(rgb)
    
        return(rgblist)


def ExtractColors(img, clust = 3):
    
    if img.lower().endswith(('.png', '.jpg', '.jpeg')):
        
        image = cv2.imread(img)

        height, width = image.shape[:2]

        if height > 1000 and width >1000:
            
            #percent by which the image is resized
            scale_percent = 30

            #calculate the 50 percent of original dimensions
            width = int(image.shape[1] * scale_percent / 100)
            height = int(image.shape[0] * scale_percent / 100)

            # dsize
            dsize = (width, height)

            # resize image
            image = cv2.resize(image, dsize)
        
        else:
            pass
            
        # load the image and convert it from BGR to RGB so that
        # we can dispaly it with matplotlib
        
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # reshape the image to be a list of pixels
        image = image.reshape((image.shape[0] * image.shape[1], 3))
        # cluster the pixel intensities

        print("please wait,This may take a moment :)")
        ExtractColors.clt = KMeans(n_clusters = clust)
        ExtractColors.clt.fit(image)

        colors = ExtractColors.clt.cluster_centers_
        colors = colors.astype(int)
        #convert numpy array into list
        rgblist = np.array(colors).tolist()
        hexlist = ['#%02x%02x%02x'%tuple(i) for i in rgblist]

        for i in range(21):
            # the exact output you're looking for:
            print ("\r[%-21s] %d%%" % ('='*i, 5*i), end='')
            sleep(0.25)
        
        print("")
        
        return(hexlist)

    else:
        raise ValidationError("Only .jpg and .png images can be accepted")

   

def centroid_histogram():
    # grab the number of different clusters and create a histogram
    # based on the number of pixels assigned to each cluster
    numLabels = np.arange(0, len(np.unique(ExtractColors.clt.labels_)) + 1)
    (hist, _) = np.histogram(ExtractColors.clt.labels_, bins = numLabels)
    # normalize the histogram, such that it sums to one
    hist = hist.astype("float")
    hist /= hist.sum()
    # return the histogram
    return hist

def ClusterAnalysis(hexlist = None):

    if hexlist is None:
        raise TypeError("Hex Color List Not Found")
    else:
        hist = centroid_histogram()

        fig, ax = plt.subplots(figsize=(8, 4), subplot_kw=dict(aspect="equal"), facecolor='#FAFAFA')

        clrcode = hexlist
        data = hist.tolist()
        print(data)
        color = hexlist

        wedges, texts, autopcts = ax.pie(data, colors = color ,autopct='%1.1f%%',pctdistance=0.7, wedgeprops=dict(width=0.5, linewidth = 3, edgecolor = 'white'), startangle=-40)
        plt.setp(autopcts, **{'color':'white', 'weight':'bold', 'fontsize':8})
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
        

    