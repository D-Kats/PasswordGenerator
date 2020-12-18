# PasswordGenerator
A small python tool to manually generate password list text files. 

**PasswordGenerator** is a small python tool to generate password lists to be used as a wordlists with various forensic tools. 

The tool will take a set of characters as input by the user and create a text file with one password by line. Passwords are being generated by permutations of the given characters, from a password length of two characters up to the length of the total characters given by the user. 

## Installation

This is a tool written in Python (version 3.8.5 used). The .exe file (**PasswordGenerator.exe**) works on Microsoft Windows based machines by just double clicking.

The source code file (**PasswordGenerator.py**) can be run on a system with python 3 installed (Version 3.6 or newer needed). It only needs one additional third party library to run successfully. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install them.

```bash
pip install PySimpleGUI
```
for the [PySimpleGUI](https://pypi.org/project/PySimpleGUI/) module from  MikeTheWatchGuy at https://pypi.org/project/PySimpleGUI/

## Usage

![GitHub Logo](/MAINGUI.PNG)

The tool comes with a GUI interface. User has to provide the tool with any character he wishes the generated passwords to contain. Characters have to be separated by coma.

User can choose an output folder for the generated password wordlist text file to be saved or leave it blank so that the output text file will be saved in the running exe folder.


## IMPORTANT INFO

- Tool writes the wordlist file in utf-8 so any language can be used for the password generation.

- The tool can accept whole words or even phrases and not just characters. Each word or phrase should be separated by coma and that way it will be considered as one element for the password creation procedure, thus being scrambbled with every other character/word/phrase provided.

- All signs and special characters can also be used as input characters for the password generation, except a '**coma**' character which is used as the separator! 

## License
[MIT](https://github.com/D-Kats/FileHarvester/blob/main/LICENSE)
