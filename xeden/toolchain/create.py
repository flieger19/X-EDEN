"""
Documentation
"""

import sys
import os
import shutil

DEFAULT_TOOL = "/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/"
TOOLCHAINS_DIR = os.path.expanduser('~') + "/Library/Developer/Toolchains/"
XEDEN_TOOL = "X-EDEN.xctoolchain/"
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


def directory_iterator(source, target):
    """
    Iterates through a directory and symlinks all containing files in a target director with the same structure
    :param source: Directory to iterate through
    :param target: Directory to symlink files to
    """
    for file in os.listdir(source):
        filename = os.fsdecode(file)
        path_source = source + bytes("/", 'utf-8') + file
        path_target = target + bytes("/", 'utf-8') + file
        if os.path.isdir(path_source):
            directory_maker(os.fsdecode(path_target))
            directory_iterator(os.fsencode(path_source), os.fsencode(path_target))
        elif os.path.isfile(path_source):
            try:
                os.symlink(path_source, path_target)
            except:
                print("Symlink Error")
        elif os.access(path_source, os.X_OK):
            try:
                os.symlink(path_source, path_target)
            except:
                print("Symlink Error")
        elif os.path.islink(path_source):
            continue
        else:
            print("Special file ", path_source)


def create():
    """
    Creates X-EDEN Xcode toolchain
    """
    # gen tool chain
    usr_directory = "usr/"
    directory_maker(TOOLCHAINS_DIR + XEDEN_TOOL + usr_directory)

    # copy plist file
    info_file = "/Info.plist"
    toolchain_directory = "/toolchain"
    source = CURRENT_DIR + toolchain_directory + info_file
    target = TOOLCHAINS_DIR + XEDEN_TOOL + info_file
    try:
        shutil.copyfile(source, target)
    except IOError as error:
        print("Unable to copy file. %s" % error)
    except:
        print("Unexpected error:", sys.exc_info())

    # symlink
    directory_iterator(os.fsencode(DEFAULT_TOOL + usr_directory), os.fsencode(TOOLCHAINS_DIR + XEDEN_TOOL + usr_directory))

    # symlink lld
    sbin_directory = "usr/sbin/"
    directory_maker(TOOLCHAINS_DIR + XEDEN_TOOL + sbin_directory)
    source_lld = "/usr/local/opt/arm-none-eabi-llvm/bin/lld"
    target_lld = sbin_directory + "ld.lld"
    try:
        os.symlink(source_lld, TOOLCHAINS_DIR + XEDEN_TOOL + target_lld)
    except:
        print("Symlink Error")

    # symlink additional llvm tools
    bin_directory = "usr/bin/"
    directory_maker(TOOLCHAINS_DIR + XEDEN_TOOL + sbin_directory)
    source_path = "/usr/local/opt/arm-none-eabi-llvm/bin/"
    source_llvm_tools = ["llvm-size", "llvm-objcopy"]
    for source_llvm_tool in source_llvm_tools:
        try:
            os.symlink(source_path + source_llvm_tool, TOOLCHAINS_DIR + XEDEN_TOOL + bin_directory + source_llvm_tool)
        except:
            print("Symlink Error")

    # copy linker adaptor
    source_linker = "/xeden/linker/ld.lld"
    target_linker = "usr/bin/ld.lld"
    try:
        shutil.copyfile(CURRENT_DIR + source_linker, TOOLCHAINS_DIR + XEDEN_TOOL + target_linker)
    except IOError as error:
        print("Unable to copy file. %s" % error)
    except:
        print("Unexpected error:", sys.exc_info())
