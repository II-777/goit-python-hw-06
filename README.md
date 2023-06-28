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

## Features

- Automatic file organization: The program scans the target directory and automatically sorts files into different categories based on their file extensions.
- Customizable file categories: The supported file categories and their associated extensions can be easily modified to fit your needs.
- Transliteration support: The program can handle filenames with Cyrillic symbols and transliterate them into Latin symbols.
- Duplicate file handling: When moving files, the program checks for duplicate filenames in the destination directory and appends a unique number to avoid overwriting existing files.
- Logging: The program creates a log file with timestamped information about the sorting process, including the original and renamed file paths.

## Prerequisites

- Python 3.6 or above
- pathlib library
- shutil library
- sys library
- re library

## Supported File Categories

The program categorizes files into the following categories based on their extensions:

- Videos: MP4, AVI, MKV, MOV, WMV, FLV, WEBM, MPEG, MPG, 3GP
- Pictures: JPG, JPEG, PNG, GIF, BMP, SVG, WEBP, TIF, TIFF, ICO
- Documents: DOC, DOCX, PDF, RTF, ODT, ODS, ODP, PPT, PPTX, XLS, XLSX, CSV, XML, HTML, HTM, TEX
- Music: MP3, WAV, WMA, OGG, FLAC, AAC, AMR, M4A, M3U, MID
- Archives: ZIP, 7Z, TAR, GZ, BZ2, XZ, TGZ, TBZ2
- Notes: '', MD, TXT,
- Images: ISO, IMG

Files with extensions not listed above will be categorized as "other".

## Customization

You can customize the file categories and their associated extensions by modifying the EXT_BY_TYPE dictionary in the script. Add or remove file extensions as needed to suit your requirements.
Example

## Usage

1. Ensure you have Python installed on your system.
2. Clone this repository or download the `sort.py` file.
3. Open a terminal and navigate to the directory containing the `sort.py` file.
4. Run the following command:

```bash
python sort.py TARGET_DIR/
```

Replace TARGET_DIR/ with the path to your target directory that you want to sort.


The program will recursively scan the target directory, categorize the files, and move them to their respective directories based on their extensions. A log file named `sort.log` will be created in the target directory, containing the details of the sorting process.

## Example:

To sort files in the directory /home/user1/Desktop/Unsorted, run the following command:

```shell
python file_sorter.py /home/user1/Desktop/Unsorted
``` 

## Installation

Clone this repository:

```bash
git clone https://github.com/II-777/goit-python-hw-06.git
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
