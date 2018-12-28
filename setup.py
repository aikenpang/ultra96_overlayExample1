from setuptools import setup, find_packages
import subprocess
import sys
import shutil
import add_overlay

setup(
    name = "add_overlay",
    url = 'https://github.com/aikenpang/ultra96_overlayExample1',
    license = 'All rights reserved.',
    author = "Aiken Pang",
    author_email = "aikenpang@gmail.com",
    packages = ['add_overlay'],
    package_data = {
    '' : ['*.bit','*.tcl','*.py','*.so'],
    },
    description = "Example#1 Adder overlay for ULTRA96"
)