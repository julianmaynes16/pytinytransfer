import os
import re
import subprocess
import sys
from pathlib import Path

from setuptools import setup, Extension
#from pybind11.setup_helpers import Pybind11Extension, built_ext

# Convert distutils Windows platform specifiers to CMake -A arguments
PLAT_TO_CMAKE = {
    "win32": "Win32",
    "win-amd64": "x64",
    "win-arm32": "ARM",
    "win-arm64": "ARM64",
}

ext_modules = [
    Extension(
        "pytinytransfer",
        ['binder.cpp'],
    ),
]


# The information here can also be placed in setup.cfg - better separation of
# logic and declaration, and simpler if you include description/version in a file.
setup(
    name="pytinytransfer",
    version="0.9.0",
    author="Julian Maynes",
    author_email="julianmaynes16@gmail.com",
    description="RPL communication protocol",
    long_description="",
    ext_modules=ext_modules,
    #cmdclass={"build_ext":build_ext},
    zip_safe=False,
    extras_require={"test": ["pytest>=6.0"]},
    python_requires=">=3.7",
)
