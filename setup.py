"""
Documentation, License etc.

@package X-EDEN Xcode Embedded DEvelopmeNt
"""
import sys
import subprocess

import xeden.__main__ as xeden


def ensure_installed(tool):
    """
    Checks if a given tool is installed and in PATH
    :param tool: Tool to check if installed and in PATH
    :return: Full path of the tool
    """
    proc = subprocess.Popen('export PATH=$PATH:/usr/local/opt/arm-none-eabi-llvm/bin/ && which ' + tool, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out, err = proc.communicate()
    exitcode = proc.returncode
    if exitcode == 0:
        print('Found {t} install in "{p}"'.format(t=tool, p=out.strip()))
        return out.strip()
    else:
        print(tool + ' is not installed (or is not in the PATH).')
        return out.strip()


def main(argv=sys.argv):
    exit_code = 0

    # check tool chain
    model = {}
    tools = ['lld', 'llvm-objcopy', 'llvm-size']
    for tool in tools:
        model[tool] = ensure_installed(tool)

    exit_code = xeden.main(argv)

    return exit_code


if __name__ == "__main__":
    sys.exit(main(sys.argv))
