# X-EDEN

**X**code **E**mbedded **DE**velopme**N**t installs an extended Xcode toolchain on basis of the default toolchain in `~/Library/Developer/Toolchains/`. The toolchain is extended by a few additional LLVM tools like `lld`, `llvm-objcopy`, `llvm-size`, and a script to adopt `lld` to work with Xcode.

## Installation

First install the `arm-none-eabi-llvm` compiler:

```bash
brew tap eblot/armeabi
brew install arm-none-eabi-llvm
```

Clone the repository or download `.zip` archive. 

Next execute the following command:

```bash
python3 setup.py
```

## Usage

Choose the X-EDEN toolchain in the Xcode main menu under Toolchains.

## Subpackages

* [X-ARM](https://github.com/flieger19/X-ARM) Xcode templates for embedded arm cortex-m development.