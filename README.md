
# Rotaforce - by Téo Haÿs

A small python utility to brute force rotational ciphers.
Usage : python3 brute.py <charset> <ciphered_text>

The latest release (0.1b - codename Sarah) is out ! Feel free to download it and try it on your machine !
This release has been tested with [bandit]([https://github.com/PyCQA/bandit](https://github.com/PyCQA/bandit)), and showed no Python vulnerability. Yay !

## Purpose

You can use this utility to brute force different **rotational** ciphers :
- Decimal rotational ciphers like ROT-5
- Alpha rotational ciphers such as ROT-13 or Caesar
- ASCII rotational ciphers

## Requirements
This program has been developed on Ubuntu 18.04 using Python 3.6.8 64-bit.
Please note that **it is not able to run on Python 2** as we use Python 3 specific arguments in some function.

Even though it has only been tested on Ubuntu 18, it should also work on any Linux system which support Python 3. If I ever test this program on other systems I'll let you know here.

The biggest mystery for me is "will it work on Windows ?" though.

Shall you have any requests about this software, send them at [teo@couaque.fr](mailto:teo@couaque.fr)

## Quality of the code
Even though this code is probably not the cleanest Python code you ever saw, it works fine !
Do not hesitate to propose pull requests in order to participate to this project.