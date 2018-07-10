#!/usr/bin/env python3
import os
from setuptools import setup, find_packages


def find_data(relpath, folder):
    dir_content = []
    path = os.path.join(relpath, folder)
    tree = [(dirname, filenames) for dirname, _, filenames in os.walk(path)
            if filenames]

    for root, files in tree:
        path = os.path.relpath(root, relpath)
        dir_content.extend(map(lambda x: os.path.join(path, x), files))

    return dir_content


def package_data(relpath, folders):
    all_files = []
    for folder in folders:
        all_files.extend(find_data(relpath, folder))

    return all_files


setup(
    name="dragoon-terminal",
    version="1.0.0",  # Copied from package.json

    description="Dragoon terminal themes.",
    long_description="""
Dragoon Terminal Themes.

Terminal backgrounds from The Legend of Dragoon.

Change the Terminal Background & Desktop Wallpaper.
Supports ITerm2, Terminology & Tilix.
Forked from Pokemon-Terminal by LazoCoder.""",
    url="https://github.com/BitBruce/Dragoon-Terminal",

    author="BitBruce",
    author_email="",

    license="GPLv3",

    packages=find_packages(exclude=['tests']),

    package_data={
        "dragoonterminal": package_data("dragoonterminal", ["Data", "Images"]),
    },

    scripts=['dragoon'],

    keywords="dragoon terminal theme style dragoon-terminal",

    classifiers=[
        "Development Status :: 1 - Alpha",

        "Intended Audience :: End Users/Desktop",
        "Environment :: Console",
        "Topic :: Utilities",

        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",

        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],

    python_requires=">=3.6"
)
