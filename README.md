# Boto3 Toolkit
This repository contains AWS related script written in Python3.X using boto3 package.

## Prerequisites
Below prerequisites must be fulfilled for successful execution of code.

### Software Requirement
Resources in nested directories are meant for use with Python 3.x (check the version using `python3 --version`). If you don't have the compatible version, download it from official python repository. Make sure to install python package manager - pip3 (check the version using `pip3 --version`) as well.

- [python3](https://www.python.org/downloads/) >= 3.14.6
- [pip3](https://pypi.org/project/pip/) >= 26.1.2

#### Python Installation
To install python3, pip3 and python3-venv on ubuntu operating system using apt package manager, use below command.

```bash
sudo apt update
sudo apt install python3
sudo apt install python3-pip
sudo apt install python3-venv

python3 --version
pip3 --version
```

### Bootstrap Virtual Environment
It is a best practice to create a virtual environment for your coding to avoid any conflict in dependencies between multiple applications. Hence, We will need to create a virtual environment (using python's default package "venv") and install all the dependencies.

```bash
python3 -m venv boto3-venv # on Windows, use "python -m venv boto3-venv" instead
source boto3-venv/bin/activate # on Windows, use "boto3-venv\Scripts\activate" instead
pip install -r requirements.txt
```

## Execution
To run the script - go to command prompt, activate the virtual environment and hit the following command:

```bash
python </path/to/the/pythonscript>
```
