from setuptools import setup, find_packages


setup(
    name="decompose",
    author="setanarut",
    version="0.1.0",
    url="https://github.com/TaylorHawkes/decompose",
    packages=find_packages(),
    scripts=["scripts/decomp"],
    package_data={"decompose": ["model/*.pth"]},
    description="Decompose image into layers",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "pyora>=0.3.11",
        "numpy==1.26.1",
        "Pillow==10.1.0",
        "guided_filter_pytorch==3.7.5",
        "torch==2.1.0",
    ],
    python_requires=">=3.10",
)
