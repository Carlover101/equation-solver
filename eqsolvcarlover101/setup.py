import setuptools

with open("/home/runner/Package/eqsolvcarlover101/README.md", "r") as fhandle:
    long_description = fhandle.read()

setuptools.setup(
    name="eqsolvcarlover101",
    version="1.1.2",
    author="Zakkai Thomas",
    author_email="zmanmustang2017@gmail.com",
    description="Automatic equation solver",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Carlover101/equation-solver",
    packages=["eqsolvcarlover101/equation","eqsolvcarlover101"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
