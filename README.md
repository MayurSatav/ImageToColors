# ImageToColors

ImageToColors is a Image color clustering library for extracting N dominant colors from image.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install ImageToColors.

```
pip install ImageToColors
```

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
Distributed under the MIT License. See LICENSE for more information.
