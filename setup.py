import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(
    
    name='ImageToColors',  

    version='0.1',

    author="Mayur Satav",

    author_email="mayursatav9@gmail.com",

    description="Image color clustering library for extracting N dominant colors from image",

    long_description=long_description,

    long_description_content_type="text/markdown",

    url="https://github.com/MayurSatav/ImageToColors",

    packages=setuptools.find_packages(),

    classifiers=[

        "Programming Language :: Python :: 3",

        "License :: OSI Approved :: MIT License",

        "Operating System :: OS Independent",

     ],

 )