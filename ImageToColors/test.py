from ImageToColors import *

img = "image.png" # .png or .jpg
clust = 5 # Cluster value nothing but the how many dominant colors user want to extract

#to print extracted colors list use imgtColors() function
ic = Extract(img, clust)
colorslist = ic.imgtColors()
print(colorslist)

#For graphical analysis use analysis()
ic.analysis()