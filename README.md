# File Sorter
## goit-python-hw-06

A Python program to sort files in a target directory based on their extensions.

## Table of Contents

- [Description](#description)
- [Usage](#usage)
- [Installation](#installation)
- [License](#license)

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

## License

This project is licensed under the MIT License.
