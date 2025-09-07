from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension, build_ext

ext_modules = [
    Pybind11Extension(
        "pytinytransfer",
        sources = [
            'binder.cpp', 
            'tinytransfer/tinyTransfer.cpp'],
        include_dirs = [
            "tinytransfer",
            "tinytransfer/heatshrink"
                        ],
    ),
]

setup(
    name="pytinytransfer",
    version="0.9.0",
    author="Julian Maynes",
    author_email="julianmaynes16@gmail.com",
    description="RPL communication protocol",
    long_description="",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    extras_require={"test": ["pytest>=6.0"]},
    python_requires=">=3.7",
)
