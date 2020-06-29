from ImageToColors import *

img = "test/colors.jpg" # .png or .jpg
clust = 5 # Cluster value nothing but the how many dominant colors user want to extract

#to print extracted colors list use ExtractColors() function
HEXlist= ExtractColors(img,clust)
print(HEXlist)

# To convert Hex color list to RGB use HEXtoRGB
RGBlist = HEXtoRGB(HEXlist)
print(RGBlist)

#For graphical analysis use ClusterAnalysis()
ClusterAnalysis(HEXlist)


