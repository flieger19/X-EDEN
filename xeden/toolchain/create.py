"""
Documentation
"""

import sys
import os
import shutil

DEFAULT_TOOL = "/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/"
XEDEN_TOOL = os.path.expanduser('~') + "/Library/Developer/Toolchains/X-EDEN.xctoolchain/"
CURRENT_DIR = os.path.abspath(os.getcwd())


def directory_maker(path):
    """
    Makes specified directory
    :param path: directory to make
    """
    try:
        os.makedirs(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
