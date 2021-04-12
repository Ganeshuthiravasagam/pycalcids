import setuptools 
with open("README.md", "r") as fh:
   long_description = fh.read()

setuptools.setup(
    #package name.
    name="py-calci-ds",
    #version of the package
    version="1",
    author="Ganesh Uthiravasagam",
    author_email="ganeshuthiravasagam@gmail.com",
 
    #Small Description about module
    description="Pycalcids",
 
    long_description=long_description,
 
    #Specifying that we are using markdown file for description
    long_description_content_type="text/markdown",
 
    url="https://github.com/Ganeshuthiravasagam",
    packages=setuptools.find_packages(),

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
