# ImageToColors

[![PyPI license](https://img.shields.io/pypi/l/ImageToColors.svg)](https://pypi.org/project/ImageToColors/)

ImageToColors is a Image color clustering library for extracting N dominant colors from image and provide list of extracted colors in HEX format.THe prime purpose of this library is to provide quick colors extraction. It has `ExtractColors()` function which deals with clustering it also operate image according to their sizes for fast and secure clustering. It also provides `HEXtoRGB()` conversion function.For Graphical analysis `ImageToColors` gives you `ClusterAnalaysis()` using this function one can analyze color values along with each color percentage present in given image 

## Installation

The easiest way to install the library is to execute

```
pip install ImageToColors
```

(note that you need network access to do it this way; if you do not have the *pip* tool installed -- see: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).

Alternatively, you can `download`_ the library source archive, unpack it, `cd` to the unpacked directory and execute the following command
```
python setup.py install
```
It is also possible to use the library without installing it: as its code is contained in a single file (``IMageToColors.py``), you can just copy it into your project.

## Functions

#### ExtractColors()
It takes 2 arguments `image` and `cluster value` which is nothing but the integer value for number of colors want to extract.`ExtractColors()` takes any image having `.jpg`, `.jpeg`, `.png` any one of them extension.It returns a list of hex color code list.

```
['#46a947', '#ed3723', '#0b66b5', '#af60a8', '#fbbf10']
```

#### HEXtoRGB()
 
It takes single `HEX` colors list argument and convert returns a `RGB` colors code list
```
[(70, 169, 71), (237, 55, 35), (11, 102, 181), (175, 96, 168), (251, 191, 16)]
```

#### ClusterAnalysis()

It takes extracted `HEX` colors list and plot the donut graph showing color code and percentage of colors present in given image.

![](https://github.com/MayurSatav/ImageToColors/blob/master/ImageToColors/test/output.png)
![Output]('https://github.com/MayurSatav/ImageToColors/blob/master/ImageToColors/test/output.png')


## Usage

```python
from ImageToColors.ImageToColors import *

img = "image.jpg" # .png or .jpg
clust = 5 # Cluster value nothing but the how many dominant colors user want to extract

#to print extracted colors list use ExtractColors() function
HEXlist= ExtractColors(img,clust)
print(HEXlist)

# To convert Hex color list to RGB use HEXtoRGB
RGBlist = HEXtoRGB(HEXlist)
print(RGBlist)

#For graphical analysis use ClusterAnalysis()
ClusterAnalysis(HEXlist)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
Distributed under the MIT License. See ![LICENSE]('https://github.com/MayurSatav/ImageToColors/blob/master/LICENSE.txt') for more information.
