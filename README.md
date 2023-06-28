# File Sorter
## goit-python-hw-06

A Python program to sort files in a target directory based on their extensions.

Tested on: Linux pop-os 6.2.6-76060206-generic

## Table of Contents

- [Description](#description)
- [Usage](#usage)
- [Installation](#installation)
- [Disclaimer](#disclaimer)

## Description

The File Sorter is a Python program that recursively scans a target directory to find files and categorizes them into different directories based on their extensions. It supports various file types such as videos, pictures, documents, music, archives, notes, and ISO images. The program uses a set of predefined file extensions to determine the category of each file.

## Usage

1. Ensure you have Python installed on your system.
2. Clone this repository or download the `sort.py` file.
3. Open a terminal and navigate to the directory containing the `sort.py` file.
4. Run the following command:

```bash
python file_sorter.py TARGET_DIR/
```

Replace TARGET_DIR/ with the path to your target directory that you want to sort.

5. The program will recursively scan the target directory, categorize the files, and move them to their respective directories based on their extensions.

    A log file named sort.log will be created in the target directory, containing the details of the sorting process.

## Installation

Clone this repository:

```bash
git clone https://github.com/username/repo.git
```

Replace username and repo with your GitHub username and the repository name, respectively.

Alternatively, you can directly download the file_sorter.py file from the repository.


## Disclaimer

**Please note that the use of this code is at your own risk.**

The code provided in this repository is for educational and informational purposes only. It is not intended to be a production-ready or fully tested solution. While efforts have been made to ensure the accuracy and reliability of the code, there is no guarantee that it is error-free or suitable for your specific needs.

**No Warranty**

The code is provided "as is" without any warranty, express or implied. This includes but is not limited to warranties of merchantability, fitness for a particular purpose, and non-infringement. The author(s) and/or contributors of this repository disclaim any warranty and accept no liability for damages or losses arising from the use or misuse of the code.

**Use at Your Own Risk**

You acknowledge and agree that you will be solely responsible for any consequences that arise from using the code. The author(s) and/or contributors of this repository shall not be held liable for any direct, indirect, incidental, special, or consequential damages or losses resulting from the use of the code.

**No Liability**

The author(s) of this repository accept no liability for any damages or losses, whether direct, indirect, incidental, special, or consequential, arising from the use or misuse of the code. This includes but is not limited to damages or losses caused by errors, inaccuracies, omissions, or any other defects in the code.

It is recommended to thoroughly review and test the code before using it in any production environment. You should adapt and modify the code according to your own requirements and follow best practices to ensure security and reliability.

By using this code, you signify your acceptance of this disclaimer. If you do not agree with these terms, you should refrain from using the code.

**License**

This project is licensed under the MIT License.
