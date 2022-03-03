import setuptools
import os.path

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setuptools.setup(
    name="eqsolvcarlover101",
    version="1.4",
    author="Zakkai Thomas",
    author_email="zmanmustang2017@gmail.com",
    description="Automatic equation solver",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/Carlover101/equation-solver",
    packages=["eqsolvcarlover101/equation","eqsolvcarlover101"],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
