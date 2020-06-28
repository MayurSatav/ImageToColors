# ImageToColors

ImageToColors is a Image color clustering library for extracting N dominant colors from image.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install ImageToColors.

```
pip install ImageToColors
```

## Usage

```python
from ImageToColors import *

img = "image.png" # .png or .jpg
clust = 5 # Cluster value nothing but the how many dominant colors user want to extract

#to print extracted colors list use imgtColors() function
ic = Extract(img, clust)
colorslist = ic.imgtColors()
print(colorslist)

#For graphical analysis use analysis()
ic.analysis()
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
Distributed under the MIT License. See LICENSE for more information.
