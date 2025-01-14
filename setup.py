import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyubee",
    version="0.12",
    author="Miroslav Zdrale",
    author_email="mzdrale@gmail.com",
    description="Simple library for getting stats from Ubee routers.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/mzdrale/pyubee',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': ['pyubee=pyubee.__main__:main']
    },

)
